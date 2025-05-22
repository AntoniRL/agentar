# Visitor, który buduje AST z drzewa składniowego ANTLR (dziedziczy po AgentarVisitor).
# agentar/ast/builder.py

from antlr.AgentarVisitor import AgentarVisitor
from ast_tree.nodes import *

class ASTBuilder(AgentarVisitor):
    def visitProgram(self, ctx):
        return Program([self.visit(stmt) for stmt in ctx.statement()])

    def visitVariableDecl(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return VariableDecl(name, expr)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression())
        return Assignment(name, expr)

    def visitPrintStmt(self, ctx):
        return PrintStatement(self.visit(ctx.expression()))

    def visitIntLiteral(self, ctx):
        return Literal(int(ctx.INT().getText()))

    def visitFloatLiteral(self, ctx):
        return Literal(float(ctx.FLOAT().getText()))

    def visitStringLiteral(self, ctx):
        return Literal(ctx.STRING().getText()[1:-1])

    def visitBoolLiteral(self, ctx):
        return Literal(ctx.BOOL().getText() == "true")

    def visitVarReference(self, ctx):
        return VarReference(ctx.ID().getText())

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return BinaryOp(left, ctx.op.text, right)

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return BinaryOp(left, ctx.op.text, right)