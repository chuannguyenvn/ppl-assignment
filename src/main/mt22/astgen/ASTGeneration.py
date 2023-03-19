from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def to_bool(self, b):
        return b == 'true'

    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declaration_list()))

    def visitDeclaration_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.declaration_list_tail():
            return self.visit(ctx.declaration()) + self.visit(ctx.declaration_list_tail())
        else:
            return self.visit(ctx.declaration())

    def visitDeclaration_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.declaration_list_tail():
            return self.visit(ctx.declaration()) + self.visit(ctx.declaration_list_tail())
        else:
            return []

    def visitDeclaration(self, ctx: MT22Parser.ProgramContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        else:
            return self.visit(ctx.function_declaration())

    def visitVariable_declaration(self, ctx: MT22Parser.ProgramContext):
        if ctx.short_variable_declaration():
            return self.visit(ctx.short_variable_declaration())
        else:
            decl_list = self.visit(ctx.long_variable_declaration())
            type = decl_list[len(decl_list) // 2]
            variables = decl_list[:len(decl_list) // 2]
            exprs = decl_list[len(decl_list) // 2 + 1:]
            return [VarDecl(pair[0], type, pair[1]) for pair in list(zip(variables, exprs))]

    def visitShort_variable_declaration(self, ctx: MT22Parser.ProgramContext):
        return [VarDecl(identifier.name, self.visit(ctx.type_specifier())) for identifier in self.visit(ctx.identifier_list())]

    def visitLong_variable_declaration(self, ctx: MT22Parser.ProgramContext):
        if ctx.type_specifier():
            return [ctx.IDENTIFIER().getText(), self.visit(ctx.type_specifier()), self.visit(ctx.expr())]
        else:
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.long_variable_declaration()) + [self.visit(ctx.expr())]

    def visitParameter_declaration_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.parameter_declaration_list_tail():
            return [self.visit(ctx.parameter_declaration())] + self.visit(ctx.parameter_declaration_list_tail())
        else:
            return [self.visit(ctx.parameter_declaration())]

    def visitParameter_declaration_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.parameter_declaration_list_tail():
            return [self.visit(ctx.parameter_declaration())] + self.visit(ctx.parameter_declaration_list_tail())
        else:
            return []

    def visitParameter_declaration(self, ctx: MT22Parser.ProgramContext):
        name = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.type_specifier())
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(name, typ, out, inherit)

    def visitIdentifier_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.identifier_list_tail():
            return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.identifier_list_tail())
        else:
            return [Id(ctx.IDENTIFIER().getText())]

    def visitIdentifier_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.identifier_list_tail():
            return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.identifier_list_tail())
        else:
            return []

    def visitType_specifier(self, ctx: MT22Parser.ProgramContext):
        if ctx.AUTO():
            return AutoType()
        elif ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        else:
            return self.visit(ctx.array_type_specifier())

    def visitArray_type_specifier(self, ctx: MT22Parser.ProgramContext):
        if ctx.INTEGER():
            array_type = IntegerType()
        elif ctx.FLOAT():
            array_type = FloatType()
        elif ctx.BOOLEAN():
            array_type = BooleanType()
        else:
            array_type = StringType()
        return ArrayType(self.visit(ctx.dimension_list()), array_type)

    def visitDimension_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.dimension_list_tail():
            return [int(ctx.INTEGER_LIT().getText())] + self.visit(ctx.dimension_list_tail())
        else:
            return [int(ctx.INTEGER_LIT().getText())]

    def visitDimension_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.dimension_list_tail():
            return [int(ctx.INTEGER_LIT().getText())] + self.visit(ctx.dimension_list_tail())
        else:
            return []

    def visitFunction_declaration(self, ctx: MT22Parser.ProgramContext):
        name = ctx.IDENTIFIER(0).getText()
        return_type = self.visit(ctx.type_specifier()) if ctx.type_specifier() else VoidType()
        params = self.visit(ctx.parameter_declaration_list()) if ctx.parameter_declaration_list() else []
        inherit = ctx.IDENTIFIER(1).getText() if ctx.INHERIT() else None
        body = self.visit(ctx.function_body())
        return [FuncDecl(name, return_type, params, inherit, body)]

    def visitFunction_body(self, ctx: MT22Parser.ProgramContext):
        return self.visit(ctx.block_statement())

    def visitStatement(self, ctx: MT22Parser.ProgramContext):
        if ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.do_while_statement():
            return self.visit(ctx.do_while_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())
        else:
            return self.visit(ctx.block_statement())

    def visitAssignment_statement(self, ctx: MT22Parser.ProgramContext):
        if ctx.IDENTIFIER():
            return AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))
        else:
            return AssignStmt(self.visit(ctx.indexing_expr()), self.visit(ctx.expr()))

    def visitIf_statement(self, ctx: MT22Parser.ProgramContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        else:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement(0)), None)

    def visitFor_statement(self, ctx: MT22Parser.ProgramContext):
        if ctx.IDENTIFIER():
            assign_stmt = AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)))
        else:
            assign_stmt = AssignStmt(self.visit(ctx.indexing_expr()), self.visit(ctx.expr(0)))
        return ForStmt(assign_stmt, self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.statement()))

    def visitWhile_statement(self, ctx: MT22Parser.ProgramContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.statement()))

    def visitDo_while_statement(self, ctx: MT22Parser.ProgramContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_statement()))

    def visitBreak_statement(self, ctx: MT22Parser.ProgramContext):
        return BreakStmt()

    def visitContinue_statement(self, ctx: MT22Parser.ProgramContext):
        return ContinueStmt()

    def visitReturn_statement(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        else:
            return ReturnStmt()

    def visitCall_statement(self, ctx: MT22Parser.ProgramContext):
        f = self.visit(ctx.function_call())
        return CallStmt(f.name, f.args)

    def visitBlock_statement(self, ctx: MT22Parser.ProgramContext):
        return BlockStmt(self.visit(ctx.block_statement_element_list()))

    def visitBlock_statement_element_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.block_statement_element_list_tail())
        elif ctx.variable_declaration():
            return self.visit(ctx.variable_declaration()) + self.visit(ctx.block_statement_element_list_tail())
        else:
            return []

    def visitBlock_statement_element_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.block_statement_element_list_tail())
        elif ctx.variable_declaration():
            return self.visit(ctx.variable_declaration()) + self.visit(ctx.block_statement_element_list_tail())
        else:
            return []

    def visitExpr_list(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr_list_tail():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_list_tail())
        else:
            return [self.visit(ctx.expr())]

    def visitExpr_list_tail(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr_list_tail():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_list_tail())
        else:
            return []

    def visitExpr(self, ctx: MT22Parser.ProgramContext):
        return self.visit(ctx.string_expr())

    def visitString_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.DOUBLE_COLON():
            return BinExpr(ctx.DOUBLE_COLON().getText(), self.visit(ctx.relational_expr(0)),
                           self.visit(ctx.relational_expr(1)))
        else:
            return self.visit(ctx.relational_expr(0))

    def visitRelational_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.EQUAL():
            return BinExpr(ctx.EQUAL().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        elif ctx.NOT_EQUAL():
            return BinExpr(ctx.NOT_EQUAL().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        elif ctx.LESS():
            return BinExpr(ctx.LESS().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        elif ctx.LESS_EQUAL():
            return BinExpr(ctx.LESS_EQUAL().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        elif ctx.GREATER():
            return BinExpr(ctx.GREATER().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        elif ctx.GREATER_EQUAL():
            return BinExpr(ctx.GREATER_EQUAL().getText(), self.visit(ctx.logical_expr(0)), self.visit(ctx.logical_expr(1)))
        else:
            return self.visit(ctx.logical_expr(0))

    def visitLogical_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.AND_AND():
            return BinExpr(ctx.AND_AND().getText(), self.visit(ctx.logical_expr()), self.visit(ctx.adding_expr()))
        elif ctx.OR_OR():
            return BinExpr(ctx.OR_OR().getText(), self.visit(ctx.logical_expr()), self.visit(ctx.adding_expr()))
        else:
            return self.visit(ctx.adding_expr())

    def visitAdding_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.ADD():
            return BinExpr(ctx.ADD().getText(), self.visit(ctx.adding_expr()), self.visit(ctx.multiplying_expr()))
        elif ctx.MINUS():
            return BinExpr(ctx.MINUS().getText(), self.visit(ctx.adding_expr()), self.visit(ctx.multiplying_expr()))
        else:
            return self.visit(ctx.multiplying_expr())

    def visitMultiplying_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.STAR():
            return BinExpr(ctx.STAR().getText(), self.visit(ctx.multiplying_expr()), self.visit(ctx.negate_expr()))
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.multiplying_expr()), self.visit(ctx.negate_expr()))
        elif ctx.MOD():
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.multiplying_expr()), self.visit(ctx.negate_expr()))
        else:
            return self.visit(ctx.negate_expr())

    def visitNegate_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.NOT():
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.negate_expr()))
        else:
            return self.visit(ctx.sign_expr())

    def visitSign_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.MINUS():
            return UnExpr(ctx.MINUS().getText(), self.visit(ctx.sign_expr()))
        else:
            return self.visit(ctx.indexing_expr_fall_through())

    def visitIndexing_expr(self, ctx: MT22Parser.ProgramContext):
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.expr_list()))

    def visitIndexing_expr_fall_through(self, ctx: MT22Parser.ProgramContext):
        if ctx.indexing_expr():
            return self.visit(ctx.indexing_expr())
        else:
            return self.visit(ctx.braced_expr())

    def visitBraced_expr(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: MT22Parser.ProgramContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return Id(ctx.IDENTIFIER().getText())

    def visitLiteral(self, ctx: MT22Parser.ProgramContext):
        if ctx.INTEGER_LIT():
            return IntegerLit(int(ctx.INTEGER_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOLEAN_LIT():
            return BooleanLit(self.to_bool(ctx.BOOLEAN_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLit(ctx.STRING_LIT().getText())
        else:
            return self.visit(ctx.indexed_array_lit())

    def visitIndexed_array_lit(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr_list():
            return ArrayLit(self.visit(ctx.expr_list()))
        else:
            return ArrayLit([])

    def visitFunction_call(self, ctx: MT22Parser.ProgramContext):
        if ctx.expr_list():
            return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.expr_list()))
        else:
            return FuncCall(ctx.IDENTIFIER().getText(), [])
