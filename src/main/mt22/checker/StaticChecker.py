from Visitor import Visitor
from MT22Parser import MT22Parser
from AST import *
from StaticError import *


def type_of(typ):
    if type(typ) is type(type):
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


def check_redeclared(symbol, typ, scope):
    if scope.latest_scope_contains_name(symbol):
        raise Redeclared(typ, symbol.name)


def check_undeclared(symbol, typ, scope):
    if not scope.any_scope_contains_name(symbol):
        raise Undeclared(typ, symbol.name)


def check_invalid(symbol, typ, scope):
    if type_of(typ) is Variable:
        print("Yo")
        if type_of(symbol.typ) is AutoType and symbol.init is None:
            raise Invalid(Variable(), symbol.name)


def try_infer(symbol, typ, exception, scope):
    if type_of(symbol) is AutoType:
        scope.find_latest_name(symbol.name).typ = typ
    elif type_of(symbol) is not typ:
        raise exception


def infer(symbol, typ, scope):
    scope.find_latest_name(symbol.name).typ = typ


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

        return decls

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, scope: ScopeStack):
        # 3.1 Redeclared Variable
        check_redeclared(var_decl, Variable(), scope)

        # 3.3 Invalid Variable
        check_invalid(var_decl, Variable(), scope)

        if var_decl.init is not None:
            self.visit(var_decl.init, scope)

        scope.add_symbol(var_decl)

        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, scope: ScopeStack):
        # 3.1 Redeclared Parameter
        check_redeclared(param_decl, Parameter(), scope)

        # 3.3 Invalid Parameter
        # TODO: Invalid

    def visitFuncDecl(self, func_decl: FuncDecl, scope: ScopeStack):
        check_redeclared(func_decl, Function(), scope)

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

        # If LHS is not an identifier or array subscripting expr
        if not isinstance(lhs, LHS):
            raise TypeMismatchInStatement(assign_stmt)

        if type_of(lhs.typ) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(assign_stmt)

    def visitIfStmt(self, if_stmt: IfStmt, scope: ScopeStack):
        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean

        try_infer(if_stmt.cond, BooleanType, TypeMismatchInStatement(if_stmt), scope)

        self.visit(if_stmt.tstmt, scope)
        self.visit(if_stmt.fstmt, scope)

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
        if type_of(cond) is not BooleanType:
            raise TypeMismatchInStatement(while_stmt)

        self.visit(while_stmt.stmt, scope)

        scope.pop_scope(while_stmt)

    def visitDoWhileStmt(self, do_while_stmt: DoWhileStmt, scope: ScopeStack):
        scope.push_scope(do_while_stmt)

        # 3.5 Type Mismatch In Statement
        # Conditional expression must be boolean
        if type_of(do_while_stmt.cond) is not BooleanType:
            raise TypeMismatchInStatement(do_while_stmt)

        self.visit(do_while_stmt.tstmt, scope)

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
        left = self.visit(bin_expr.left)
        right = self.visit(bin_expr.right)

        if bin_expr.op in ['+', '-', '*', '/']:
            if type_of(left) not in [IntegerType, FloatType] or type_of(right) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(bin_expr)
            if FloatType in [type_of(left), type_of(right)]:
                return FloatType()
            else:
                return IntegerType()
        if bin_expr.op is '%':
            if type_of(left) is not IntegerType or type_of(right) is not IntegerType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return IntegerType()
        if bin_expr.op in ['&&', '||']:
            if type_of(left) is not BooleanType or type_of(right) is not BooleanType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()
        if bin_expr.op is '::':
            if type_of(left) is not StringType or type_of(right) is not StringType:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return StringType()
        if bin_expr.op in ['==', '!=']:
            if type_of(left) not in [IntegerType, BooleanType] or type_of(right) not in [IntegerType, BooleanType] or type_of(left) != type_of(right):
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()
        if bin_expr.op in ['<', '>', '<=', '>=']:
            if type_of(left) not in [IntegerType, FloatType] or type_of(right) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(bin_expr)
            else:
                return BooleanType()

    def visitUnExpr(self, un_expr: UnExpr, scope: ScopeStack):
        val = self.visit(un_expr.val, scope)

        if un_expr.op is '-':
            if type_of(val) not in [IntegerType, FloatType]:
                raise TypeMismatchInExpression(un_expr)
            else:
                if type_of(val) is FloatType:
                    return FloatType()
                else:
                    return IntegerType()
        if un_expr.op is '!':
            if type_of(val) is not BooleanType:
                raise TypeMismatchInExpression(un_expr)
            else:
                return BooleanType()
        # TODO: indexing expression

    def visitId(self, id: Id, scope: ScopeStack):
        # 3.2 Undeclared Identifier
        check_undeclared(id, Identifier(), scope)

    def visitArrayCell(self, array_cell: ArrayCell, scope: ScopeStack):
        # 3.4 Type Mismatch In Expression

        # Name not found
        check_undeclared(array_cell)

        # Type is not ArrayType
        if type_of(scope.find_latest_name(array_cell.name)) is not ArrayType:
            raise TypeMismatchInExpression(array_cell)

        # Any subscript is not an integer
        for expr in array_cell.cell:
            if type_of(self.visit(expr, scope)) is not IntegerType:
                raise TypeMismatchInExpression(array_cell)

        # Dimension not matched
        # TODO

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
                elif first_concrete_type is not type_of(exp_type):
                    raise TypeMismatchInExpression(array_lit)

        # If all elements in the array literal is of AutoType
        if first_concrete_type is None:
            raise TypeMismatchInExpression(array_lit)

        # If there's at least one concrete type, infer the AutoType variables
        for var in auto_variables:
            infer(var, first_concrete_type, scope)

    def visitFuncCall(self, func_call: FuncCall, scope: ScopeStack):
        # 3.4 Type Mismatch In Expression
        func_decl = scope.find_latest_name(func_call.name)

        # Return type must not be void
        if type_of(func_decl.return_type) is VoidType:
            raise TypeMismatchInExpression(func_call)

        # Parameters must match
        if len(func_decl.params) != len(func_call.args):
            raise TypeMismatchInExpression(func_call)

        for i in range(len(func_decl.params)):
            arg = self.visit(func_call.args[i], scope)
            if type_of(arg) is not type_of(func_decl.params[i].typ):
                raise TypeMismatchInExpression(func_call)

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
