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

    def closest_scope_contains_exact(self, o):
        for i in reversed(range(len(self.stack))):
            if self.stack[i] == o:
                return True
            if self.stack[i] is ScopeDivider():
                return False

    def closest_scope_contains_name(self, o):
        for i in reversed(range(len(self.stack))):
            if self.stack[i].name == o.name:
                return True
            if self.stack[i] is ScopeDivider():
                return False

    def any_scope_contains_exact(self, o):
        return o in self.stack

    def any_scope_contains_name(self, o):
        for element in self.stack:
            if o.name == element.name:
                return True
        return False


class Utils:
    @staticmethod
    def check_redeclared(symbol, scope: ScopeStack):
        return scope.closest_scope_contains_name(symbol)

    @staticmethod
    def check_undeclared(symbol, scope: ScopeStack):
        return not scope.any_scope_contains_name(symbol)


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.visitProgram(ast)

    def visitProgram(self, program: Program):
        global_scope = ScopeStack()
        for decl in program.decls:
            self.visit(decl, global_scope)

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, scope: ScopeStack):
        if Utils.check_redeclared(var_decl, scope):
            raise Redeclared(Variable(), var_decl.name)
        if var_decl.typ == AutoType() and var_decl.init is None:
            raise Invalid(Variable(), var_decl.name)

        scope.add_symbol(var_decl)
        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, scope: ScopeStack):
        if Utils.check_redeclared(param_decl, scope):
            raise Redeclared(Parameter(), param_decl.name)

        # TODO: Invalid

    def visitFuncDecl(self, func_decl: FuncDecl, scope: ScopeStack):
        if Utils.check_redeclared(func_decl, scope):
            raise Redeclared(Function(), func_decl.name)

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
            self.visit(line)

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
        pass

    def visitArrayCell(self, array_cell: ArrayCell, scope: ScopeStack):
        pass

    def visitIntegerLit(self, integer_lit: IntegerLit, scope: ScopeStack):
        pass

    def visitFloatLit(self, float_lit: FloatLit, scope: ScopeStack):
        pass

    def visitStringLit(self, string_lit: StringLit, scope: ScopeStack):
        pass

    def visitBooleanLit(self, boolean_lit: BooleanLit, scope: ScopeStack):
        pass

    def visitArrayLit(self, array_lit: ArrayLit, scope: ScopeStack):
        pass

    def visitFuncCall(self, func_call: FuncCall, scope: ScopeStack):
        pass

    # endregion

    # region Types
    def visitIntegerType(self, integer_type: IntegerType, scope: ScopeStack):
        pass

    def visitFloatType(self, float_type: FloatType, scope: ScopeStack):
        pass

    def visitBooleanType(self, boolean_type: BooleanType, scope: ScopeStack):
        pass

    def visitStringType(self, string_type: StringType, scope: ScopeStack):
        pass

    def visitArrayType(self, array_type: ArrayType, scope: ScopeStack):
        pass

    def visitAutoType(self, auto_type: AutoType, scope: ScopeStack):
        pass

    def visitVoidType(self, void_type: VoidType, scope: ScopeStack):
        pass

    # endregion
