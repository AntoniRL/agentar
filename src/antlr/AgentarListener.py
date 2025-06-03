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


    # Enter a parse tree produced by AgentarParser#motherDecl.
    def enterMotherDecl(self, ctx:AgentarParser.MotherDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#motherDecl.
    def exitMotherDecl(self, ctx:AgentarParser.MotherDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#agentDecl.
    def enterAgentDecl(self, ctx:AgentarParser.AgentDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#agentDecl.
    def exitAgentDecl(self, ctx:AgentarParser.AgentDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#agentBody.
    def enterAgentBody(self, ctx:AgentarParser.AgentBodyContext):
        pass

    # Exit a parse tree produced by AgentarParser#agentBody.
    def exitAgentBody(self, ctx:AgentarParser.AgentBodyContext):
        pass


    # Enter a parse tree produced by AgentarParser#fieldSection.
    def enterFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#fieldSection.
    def exitFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#initialSection.
    def enterInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#initialSection.
    def exitInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#destroySection.
    def enterDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#destroySection.
    def exitDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#receiveSection.
    def enterReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#receiveSection.
    def exitReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#whenBlock.
    def enterWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        pass

    # Exit a parse tree produced by AgentarParser#whenBlock.
    def exitWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        pass


    # Enter a parse tree produced by AgentarParser#actionSection.
    def enterActionSection(self, ctx:AgentarParser.ActionSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#actionSection.
    def exitActionSection(self, ctx:AgentarParser.ActionSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#parameterList.
    def enterParameterList(self, ctx:AgentarParser.ParameterListContext):
        pass

    # Exit a parse tree produced by AgentarParser#parameterList.
    def exitParameterList(self, ctx:AgentarParser.ParameterListContext):
        pass


    # Enter a parse tree produced by AgentarParser#parameter.
    def enterParameter(self, ctx:AgentarParser.ParameterContext):
        pass

    # Exit a parse tree produced by AgentarParser#parameter.
    def exitParameter(self, ctx:AgentarParser.ParameterContext):
        pass


    # Enter a parse tree produced by AgentarParser#messageDecl.
    def enterMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#messageDecl.
    def exitMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#sendStmt.
    def enterSendStmt(self, ctx:AgentarParser.SendStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#sendStmt.
    def exitSendStmt(self, ctx:AgentarParser.SendStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#spawnStmt.
    def enterSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#spawnStmt.
    def exitSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#killStmt.
    def enterKillStmt(self, ctx:AgentarParser.KillStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#killStmt.
    def exitKillStmt(self, ctx:AgentarParser.KillStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#messageInit.
    def enterMessageInit(self, ctx:AgentarParser.MessageInitContext):
        pass

    # Exit a parse tree produced by AgentarParser#messageInit.
    def exitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        pass


    # Enter a parse tree produced by AgentarParser#messageFieldAssign.
    def enterMessageFieldAssign(self, ctx:AgentarParser.MessageFieldAssignContext):
        pass

    # Exit a parse tree produced by AgentarParser#messageFieldAssign.
    def exitMessageFieldAssign(self, ctx:AgentarParser.MessageFieldAssignContext):
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


    # Enter a parse tree produced by AgentarParser#SimpleAssign.
    def enterSimpleAssign(self, ctx:AgentarParser.SimpleAssignContext):
        pass

    # Exit a parse tree produced by AgentarParser#SimpleAssign.
    def exitSimpleAssign(self, ctx:AgentarParser.SimpleAssignContext):
        pass


    # Enter a parse tree produced by AgentarParser#IndexAssign.
    def enterIndexAssign(self, ctx:AgentarParser.IndexAssignContext):
        pass

    # Exit a parse tree produced by AgentarParser#IndexAssign.
    def exitIndexAssign(self, ctx:AgentarParser.IndexAssignContext):
        pass


    # Enter a parse tree produced by AgentarParser#SpawnAssign.
    def enterSpawnAssign(self, ctx:AgentarParser.SpawnAssignContext):
        pass

    # Exit a parse tree produced by AgentarParser#SpawnAssign.
    def exitSpawnAssign(self, ctx:AgentarParser.SpawnAssignContext):
        pass


    # Enter a parse tree produced by AgentarParser#doStmt.
    def enterDoStmt(self, ctx:AgentarParser.DoStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#doStmt.
    def exitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#type.
    def enterType(self, ctx:AgentarParser.TypeContext):
        pass

    # Exit a parse tree produced by AgentarParser#type.
    def exitType(self, ctx:AgentarParser.TypeContext):
        pass


    # Enter a parse tree produced by AgentarParser#MapExpr.
    def enterMapExpr(self, ctx:AgentarParser.MapExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MapExpr.
    def exitMapExpr(self, ctx:AgentarParser.MapExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AndExpr.
    def enterAndExpr(self, ctx:AgentarParser.AndExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AndExpr.
    def exitAndExpr(self, ctx:AgentarParser.AndExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#SelfAccessExpr.
    def enterSelfAccessExpr(self, ctx:AgentarParser.SelfAccessExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#SelfAccessExpr.
    def exitSelfAccessExpr(self, ctx:AgentarParser.SelfAccessExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LeqExpr.
    def enterLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LeqExpr.
    def exitLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#XorExpr.
    def enterXorExpr(self, ctx:AgentarParser.XorExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#XorExpr.
    def exitXorExpr(self, ctx:AgentarParser.XorExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#GeqExpr.
    def enterGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#GeqExpr.
    def exitGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MessageAccessExpr.
    def enterMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MessageAccessExpr.
    def exitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LtExpr.
    def enterLtExpr(self, ctx:AgentarParser.LtExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LtExpr.
    def exitLtExpr(self, ctx:AgentarParser.LtExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#GtExpr.
    def enterGtExpr(self, ctx:AgentarParser.GtExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#GtExpr.
    def exitGtExpr(self, ctx:AgentarParser.GtExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#OrExpr.
    def enterOrExpr(self, ctx:AgentarParser.OrExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#OrExpr.
    def exitOrExpr(self, ctx:AgentarParser.OrExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#IndexExpr.
    def enterIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#IndexExpr.
    def exitIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AgentIdExpr.
    def enterAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AgentIdExpr.
    def exitAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
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


    # Enter a parse tree produced by AgentarParser#EqExpr.
    def enterEqExpr(self, ctx:AgentarParser.EqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#EqExpr.
    def exitEqExpr(self, ctx:AgentarParser.EqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#NeqExpr.
    def enterNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#NeqExpr.
    def exitNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MsgTypeValueExpr.
    def enterMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MsgTypeValueExpr.
    def exitMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#NotExpr.
    def enterNotExpr(self, ctx:AgentarParser.NotExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#NotExpr.
    def exitNotExpr(self, ctx:AgentarParser.NotExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#ListExpr.
    def enterListExpr(self, ctx:AgentarParser.ListExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#ListExpr.
    def exitListExpr(self, ctx:AgentarParser.ListExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#ParenExpr.
    def enterParenExpr(self, ctx:AgentarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#ParenExpr.
    def exitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MessageInitExpr.
    def enterMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MessageInitExpr.
    def exitMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#listLiteral.
    def enterListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#listLiteral.
    def exitListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#mapLiteral.
    def enterMapLiteral(self, ctx:AgentarParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#mapLiteral.
    def exitMapLiteral(self, ctx:AgentarParser.MapLiteralContext):
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


    # Enter a parse tree produced by AgentarParser#msgTypeValue.
    def enterMsgTypeValue(self, ctx:AgentarParser.MsgTypeValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#msgTypeValue.
    def exitMsgTypeValue(self, ctx:AgentarParser.MsgTypeValueContext):
        pass



del AgentarParser