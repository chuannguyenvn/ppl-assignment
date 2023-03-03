from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce


class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail()) if ctx.getChildCount() == 2 else 0

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        return 2 + self.visit(ctx.ids()) if ctx.getChildCount() == 3 else 1
