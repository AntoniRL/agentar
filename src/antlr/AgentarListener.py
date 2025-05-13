# Generated from /home/toni/mgr/agentar/grammar/Agentar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AgentarParser import AgentarParser
else:
    from AgentarParser import AgentarParser

# This class defines a complete listener for a parse tree produced by AgentarParser.
class AgentarListener(ParseTreeListener):

    # Enter a parse tree produced by AgentarParser#program.
    def enterProgram(self, ctx:AgentarParser.ProgramContext):
        pass

    # Exit a parse tree produced by AgentarParser#program.
    def exitProgram(self, ctx:AgentarParser.ProgramContext):
        pass


    # Enter a parse tree produced by AgentarParser#statement.
    def enterStatement(self, ctx:AgentarParser.StatementContext):
        pass

    # Exit a parse tree produced by AgentarParser#statement.
    def exitStatement(self, ctx:AgentarParser.StatementContext):
        pass


    # Enter a parse tree produced by AgentarParser#printStmt.
    def enterPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#printStmt.
    def exitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#variableDecl.
    def enterVariableDecl(self, ctx:AgentarParser.VariableDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#variableDecl.
    def exitVariableDecl(self, ctx:AgentarParser.VariableDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#assignment.
    def enterAssignment(self, ctx:AgentarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AgentarParser#assignment.
    def exitAssignment(self, ctx:AgentarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AgentarParser#type.
    def enterType(self, ctx:AgentarParser.TypeContext):
        pass

    # Exit a parse tree produced by AgentarParser#type.
    def exitType(self, ctx:AgentarParser.TypeContext):
        pass


    # Enter a parse tree produced by AgentarParser#VarReference.
    def enterVarReference(self, ctx:AgentarParser.VarReferenceContext):
        pass

    # Exit a parse tree produced by AgentarParser#VarReference.
    def exitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        pass


    # Enter a parse tree produced by AgentarParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#CompareExpr.
    def enterCompareExpr(self, ctx:AgentarParser.CompareExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#CompareExpr.
    def exitCompareExpr(self, ctx:AgentarParser.CompareExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#ParenExpr.
    def enterParenExpr(self, ctx:AgentarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#ParenExpr.
    def exitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#IntLiteral.
    def enterIntLiteral(self, ctx:AgentarParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#IntLiteral.
    def exitIntLiteral(self, ctx:AgentarParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#FloatLiteral.
    def enterFloatLiteral(self, ctx:AgentarParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#FloatLiteral.
    def exitFloatLiteral(self, ctx:AgentarParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#StringLiteral.
    def enterStringLiteral(self, ctx:AgentarParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#StringLiteral.
    def exitStringLiteral(self, ctx:AgentarParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#BoolLiteral.
    def enterBoolLiteral(self, ctx:AgentarParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#BoolLiteral.
    def exitBoolLiteral(self, ctx:AgentarParser.BoolLiteralContext):
        pass



del AgentarParser