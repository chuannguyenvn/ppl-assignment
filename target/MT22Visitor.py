# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration_list.
    def visitDeclaration_list(self, ctx:MT22Parser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration_list_tail.
    def visitDeclaration_list_tail(self, ctx:MT22Parser.Declaration_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_declaration.
    def visitVariable_declaration(self, ctx:MT22Parser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#short_variable_declaration.
    def visitShort_variable_declaration(self, ctx:MT22Parser.Short_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#long_variable_declaration.
    def visitLong_variable_declaration(self, ctx:MT22Parser.Long_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_declaration_list.
    def visitParameter_declaration_list(self, ctx:MT22Parser.Parameter_declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_declaration_list_tail.
    def visitParameter_declaration_list_tail(self, ctx:MT22Parser.Parameter_declaration_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MT22Parser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list_tail.
    def visitIdentifier_list_tail(self, ctx:MT22Parser.Identifier_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_specifier.
    def visitType_specifier(self, ctx:MT22Parser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type_specifier.
    def visitArray_type_specifier(self, ctx:MT22Parser.Array_type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_list.
    def visitDimension_list(self, ctx:MT22Parser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_list_tail.
    def visitDimension_list_tail(self, ctx:MT22Parser.Dimension_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_declaration.
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_body.
    def visitFunction_body(self, ctx:MT22Parser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment_statement.
    def visitAssignment_statement(self, ctx:MT22Parser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_statement.
    def visitDo_while_statement(self, ctx:MT22Parser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement_element_list.
    def visitBlock_statement_element_list(self, ctx:MT22Parser.Block_statement_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement_element_list_tail.
    def visitBlock_statement_element_list_tail(self, ctx:MT22Parser.Block_statement_element_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list.
    def visitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_list_tail.
    def visitExpr_list_tail(self, ctx:MT22Parser.Expr_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_expr.
    def visitString_expr(self, ctx:MT22Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#negate_expr.
    def visitNegate_expr(self, ctx:MT22Parser.Negate_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexing_expr.
    def visitIndexing_expr(self, ctx:MT22Parser.Indexing_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexing_expr_fall_through.
    def visitIndexing_expr_fall_through(self, ctx:MT22Parser.Indexing_expr_fall_throughContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#braced_expr.
    def visitBraced_expr(self, ctx:MT22Parser.Braced_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexed_array_lit.
    def visitIndexed_array_lit(self, ctx:MT22Parser.Indexed_array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)



del MT22Parser