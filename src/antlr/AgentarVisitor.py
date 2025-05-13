# Generated from /home/toni/mgr/agentar/grammar/Agentar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AgentarParser import AgentarParser
else:
    from AgentarParser import AgentarParser

# This class defines a complete generic visitor for a parse tree produced by AgentarParser.

class AgentarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AgentarParser#program.
    def visitProgram(self, ctx:AgentarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#statement.
    def visitStatement(self, ctx:AgentarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#printStmt.
    def visitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#variableDecl.
    def visitVariableDecl(self, ctx:AgentarParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#assignment.
    def visitAssignment(self, ctx:AgentarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#type.
    def visitType(self, ctx:AgentarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#VarReference.
    def visitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#CompareExpr.
    def visitCompareExpr(self, ctx:AgentarParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#ParenExpr.
    def visitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#IntLiteral.
    def visitIntLiteral(self, ctx:AgentarParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#FloatLiteral.
    def visitFloatLiteral(self, ctx:AgentarParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#StringLiteral.
    def visitStringLiteral(self, ctx:AgentarParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#BoolLiteral.
    def visitBoolLiteral(self, ctx:AgentarParser.BoolLiteralContext):
        return self.visitChildren(ctx)



del AgentarParser