from Visitor import Visitor
from StaticError import *
from AST import *


def type_of(typ):
    if type(typ) is type(AST):
        return typ
    else:
        return type(typ)


def is_same_type(typ1, typ2):
    return str(typ1) == str(typ2)


def get_type(symbol):
    if type_of(symbol) in [VarDecl, ParamDecl]:
        return symbol.typ
    if type_of(symbol) is FuncDecl:
        return symbol.return_type
    return symbol


def set_type(symbol, typ):
    if type_of(symbol) in [VarDecl, ParamDecl]:
        symbol.typ = typ
    elif type_of(symbol) is FuncDecl:
        symbol.return_type = typ


class FloatOrInteger:
    pass


class ScopeMarker:
    def __init__(self, owner=None):
        self.owner = owner


class Inspector:
    def __init__(self):
        self.scope_stack = [ScopeMarker()]
        self.is_first_pass = True
        self.override_auto = None
        self.possible_types = None
        self.lhs_type = None
        self.lhs_exception = None
        self.func_return_type = None
        self.func_call_stack = []

    def reset_states(self):
        self.override_auto = None
        self.possible_types = None
        self.lhs_type = None
        self.lhs_exception = None
        self.func_return_type = None

    def add_symbol(self, o):
        self.scope_stack.append(o)

    def push_scope(self, owner=None):
        if owner is None:
            self.scope_stack.append(ScopeMarker())
        else:
            self.scope_stack.append(ScopeMarker(owner))

    def pop_scope(self, owner=None):
        for i in reversed(range(len(self.scope_stack))):
            element = self.scope_stack.pop()
            if owner is None:
                if type_of(element) is ScopeMarker:
                    return
            else:
                if type_of(element) is ScopeMarker and type_of(element.owner) == type_of(owner):
                    return

    def find_latest_name(self, name: str) -> Decl:
        for i in reversed(range(len(self.scope_stack))):
            if type_of(self.scope_stack[i]) in [VarDecl, ParamDecl, FuncDecl]:
                if self.scope_stack[i].name == name:
                    return self.scope_stack[i]
        return None

    def find_latest_name_of_type(self, name: str, types: [Type], exception=None) -> Decl:
        for i in reversed(range(len(self.scope_stack))):
            if type_of(self.scope_stack[i]) in types and self.scope_stack[i].name == name:
                return self.scope_stack[i]
        if exception:
            raise exception

    def is_marker_in_scope(self, marker_types: List[Type]) -> bool:
        for i in range(len(self.scope_stack)):
            if type_of(self.scope_stack[i]) is ScopeMarker and type_of(self.scope_stack[i].owner) in marker_types:
                return True
        return False

    def check_redeclared(self, symbol: Decl, kind: Kind):
        for i in reversed(range(len(self.scope_stack))):
            if type_of(self.scope_stack[i]) is ScopeMarker:
                return
            if self.scope_stack[i].name == symbol.name:
                raise Redeclared(kind, symbol.name)

    def check_undeclared(self, symbol: Decl, kind: Kind):
        if self.find_latest_name(symbol.name) is None:
            raise Undeclared(kind, symbol.name)

    def check_invalid(self, symbol, typ):
        if type_of(typ) is Variable:
            if type_of(symbol.typ) is AutoType and symbol.init is None:
                raise Invalid(Variable(), symbol.name)

    def get_latest_marker(self, marker_type=None) -> ScopeMarker:
        for i in reversed(range(len(self.scope_stack))):
            if type_of(self.scope_stack[i]) is ScopeMarker:
                if marker_type is None:
                    return self.scope_stack[i]
                elif type_of(self.scope_stack[i].owner) is marker_type:
                    return self.scope_stack[i]
        return None


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, Inspector())

    def infer(self, lhs, rhs, exception):
        lhs_type = get_type(lhs)
        rhs_type = get_type(rhs)

        if type_of(lhs_type) is ArrayType or type_of(rhs_type) is ArrayType:
            if type_of(lhs) is ArrayLit:
                for exp in lhs.explist:
                    self.infer(exp, rhs.typ, exception)

            if type_of(rhs) is ArrayLit:
                for exp in rhs.explist:
                    self.infer(exp, lhs.typ, exception)

        if type_of(lhs_type) is FuncCall or type_of(rhs_type) is FuncCall:
            return

        if type_of(lhs_type) is AutoType:
            set_type(lhs, rhs_type)
        elif type_of(rhs_type) is AutoType:
            set_type(rhs, lhs_type)
        elif type_of(lhs_type) is FloatType and type_of(rhs_type) is IntegerType:
            pass
        elif not is_same_type(lhs_type, rhs_type):
            raise exception

    def call_func(self, function_name, params, inspector, exception, return_type=None):
        # 3.4 Type Mismatch In Expression
        func_decl = inspector.find_latest_name_of_type(function_name, [FuncDecl], Undeclared(Function(), function_name))

        inspector.func_call_stack.append(func_decl)

        if func_decl.name == 'preventDefault':
            if len(params) > 0:
                raise TypeMismatchInExpression(params[0])

        # Parameters must match
        if len(func_decl.params) != len(params):
            if func_decl.name == 'super':
                raise TypeMismatchInExpression(params)
            else:
                raise exception

        for i in range(len(params)):
            arg = self.visit(params[i], inspector)
            if func_decl.name == 'super':
                self.infer(func_decl.params[i], arg, TypeMismatchInExpression(params[i]))
            else:
                self.infer(func_decl.params[i], arg, exception)

        if return_type and type_of(func_decl.return_type) is AutoType:
            func_decl.return_type = return_type

        for line in func_decl.body.body:
            if type_of(line) is ReturnStmt:
                self.visit(line, inspector)

        inspector.func_call_stack.pop()

        return func_decl

    def visitProgram(self, program: Program, inspector: Inspector):
        self.visit(FuncDecl('readInteger', IntegerType(), [], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('printInteger', VoidType(), [ParamDecl('anArg', IntegerType())], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('readFloat', FloatType(), [], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('writeFloat', VoidType(), [ParamDecl('anArg', FloatType())], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('readBoolean', BooleanType(), [], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('printBoolean', VoidType(), [ParamDecl('anArg', BooleanType())], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('readString', StringType(), [], None, BlockStmt([])), inspector)
        self.visit(FuncDecl('printString', VoidType(), [ParamDecl('anArg', StringType())], None, BlockStmt([])), inspector)

        for decl in program.decls:
            self.visit(decl, inspector)

        inspector.is_first_pass = False

        for decl in program.decls:
            self.visit(decl, inspector)

        # 3.9 No entry point
        main_func = inspector.find_latest_name('main')
        if main_func is None or type_of(main_func) is not FuncDecl or type_of(main_func.return_type) is not VoidType or len(main_func.params) != 0:
            raise NoEntryPoint()

        return []

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, inspector: Inspector):
        if inspector.is_first_pass:
            return

        # 3.1 Redeclared Variable
        inspector.check_redeclared(var_decl, Variable())

        # 3.3 Invalid Variable
        inspector.check_invalid(var_decl, Variable())

        inspector.add_symbol(var_decl)

        if var_decl.init is not None:
            inspector.lhs_type = var_decl.typ
            inspector.lhs_exception = TypeMismatchInVarDecl(var_decl)
            init = self.visit(var_decl.init, inspector)
            if inspector.possible_types and type_of(init) not in inspector.possible_types:
                raise TypeMismatchInVarDecl(var_decl)
            self.infer(var_decl, init, TypeMismatchInVarDecl(var_decl))

            inspector.reset_states()

        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, inspector: Inspector):
        if inspector.is_first_pass:
            return

        # 3.1 Redeclared Parameter
        inspector.check_redeclared(param_decl, Parameter())

    def visitFuncDecl(self, func_decl: FuncDecl, inspector: Inspector):
        if inspector.is_first_pass:
            inspector.check_redeclared(func_decl, Function())

            inspector.add_symbol(func_decl)

            if func_decl.name == 'super' or func_decl.name == 'preventDefault':
                raise Redeclared(Function(), func_decl.name)

            param_names = []
            for param in func_decl.params:
                if param.name in param_names:
                    raise Redeclared(Parameter(), param.name)
                param_names.append(param.name)

            return

        inspector.push_scope(func_decl)

        if func_decl.inherit:
            parent_func_decl = inspector.find_latest_name_of_type(func_decl.inherit, [FuncDecl], Undeclared(Function(), func_decl.inherit))

            # 3.3 Invalid Variable/Parameter declaration
            param_names = list(map(lambda p: p.name, func_decl.params))
            for parent_param in parent_func_decl.params:
                if parent_param.inherit and parent_param.name in param_names:
                    raise Invalid(Parameter(), parent_param.name)

            # 2.3 Inheritance features
            inspector.add_symbol(self.visit(FuncDecl('super', parent_func_decl.return_type, parent_func_decl.params, None, BlockStmt([])), inspector))
            inspector.add_symbol(self.visit(FuncDecl('preventDefault', VoidType(), [], None, BlockStmt([])), inspector))

        for param in func_decl.params:
            self.visit(param, inspector)
            inspector.add_symbol(param)

        self.visit(func_decl.body, inspector)

        inspector.pop_scope(func_decl)

        return func_decl

    # endregion

    # region Statemements

    def visitBlockStmt(self, block_stmt: BlockStmt, inspector: Inspector):
        inspector.push_scope()
        for i in range(len(block_stmt.body)):
            if type_of(inspector.get_latest_marker().owner) is FuncDecl:
                name = inspector.get_latest_marker().owner
                if type_of(block_stmt.body[i]) is CallStmt:
                    if i != 0:
                        if block_stmt.body[i].name == 'super' or block_stmt.body[i].name == 'preventDefault':
                            raise InvalidStatementInFunction(name)
                    if block_stmt.body[i].name == 'super' or block_stmt.body[i].name == 'preventDefault':
                        if i != 0:
                            raise InvalidStatementInFunction(name)
            self.visit(block_stmt.body[i], inspector)
        inspector.pop_scope()

    def visitAssignStmt(self, assign_stmt: AssignStmt, inspector: Inspector):
        # 3.5 Type Mismatch In Statement
        # LHS can be in any type except void and array
        lhs = self.visit(assign_stmt.lhs, inspector)
        rhs = self.visit(assign_stmt.rhs, inspector)

        # If LHS is not an identifier or array subscripting expr
        if type_of(lhs) not in [VarDecl, ParamDecl]:
            raise TypeMismatchInStatement(assign_stmt)

        # LHS can't be of type void or array
        if type_of(get_type(lhs)) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(assign_stmt)

        # Can't infer type: won't happen
        self.infer(lhs, rhs, TypeMismatchInStatement(assign_stmt))

        return assign_stmt

    def visitIfStmt(self, if_stmt: IfStmt, inspector: Inspector):
        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean

        cond = self.visit(if_stmt.cond, inspector)
        self.infer(cond, BooleanType(), TypeMismatchInStatement(if_stmt))

        self.visit(if_stmt.tstmt, inspector)
        if if_stmt.fstmt is not None:
            self.visit(if_stmt.fstmt, inspector)

    def visitForStmt(self, for_stmt: ForStmt, inspector: Inspector):
        inspector.push_scope(for_stmt)

        # 3.5 Type Mismatch In Statement

        # The type of the scalar variable must be integer
        if type_of(for_stmt.init) is not AssignStmt:
            raise TypeMismatchInStatement(for_stmt)

        init = self.visit(for_stmt.init, inspector)

        scalar = inspector.find_latest_name(init.lhs.name)
        if type_of(get_type(scalar)) is not IntegerType:
            raise TypeMismatchInStatement(for_stmt)

        # The type of the cond expression must be boolean
        cond = self.visit(for_stmt.cond, inspector)
        if type_of(cond) is not BooleanType:
            raise TypeMismatchInStatement(for_stmt)

        # The type of the update expression must be integer
        upd = self.visit(for_stmt.upd, inspector)
        if type_of(upd) is not IntegerType:
            raise TypeMismatchInStatement(for_stmt)

        self.visit(for_stmt.stmt, inspector)

        inspector.pop_scope(for_stmt)

    def visitWhileStmt(self, while_stmt: WhileStmt, inspector: Inspector):
        inspector.push_scope(while_stmt)

        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean
        cond = self.visit(while_stmt.cond, inspector)
        self.infer(cond, BooleanType(), TypeMismatchInStatement(while_stmt))

        self.visit(while_stmt.stmt, inspector)

        inspector.pop_scope(while_stmt)

    def visitDoWhileStmt(self, do_while_stmt: DoWhileStmt, inspector: Inspector):
        inspector.push_scope(do_while_stmt)

        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean
        cond = self.visit(do_while_stmt.cond, inspector)
        self.infer(cond, BooleanType(), TypeMismatchInStatement(do_while_stmt))

        self.visit(do_while_stmt.stmt, inspector)

        inspector.pop_scope(do_while_stmt)

    def visitBreakStmt(self, break_stmt: BreakStmt, inspector: Inspector):
        # 3.6 Break/Continue not in loop
        if not inspector.is_marker_in_scope([ForStmt, WhileStmt, DoWhileStmt]):
            raise MustInLoop(break_stmt)

    def visitContinueStmt(self, continue_stmt: ContinueStmt, inspector: Inspector):
        # 3.6 Break/Continue not in loop
        if not inspector.is_marker_in_scope([ForStmt, WhileStmt, DoWhileStmt]):
            raise MustInLoop(continue_stmt)

    def visitReturnStmt(self, return_stmt: ReturnStmt, inspector: Inspector):
        if return_stmt.expr is None:
            return

        if len(inspector.func_call_stack) > 0:
            func_decl = inspector.func_call_stack[-1]
        else:
            func_decl = inspector.get_latest_marker(FuncDecl).owner

        expr = self.visit(return_stmt.expr, inspector)

        self.infer(func_decl, expr, TypeMismatchInStatement(return_stmt))
        return return_stmt

    def visitCallStmt(self, call_stmt: CallStmt, inspector: Inspector):
        return self.call_func(call_stmt.name, call_stmt.args, inspector, TypeMismatchInStatement(call_stmt))

    # endregion

    # region Expressions

    def visitBinExpr(self, bin_expr: BinExpr, inspector: Inspector):
        if type_of(bin_expr.left) is FuncCall:
            left = bin_expr.left
            left_type = get_type(inspector.find_latest_name_of_type(bin_expr.left.name, [FuncDecl], Undeclared(Function(), bin_expr.left.name)))
        else:
            left = self.visit(bin_expr.left, inspector)
            left_type = get_type(left)

        if type_of(bin_expr.left) is FuncCall:
            right = bin_expr.right
            right_type = get_type(inspector.find_latest_name_of_type(bin_expr.right.name, [FuncDecl], Undeclared(Function(), bin_expr.right.name)))
        else:
            right = self.visit(bin_expr.right, inspector)
            right_type = get_type(right)

        return_type = None

        if bin_expr.op in ['+', '-', '*', '/']:
            if type_of(left_type) not in [IntegerType, FloatType, AutoType] or type_of(right_type) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(bin_expr)

            # Uncertain
            if type_of(left_type) is AutoType and type_of(right_type) is AutoType:
                if type_of(inspector.lhs_type) in [FloatType, IntegerType, AutoType]:
                    self.infer(inspector.lhs_type, left, TypeMismatchInExpression(bin_expr))
                    self.infer(inspector.lhs_type, right, TypeMismatchInExpression(bin_expr))
                    inspector.possible_types = [FloatType, IntegerType, AutoType]
                    return_type = inspector.lhs_type
                else:
                    raise inspector.lhs_exception

            elif type_of(right_type) is AutoType:
                self.infer(left, right, TypeMismatchInExpression(bin_expr))
                return_type = left_type
            elif type_of(left_type) is AutoType:
                self.infer(right, left, TypeMismatchInExpression(bin_expr))
                return_type = right_type
            elif type_of(left_type) is IntegerType and type_of(right_type) is IntegerType:
                return_type = IntegerType()
            else:
                return_type = FloatType()
        if bin_expr.op == '%':
            self.infer(IntegerType(), left, TypeMismatchInExpression(bin_expr))
            self.infer(IntegerType(), right, TypeMismatchInExpression(bin_expr))
            return_type = IntegerType()
        if bin_expr.op in ['&&', '||']:
            self.infer(BooleanType(), left, TypeMismatchInExpression(bin_expr))
            self.infer(BooleanType(), right, TypeMismatchInExpression(bin_expr))
            return_type = BooleanType()
        if bin_expr.op == '::':
            self.infer(StringType(), left, TypeMismatchInExpression(bin_expr))
            self.infer(StringType(), right, TypeMismatchInExpression(bin_expr))
            return_type = StringType()
        if bin_expr.op in ['==', '!=']:
            if IntegerType in [type_of(left_type), type_of(right_type)]:
                self.infer(IntegerType(), left, TypeMismatchInExpression(bin_expr))
                self.infer(IntegerType(), right, TypeMismatchInExpression(bin_expr))
            if BooleanType in [type_of(left_type), type_of(right_type)]:
                self.infer(BooleanType(), left, TypeMismatchInExpression(bin_expr))
                self.infer(BooleanType(), right, TypeMismatchInExpression(bin_expr))
            return_type = BooleanType()
        if bin_expr.op in ['<', '>', '<=', '>=']:
            if type_of(left_type) not in [IntegerType, FloatType, AutoType] or type_of(right_type) not in [IntegerType, FloatType, AutoType]:
                raise TypeMismatchInExpression(bin_expr)
            if FloatType in [type_of(left_type), type_of(right_type)]:
                self.infer(FloatType(), left, TypeMismatchInExpression(bin_expr))
                self.infer(FloatType(), right, TypeMismatchInExpression(bin_expr))
            else:
                self.infer(IntegerType(), left, TypeMismatchInExpression(bin_expr))
                self.infer(IntegerType(), right, TypeMismatchInExpression(bin_expr))
            return_type = BooleanType()

        inspector.func_return_type = left_type
        if type_of(bin_expr.left) is FuncCall:
            self.visit(bin_expr.left, inspector)

        inspector.func_return_type = right_type
        if type_of(bin_expr.right) is FuncCall:
            self.visit(bin_expr.right, inspector)

        inspector.func_return_type = None

        return return_type

    def visitUnExpr(self, un_expr: UnExpr, inspector: Inspector):
        val = self.visit(un_expr.val, inspector)
        val_type = type_of(get_type(val))

        if un_expr.op == '-':
            if val_type is AutoType:
                if type_of(inspector.lhs_type) in [FloatType, IntegerType, AutoType]:
                    self.infer(inspector.lhs_type, val, TypeMismatchInExpression(un_expr))
                    inspector.possible_types = [FloatType, IntegerType, AutoType]
                    return inspector.lhs_type
                else:
                    raise inspector.lhs_exception
            elif val_type not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(un_expr)
            else:
                return val_type
        if un_expr.op == '!':
            self.infer(BooleanType(), val, TypeMismatchInExpression(un_expr))
            return BooleanType()

    def visitId(self, id: Id, inspector: Inspector):
        # 3.2 Undeclared Identifier
        inspector.check_undeclared(id, Identifier())

        id_decl = inspector.find_latest_name(id.name)
        if type_of(id_decl) is FuncDecl:
            raise Undeclared(Identifier(), id.name)

        return id_decl

    def visitArrayCell(self, array_cell: ArrayCell, inspector: Inspector):
        # 3.4 Type Mismatch In Expression

        # Name not found
        inspector.check_undeclared(array_cell, Identifier())

        array_decl = inspector.find_latest_name(array_cell.name)

        # Type is not ArrayType
        if type_of(array_decl) is not VarDecl or type_of(get_type(array_decl)) is not ArrayType:
            raise TypeMismatchInExpression(array_cell)

        # Any subscript is not an integer
        for expr in array_cell.cell:
            self.infer(IntegerType(), self.visit(expr, inspector), TypeMismatchInExpression(expr))

        if len(array_cell.cell) == len(array_decl.typ.dimensions):
            return array_decl.typ.typ
        elif len(array_cell.cell) > len(array_decl.typ.dimensions):
            raise TypeMismatchInExpression(array_cell)
        else:
            return ArrayType(array_decl.typ.dimensions[len(array_cell.cell):], array_decl.typ.typ)

    def visitIntegerLit(self, integer_lit: IntegerLit, inspector: Inspector):
        return IntegerType()

    def visitFloatLit(self, float_lit: FloatLit, inspector: Inspector):
        return FloatType()

    def visitStringLit(self, string_lit: StringLit, inspector: Inspector):
        return StringType()

    def visitBooleanLit(self, boolean_lit: BooleanLit, inspector: Inspector):
        return BooleanType()

    def visitArrayLit(self, array_lit: ArrayLit, inspector: Inspector):
        auto_variables = []
        first_concrete_type = None

        try:
            for exp in array_lit.explist:
                exp_visited = self.visit(exp, inspector)
                exp_type = get_type(exp_visited)
                if type_of(exp_type) is AutoType:
                    auto_variables.append(exp_visited)
                else:
                    if first_concrete_type is None:
                        first_concrete_type = exp_type
                    elif not is_same_type(first_concrete_type, exp_type):
                        raise IllegalArrayLiteral(array_lit)
        except:
            raise IllegalArrayLiteral(array_lit)

        # If all elements in the array literal is of AutoType
        if first_concrete_type is None:
            raise IllegalArrayLiteral(array_lit)

        # If there's at least one concrete type, infer the AutoType variables
        for var in auto_variables:
            self.infer(var, first_concrete_type, TypeMismatchInExpression(array_lit))

        if type_of(first_concrete_type) is ArrayType:
            return ArrayType([len(array_lit.explist)] + first_concrete_type.dimensions, first_concrete_type.typ)
        else:
            return ArrayType([len(array_lit.explist)], first_concrete_type)

    def visitFuncCall(self, func_call: FuncCall, inspector: Inspector):
        return self.call_func(func_call.name, func_call.args, inspector, TypeMismatchInExpression(func_call), inspector.func_return_type)

    # endregion

    # region Types

    def visitIntegerType(self, integer_type: IntegerType, inspector: Inspector):
        return integer_type

    def visitFloatType(self, float_type: FloatType, inspector: Inspector):
        return float_type

    def visitBooleanType(self, boolean_type: BooleanType, inspector: Inspector):
        return boolean_type

    def visitStringType(self, string_type: StringType, inspector: Inspector):
        return string_type

    def visitArrayType(self, array_type: ArrayType, inspector: Inspector):
        return array_type

    def visitAutoType(self, auto_type: AutoType, inspector: Inspector):
        return auto_type

    def visitVoidType(self, void_type: VoidType, inspector: Inspector):
        return void_type

    # endregion
