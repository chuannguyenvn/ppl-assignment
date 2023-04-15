from Visitor import Visitor
from MT22Parser import MT22Parser
from AST import *
from StaticError import *


class ScopeUnit:
    def __init__(self):
        self.scope_elements = []

    def add(self, o):
        self.scope_elements += [o]

    def remove(self, o):
        self.scope_elements -= [o]

    def contains(self, o):
        return o in self.scope_elements


class Scope:
    def __init__(self):
        self.scope_stack: List[ScopeUnit] = []

    def add_symbol(self, o):
        self.scope_stack[-1].add(o)

    def remove_symbol(self, o):
        self.scope_stack[-1].remove(o)

    def push_scope(self):
        self.scope_stack += [ScopeUnit()]

    def pop_scope(self):
        self.scope_stack = self.scope_stack[:-1]

    def closest_scope_contains_exact(self, o):
        return self.scope_stack[-1].contains(o)

    def closest_scope_contains_name(self, o):
        return o in map(lambda scope_unit: scope_unit.name, self.scope_stack[-1].scope_elements)

    def any_scope_contains_exact(self, o):
        for scope in self.scope_stack:
            if scope.contains(o):
                return True

    def any_scope_contains_name(self, o):
        for scope in self.scope_stack:
            if o in map(lambda scope_unit: scope_unit.name, scope.scope_elements)
                return True

        return False


class Utils:
    @staticmethod
    def check_redeclared(symbol, scope: Scope):
        return scope.closest_scope_contains_name(symbol)

    @staticmethod
    def check_undeclared(symbol, scope: Scope):
        return not scope.any_scope_contains_name(symbol)


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.visitProgram(ast)

    def visitProgram(self, program: Program):
        self.visit(program.decls, Scope())

    # region Declarations

    def visitVarDecl(self, var_decl: VarDecl, scope: Scope):
        if Utils.check_redeclared(var_decl, scope):
            raise Redeclared(Variable(), var_decl.name)
        if var_decl.typ == AutoType() and var_decl.init == None:
            raise Invalid(Variable(), var_decl.name)

        scope.add_symbol(var_decl)
        return var_decl

    def visitParamDecl(self, param_decl: ParamDecl, scope: Scope):
        if Utils.check_redeclared(param_decl, scope):
            raise Redeclared(Parameter(), param_decl.name)
        
        # TODO: Invalid

    def visitFuncDecl(self, func_decl: FuncDecl, scope: Scope):
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

    def visitBlockStmt(self, block_stmt: BlockStmt, scope: Scope):
        pass

    def visitAssignStmt(self, assign_stmt: AssignStmt, scope: Scope):
        pass

    def visitIfStmt(self, if_stmt: IfStmt, scope: Scope):
        pass

    def visitForStmt(self, for_stmt: ForStmt, scope: Scope):
        pass

    def visitWhileStmt(self, while_stmt: WhileStmt, scope: Scope):
        pass

    def visitDoWhileStmt(self, do_while_stmt: DoWhileStmt, scope: Scope):
        pass

    def visitBreakStmt(self, break_stmt: BreakStmt, scope: Scope):
        pass

    def visitContinueStmt(self, continue_stmt: ContinueStmt, scope: Scope):
        pass

    def visitReturnStmt(self, return_stmt: ReturnStmt, scope: Scope):
        pass

    def visitCallStmt(self, call_stmt: CallStmt, scope: Scope):
        pass

    # endregion

    # region Expressions
    def visitBinExpr(self, bin_expr: BinExpr, scope: Scope):
        pass

    def visitUnExpr(self, un_expr: UnExpr, scope: Scope):
        pass

    def visitId(self, id: Id, scope: Scope):
        pass

    def visitArrayCell(self, array_cell: ArrayCell, scope: Scope):
        pass

    def visitIntegerLit(self, integer_lit: IntegerLit, scope: Scope):
        pass

    def visitFloatLit(self, float_lit: FloatLit, scope: Scope):
        pass

    def visitStringLit(self, string_lit: StringLit, scope: Scope):
        pass

    def visitBooleanLit(self, boolean_lit: BooleanLit, scope: Scope):
        pass

    def visitArrayLit(self, array_lit: ArrayLit, scope: Scope):
        pass

    def visitFuncCall(self, func_call: FuncCall, scope: Scope):
        pass

    # endregion

    # region Types
    def visitIntegerType(self, integer_type: IntegerType, scope: Scope):
        pass

    def visitFloatType(self, float_type: FloatType, scope: Scope):
        pass

    def visitBooleanType(self, boolean_type: BooleanType, scope: Scope):
        pass

    def visitStringType(self, string_type: StringType, scope: Scope):
        pass

    def visitArrayType(self, array_type: ArrayType, scope: Scope):
        pass

    def visitAutoType(self, auto_type: AutoType, scope: Scope):
        pass

    def visitVoidType(self, void_type: VoidType, scope: Scope):
        pass

    # endregion
