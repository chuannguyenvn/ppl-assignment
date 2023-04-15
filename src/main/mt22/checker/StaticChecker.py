from Visitor import Visitor
from MT22Parser import MT22Parser
from AST import *
from StaticError import *


class ScopeDivider:
    pass


class ScopeStack:

    def __init__(self):
        self.stack = []

    def add_symbol(self, o):
        self.stack.append(o)

    def remove_symbol(self, o):
        self.stack.remove(o)

    def push_scope(self):
        self.stack.append(ScopeDivider())

    def pop_scope(self):
        for i in range(len(self.stack)):
            element = self.stack.pop()
            if element is ScopeDivider():
                return

    def find_latest_name(self, name):
        for i in reversed(range(len(self.stack))):
            if type(self.stack[i]) is ScopeDivider:
                continue
            if self.stack[i].name == name:
                return self.stack[i].name
        return None

    def latest_scope_contains_exact(self, o):
        for i in reversed(range(len(self.stack))):
            if type(self.stack[i]) is ScopeDivider:
                continue
            if self.stack[i] == o:
                return True
            if self.stack[i] is ScopeDivider():
                return False

    def latest_scope_contains_name(self, o):
        for i in reversed(range(len(self.stack))):
            if type(self.stack[i]) is ScopeDivider:
                continue
            if self.stack[i].name == o.name:
                return True
            if self.stack[i] is ScopeDivider():
                return False

    def any_scope_contains_exact(self, o):
        return o in self.stack

    def any_scope_contains_name(self, o):
        return self.find_latest_name(o) is not None


def check_redeclared(symbol, typ, scope):
    if scope.latest_scope_contains_name(symbol):
        raise Redeclared(typ, symbol.name)


def check_undeclared(symbol, typ, scope):
    if not scope.any_scope_contains_name(symbol):
        raise Undeclared(typ, symbol.name)


def check_invalid(symbol, typ, scope):
    if type(typ) is Variable:
        print("Yo")
        if type(symbol.typ) is AutoType and symbol.init is None:
            raise Invalid(Variable(), symbol.name)


def check_type_mismatch_in_expression(expression, typ, scope):
    pass


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, ScopeStack())

    def visitProgram(self, program: Program, scope: ScopeStack):
        return [self.visit(decl, scope) for decl in program.decls]

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, scope: ScopeStack):
        # 3.1 Redeclared Variable
        check_redeclared(var_decl, Variable(), scope)

        # 3.3 Invalid Variable
        check_invalid(var_decl, Variable(), scope)

        scope.add_symbol(var_decl)
        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, scope: ScopeStack):
        # 3.1 Redeclared Parameter
        check_redeclared(param_decl, Parameter(), scope)

        # 3.3 Invalid Parameter
        # TODO: Invalid

    def visitFuncDecl(self, func_decl: FuncDecl, scope: ScopeStack):
        check_redeclared(func_decl, Function(), scope)

        scope.push_scope()
        scope.add_symbol(func_decl)

        for param in func_decl.params:
            self.visit(param, scope)
            scope.add_symbol(param)

        self.visit(func_decl.body, scope)
        scope.pop_scope()

    # endregion

    # region Statemements

    def visitBlockStmt(self, block_stmt: BlockStmt, scope: ScopeStack):
        scope.push_scope()
        for line in block_stmt.body:
            self.visit(line, scope)

    def visitAssignStmt(self, assign_stmt: AssignStmt, scope: ScopeStack):
        pass

    def visitIfStmt(self, if_stmt: IfStmt, scope: ScopeStack):
        pass

    def visitForStmt(self, for_stmt: ForStmt, scope: ScopeStack):
        pass

    def visitWhileStmt(self, while_stmt: WhileStmt, scope: ScopeStack):
        pass

    def visitDoWhileStmt(self, do_while_stmt: DoWhileStmt, scope: ScopeStack):
        pass

    def visitBreakStmt(self, break_stmt: BreakStmt, scope: ScopeStack):
        pass

    def visitContinueStmt(self, continue_stmt: ContinueStmt, scope: ScopeStack):
        pass

    def visitReturnStmt(self, return_stmt: ReturnStmt, scope: ScopeStack):
        pass

    def visitCallStmt(self, call_stmt: CallStmt, scope: ScopeStack):
        pass

    # endregion

    # region Expressions
    def visitBinExpr(self, bin_expr: BinExpr, scope: ScopeStack):
        pass

    def visitUnExpr(self, un_expr: UnExpr, scope: ScopeStack):
        pass

    def visitId(self, id: Id, scope: ScopeStack):
        # 3.2 Undeclared Identifier
        check_undeclared(id, Identifier(), scope)

    def visitArrayCell(self, array_cell: ArrayCell, scope: ScopeStack):
        # 3.4 Type Mismatch In Expression

        # Name not found
        check_undeclared(array_cell)

        # Type is not ArrayType
        if type(scope.find_latest_name(array_cell.name)) is not ArrayType:
            raise TypeMismatchInExpression(array_cell)

        # Any subscript is not an integer
        for expr in array_cell.cell:
            if type(self.visit(expr, scope)) is not IntegerType:
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
        pass

    def visitFuncCall(self, func_call: FuncCall, scope: ScopeStack):
        pass

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
