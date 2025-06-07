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


    # Visit a parse tree produced by AgentarParser#motherDecl.
    def visitMotherDecl(self, ctx:AgentarParser.MotherDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#agentDecl.
    def visitAgentDecl(self, ctx:AgentarParser.AgentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#agentBody.
    def visitAgentBody(self, ctx:AgentarParser.AgentBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#fieldSection.
    def visitFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#initialSection.
    def visitInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#destroySection.
    def visitDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#receiveSection.
    def visitReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#whenBlock.
    def visitWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#actionSection.
    def visitActionSection(self, ctx:AgentarParser.ActionSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#parameterList.
    def visitParameterList(self, ctx:AgentarParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#parameter.
    def visitParameter(self, ctx:AgentarParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#messageDecl.
    def visitMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#sendStmt.
    def visitSendStmt(self, ctx:AgentarParser.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#spawnStmt.
    def visitSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#killStmt.
    def visitKillStmt(self, ctx:AgentarParser.KillStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#sleepStmt.
    def visitSleepStmt(self, ctx:AgentarParser.SleepStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#messageInit.
    def visitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#messageFieldAssign.
    def visitMessageFieldAssign(self, ctx:AgentarParser.MessageFieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#printStmt.
    def visitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#VarDecl.
    def visitVarDecl(self, ctx:AgentarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#SelfDecl.
    def visitSelfDecl(self, ctx:AgentarParser.SelfDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#SimpleAssign.
    def visitSimpleAssign(self, ctx:AgentarParser.SimpleAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#IndexAssign.
    def visitIndexAssign(self, ctx:AgentarParser.IndexAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#SpawnAssign.
    def visitSpawnAssign(self, ctx:AgentarParser.SpawnAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#SelfAssign.
    def visitSelfAssign(self, ctx:AgentarParser.SelfAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#doStmt.
    def visitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#type.
    def visitType(self, ctx:AgentarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MapExpr.
    def visitMapExpr(self, ctx:AgentarParser.MapExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#AndExpr.
    def visitAndExpr(self, ctx:AgentarParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#SelfAccessExpr.
    def visitSelfAccessExpr(self, ctx:AgentarParser.SelfAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#LeqExpr.
    def visitLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#XorExpr.
    def visitXorExpr(self, ctx:AgentarParser.XorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#GeqExpr.
    def visitGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MessageAccessExpr.
    def visitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#LtExpr.
    def visitLtExpr(self, ctx:AgentarParser.LtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#GtExpr.
    def visitGtExpr(self, ctx:AgentarParser.GtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#OrExpr.
    def visitOrExpr(self, ctx:AgentarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#IndexExpr.
    def visitIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#AgentIdExpr.
    def visitAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#VarReference.
    def visitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#EqExpr.
    def visitEqExpr(self, ctx:AgentarParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#NeqExpr.
    def visitNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MsgTypeValueExpr.
    def visitMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#NotExpr.
    def visitNotExpr(self, ctx:AgentarParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#ListExpr.
    def visitListExpr(self, ctx:AgentarParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#ParenExpr.
    def visitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#MessageInitExpr.
    def visitMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#listLiteral.
    def visitListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AgentarParser#mapLiteral.
    def visitMapLiteral(self, ctx:AgentarParser.MapLiteralContext):
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


    # Visit a parse tree produced by AgentarParser#msgTypeValue.
    def visitMsgTypeValue(self, ctx:AgentarParser.MsgTypeValueContext):
        return self.visitChildren(ctx)



del AgentarParser