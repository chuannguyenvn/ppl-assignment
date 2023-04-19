from Visitor import Visitor
from AST import *
from StaticError import *


def type_of(typ):
    if type(typ) is type(AST):
        return typ
    else:
        return type(typ)


class Marker:
    pass


class ScopeMarker(Marker):
    def __init__(self, typ=None):
        self.typ = typ


class ScopeStack:

    def __init__(self):
        self.stack = [ScopeMarker()]

    def add(self, o):
        self.stack.append(o)

    def add_symbol(self, o):
        self.stack.append(o)

    def remove(self, o):
        self.stack.remove(o)

    def remove_symbol(self, o):
        self.stack.remove(o)

    def push_scope(self, typ=None):
        if typ is None:
            self.stack.append(ScopeMarker())
        else:
            self.stack.append(ScopeMarker(type(typ)))

    def pop_scope(self, typ=None):
        for i in reversed(range(len(self.stack))):
            element = self.stack.pop()
            if typ is None:
                if type_of(element) is ScopeMarker:
                    return
            else:
                if type_of(element) is ScopeMarker and element.typ is type_of(typ):
                    return

    def find_latest_name(self, name):
        for i in reversed(range(len(self.stack))):
            if type_of(self.stack[i]) not in [VarDecl, ParamDecl, FuncDecl]:
                continue
            if self.stack[i].name == name:
                return self.stack[i]
        return None

    def latest_scope_contains_exact(self, o):
        for i in reversed(range(len(self.stack))):
            if type_of(self.stack[i]) is ScopeMarker:
                return False
            if self.stack[i] == o:
                return True

    def latest_scope_contains_name(self, o):
        for i in reversed(range(len(self.stack))):
            if type_of(self.stack[i]) is ScopeMarker:
                return False
            if self.stack[i].name == o.name:
                return True

    def any_scope_contains_exact(self, o):
        return o in self.stack

    def any_scope_contains_name(self, o):
        return self.find_latest_name(o) is not None

    def is_marker_in_scope(self, marker_types):
        for i in range(len(self.stack)):
            if type_of(self.stack[i]) is ScopeMarker and self.stack[i].typ in marker_types:
                return True

        return False

    def try_infer(self, symbol, typ, exception):
        if type_of(symbol) in [VarDecl, ParamDecl]:
            decl = self.find_latest_name(symbol.name)
            if type_of(decl.typ) is AutoType:
                decl.typ = typ
            elif type_of(decl.typ) != type_of(typ):
                raise exception
        elif type_of(symbol) is FuncDecl:
            func_decl = self.find_latest_name(symbol.name)
            if type_of(func_decl.return_type) is AutoType:
                func_decl.return_type = typ
            elif type_of(func_decl.return_type) != type_of(typ):
                raise exception
        else:
            if type_of(symbol) is not typ:
                raise exception

    def try_two_way_infer(self, lhs, rhs, exception):
        decl = self.find_latest_name(lhs.name)
        if type_of(decl.typ) is AutoType:
            decl.typ = typ
        elif type_of(decl.typ) is not typ:
            raise exception

    def try_infer_func_return(self, symbol, typ, exception):
        func_decl = self.find_latest_name(symbol.name)

        if type_of(symbol.return_type) not in [AutoType, return_type]:
            raise exception

        func_decl.return_type = typ

    def try_infer_func_params(self, symbol, param_types, exception):
        if len(symbol.params) != len(param_types):
            raise exception

        for i in range(len(param_types)):
            self.try_infer(symbol.params[i], param_types[i], exception)

    def check_redeclared(self, symbol, typ):
        if self.latest_scope_contains_name(symbol):
            raise Redeclared(typ, symbol.name)

    def check_undeclared(self, symbol, typ):
        if not self.any_scope_contains_name(symbol.name):
            raise Undeclared(typ, symbol.name)

    def check_invalid(self, symbol, typ):
        if type_of(typ) is Variable:
            if type_of(symbol.typ) is AutoType and symbol.init is None:
                raise Invalid(Variable(), symbol.name)

    def infer(self, symbol, typ):
        self.find_latest_name(symbol.name).typ = typ

    def deduct_type(self, symbol):
        if type_of(symbol) in [VarDecl, ParamDecl]:
            return symbol.typ
        if type_of(symbol) is FuncDecl:
            return symbol.return_type

        return symbol


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, ScopeStack())

    def visitProgram(self, program: Program, scope: ScopeStack):
        decls = [self.visit(decl, scope) for decl in program.decls]

        # 3.9 No entry point
        main_func = scope.find_latest_name('main')
        if main_func is None or type_of(main_func) is not FuncDecl or type_of(main_func.return_type) is not VoidType or len(main_func.params) != 0:
            raise NoEntryPoint()

        return []

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, scope: ScopeStack):
        # 3.1 Redeclared Variable
        scope.check_redeclared(var_decl, Variable())
        # 3.3 Invalid Variable

        scope.check_invalid(var_decl, Variable())

        if var_decl.init is not None:
            init_type = scope.deduct_type(self.visit(var_decl.init, scope))
            if type_of(var_decl.typ) is AutoType:
                var_decl.typ = init_type
            elif type_of(var_decl.typ) is FloatType and type_of(init_type) is IntegerType:
                pass
            elif type_of(init_type) != type_of(var_decl.typ):
                raise TypeMismatchInVarDecl(var_decl)

        scope.add_symbol(var_decl)

        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, scope: ScopeStack):
        # 3.1 Redeclared Parameter
        scope.check_redeclared(param_decl, Parameter())

        # 3.3 Invalid Parameter
        # TODO: Invalid

    def visitFuncDecl(self, func_decl: FuncDecl, scope: ScopeStack):
        scope.check_redeclared(func_decl, Function())

        scope.add_symbol(func_decl)

        scope.push_scope(func_decl)

        for param in func_decl.params:
            self.visit(param, scope)
            scope.add_symbol(param)

        self.visit(func_decl.body, scope)

        scope.pop_scope(func_decl)

    # endregion

    # region Statemements

    def visitBlockStmt(self, block_stmt: BlockStmt, scope: ScopeStack):
        scope.push_scope()
        for line in block_stmt.body:
            self.visit(line, scope)
        scope.pop_scope()

    def visitAssignStmt(self, assign_stmt: AssignStmt, scope: ScopeStack):
        # 3.5 Type Mismatch In Statement
        # LHS can be in any type except void and array
        lhs = self.visit(assign_stmt.lhs, scope)
        rhs = self.visit(assign_stmt.rhs, scope)

        lhs_decl = lhs
        rhs_decl = rhs if type_of(rhs) in [VarDecl, ParamDecl, FuncDecl] else None
        lhs_type = lhs_decl.typ
        rhs_type = rhs

        if type_of(rhs) in [VarDecl, ParamDecl]:
            rhs_type = rhs_decl.typ
        elif type_of(rhs) is FuncDecl:
            rhs_type = rhs_decl.return_type

        # If LHS is not an identifier or array subscripting expr
        if not isinstance(lhs, LHS):
            raise TypeMismatchInStatement(assign_stmt)

        # LHS can't be of type void or array
        if type_of(lhs_type) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(assign_stmt)

        # Can't infer type: won't happen
        if type_of(lhs_type) is AutoType:
            scope.try_infer(lhs_decl, rhs_type)
        else:
            if type_of(lhs_type) != type_of(rhs_type):
                raise TypeMismatchInStatement(assign_stmt)

    def visitIfStmt(self, if_stmt: IfStmt, scope: ScopeStack):
        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean

        cond = self.visit(if_stmt.cond, scope)
        scope.try_infer(cond, BooleanType, TypeMismatchInStatement(if_stmt))

        self.visit(if_stmt.tstmt, scope)
        if if_stmt.fstmt is not None: self.visit(if_stmt.fstmt, scope)

    def visitForStmt(self, for_stmt: ForStmt, scope: ScopeStack):
        scope.push_scope(for_stmt)

        # 3.5 Type Mismatch In Statement

        # The type of the scalar variable must be integer
        if type_of(for_stmt.init) is not AssignStmt:
            raise TypeMismatchInStatement(for_stmt)

        scalar_name = self.visit(for_stmt.init.lhs, scope).name
        if type_of(scope.find_latest_name(scalar_name).typ) is not IntegerType:
            raise TypeMismatchInStatement(for_stmt)

        self.visit(for_stmt.cond, scope)

        # The type of the update expression must be integer
        if type_of(for_stmt.upd) is not Expr:
            raise TypeMismatchInStatement(for_stmt)

        if type_of(self.visit(for_stmt.upd, scope)) is not IntegerType:
            raise TypeMismatchInStatement(for_stmt)

        self.visit(for_stmt.stmt, scope)

        scope.pop_scope(for_stmt)

    def visitWhileStmt(self, while_stmt: WhileStmt, scope: ScopeStack):
        scope.push_scope(while_stmt)

        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean
        cond = self.visit(while_stmt.cond, scope)
        scope.try_infer(cond, BooleanType, TypeMismatchInStatement(while_stmt))

        self.visit(while_stmt.stmt, scope)

        scope.pop_scope(while_stmt)

    def visitDoWhileStmt(self, do_while_stmt: DoWhileStmt, scope: ScopeStack):
        scope.push_scope(do_while_stmt)

        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean
        cond = self.visit(do_while_stmt.cond, scope)
        scope.try_infer(cond, BooleanType, TypeMismatchInStatement(do_while_stmt))

        self.visit(do_while_stmt.stmt, scope)

        scope.pop_scope(do_while_stmt)

    def visitBreakStmt(self, break_stmt: BreakStmt, scope: ScopeStack):
        # 3.6 Break/Continue not in loop
        if not scope.is_marker_in_scope([ForStmt, WhileStmt, DoWhileStmt]):
            raise MustInLoop(break_stmt)

    def visitContinueStmt(self, continue_stmt: ContinueStmt, scope: ScopeStack):
        # 3.6 Break/Continue not in loop
        if not scope.is_marker_in_scope([ForStmt, WhileStmt, DoWhileStmt]):
            raise MustInLoop(continue_stmt)

    def visitReturnStmt(self, return_stmt: ReturnStmt, scope: ScopeStack):
        pass

    def visitCallStmt(self, call_stmt: CallStmt, scope: ScopeStack):
        pass

    # endregion

    # region Expressions

    def visitBinExpr(self, bin_expr: BinExpr, scope: ScopeStack):
        left_type = type_of(scope.deduct_type(self.visit(bin_expr.left, scope)))
        right_type = type_of(scope.deduct_type(self.visit(bin_expr.right, scope)))

        if bin_expr.op in ['+', '-', '*', '/']:
            if left_type not in [IntegerType, FloatType] or right_type not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(bin_expr)
            if FloatType in [left_type, right_type]:
                return FloatType()
            else:
                return IntegerType()
        if bin_expr.op == '%':
            if left_type is not IntegerType or right_type is not IntegerType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return IntegerType()
        if bin_expr.op in ['&&', '||']:
            if left_type is not BooleanType or right_type is not BooleanType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()
        if bin_expr.op == '::':
            if left_type is not StringType or right_type is not StringType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return StringType()
        if bin_expr.op in ['==', '!=']:
            if left_type not in [IntegerType, BooleanType] or right_type not in [IntegerType, BooleanType] or left_type != right_type:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()
        if bin_expr.op in ['<', '>', '<=', '>=']:
            if left_type not in [IntegerType, FloatType] or right_type not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()

    def visitUnExpr(self, un_expr: UnExpr, scope: ScopeStack):
        val_type = type_of(scope.deduct_type(self.visit(un_expr.val, scope)))

        if un_expr.op == '-':
            if val_type not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(un_expr)
            else:
                if val_type is FloatType:
                    return FloatType()
                else:
                    return IntegerType()
        if un_expr.op == '!':
            if val_type is not BooleanType:
                raise TypeMismatchInExpression(un_expr)
            else:
                return BooleanType()
        # TODO: indexing expression

    def visitId(self, id: Id, scope: ScopeStack):
        # 3.2 Undeclared Identifier
        scope.check_undeclared(id, Identifier())

        id_decl = scope.find_latest_name(id.name)

        return id_decl

    def visitArrayCell(self, array_cell: ArrayCell, scope: ScopeStack):
        # 3.4 Type Mismatch In Expression

        # Name not found
        scope.check_undeclared(array_cell.name, Identifier())

        array_decl = scope.find_latest_name(array_cell.name)

        # Type is not ArrayType
        if type_of(array_decl) is not ArrayType:
            raise TypeMismatchInExpression(array_cell)

        # Any subscript is not an integer
        for expr in array_cell.cell:
            if type_of(self.visit(expr, scope)) is not IntegerType:
                raise TypeMismatchInExpression(array_cell)

        # Dimension not matched
        # TODO

        return array_decl

    def visitIntegerLit(self, integer_lit: IntegerLit, scope: ScopeStack):
        return IntegerType()

    def visitFloatLit(self, float_lit: FloatLit, scope: ScopeStack):
        return FloatType()

    def visitStringLit(self, string_lit: StringLit, scope: ScopeStack):
        return StringType()

    def visitBooleanLit(self, boolean_lit: BooleanLit, scope: ScopeStack):
        return BooleanType()

    def visitArrayLit(self, array_lit: ArrayLit, scope: ScopeStack):
        auto_variables = []
        first_concrete_type = None

        for exp in array_lit.explist:
            exp_type = self.visit(exp, scope)
            if type_of(exp_type) is AutoType:
                auto_variables.append(exp)
            else:
                if first_concrete_type is None:
                    first_concrete_type = exp_type
                elif type_of(first_concrete_type) is not type_of(exp_type):
                    raise TypeMismatchInExpression(array_lit)

        # If all elements in the array literal is of AutoType
        if first_concrete_type is None:
            raise TypeMismatchInExpression(array_lit)

        # If there's at least one concrete type, infer the AutoType variables
        for var in auto_variables:
            scope.infer(var, first_concrete_type)

        if type_of(first_concrete_type) is ArrayType:
            return ArrayType([len(array_lit.explist)] + first_concrete_type.dimensions, first_concrete_type.typ)
        else:
            return ArrayType([len(array_lit.explist)], first_concrete_type)

    def visitFuncCall(self, func_call: FuncCall, scope: ScopeStack):
        # 3.4 Type Mismatch In Expression
        func_decl = scope.find_latest_name(func_call.name)

        # Return type must not be void
        if type_of(func_decl) is not FuncDecl or type_of(func_decl.return_type) is VoidType:
            raise TypeMismatchInExpression(func_call)

        # Parameters must match
        if len(func_decl.params) != len(func_call.args):
            raise TypeMismatchInExpression(func_call)

        arg_types = []
        for i in range(len(func_decl.params)):
            arg_type = self.visit(func_call.args[i], scope)
            if type_of(arg_type) in [VarDecl, Id]:
                arg_type = scope.find_latest_name(arg_type.name).typ
            arg_types.append(arg_type)

        scope.try_infer_func_params(func_decl, arg_types, TypeMismatchInExpression(func_call))

        return func_decl

    # endregion

    # region Types

    def visitIntegerType(self, integer_type: IntegerType, scope: ScopeStack):
        return integer_type

    def visitFloatType(self, float_type: FloatType, scope: ScopeStack):
        return float_type

    def visitBooleanType(self, boolean_type: BooleanType, scope: ScopeStack):
        return boolean_type

    def visitStringType(self, string_type: StringType, scope: ScopeStack):
        return string_type

    def visitArrayType(self, array_type: ArrayType, scope: ScopeStack):
        return array_type

    def visitAutoType(self, auto_type: AutoType, scope: ScopeStack):
        return auto_type

    def visitVoidType(self, void_type: VoidType, scope: ScopeStack):
        return void_type

    # endregion
