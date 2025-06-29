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


    # Enter a parse tree produced by AgentarParser#beliefsSection.
    def enterBeliefsSection(self, ctx:AgentarParser.BeliefsSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#beliefsSection.
    def exitBeliefsSection(self, ctx:AgentarParser.BeliefsSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#senseSection.
    def enterSenseSection(self, ctx:AgentarParser.SenseSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#senseSection.
    def exitSenseSection(self, ctx:AgentarParser.SenseSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#goalsSection.
    def enterGoalsSection(self, ctx:AgentarParser.GoalsSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#goalsSection.
    def exitGoalsSection(self, ctx:AgentarParser.GoalsSectionContext):
        pass


    # Enter a parse tree produced by AgentarParser#goalBlock.
    def enterGoalBlock(self, ctx:AgentarParser.GoalBlockContext):
        pass

    # Exit a parse tree produced by AgentarParser#goalBlock.
    def exitGoalBlock(self, ctx:AgentarParser.GoalBlockContext):
        pass


    # Enter a parse tree produced by AgentarParser#rulesSection.
    def enterRulesSection(self, ctx:AgentarParser.RulesSectionContext):
        pass

    # Exit a parse tree produced by AgentarParser#rulesSection.
    def exitRulesSection(self, ctx:AgentarParser.RulesSectionContext):
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


    # Enter a parse tree produced by AgentarParser#sendParentStmt.
    def enterSendParentStmt(self, ctx:AgentarParser.SendParentStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#sendParentStmt.
    def exitSendParentStmt(self, ctx:AgentarParser.SendParentStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#sendChildrenStmt.
    def enterSendChildrenStmt(self, ctx:AgentarParser.SendChildrenStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#sendChildrenStmt.
    def exitSendChildrenStmt(self, ctx:AgentarParser.SendChildrenStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#sendSiblingStmt.
    def enterSendSiblingStmt(self, ctx:AgentarParser.SendSiblingStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#sendSiblingStmt.
    def exitSendSiblingStmt(self, ctx:AgentarParser.SendSiblingStmtContext):
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


    # Enter a parse tree produced by AgentarParser#killchildrenStmt.
    def enterKillchildrenStmt(self, ctx:AgentarParser.KillchildrenStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#killchildrenStmt.
    def exitKillchildrenStmt(self, ctx:AgentarParser.KillchildrenStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#sleepStmt.
    def enterSleepStmt(self, ctx:AgentarParser.SleepStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#sleepStmt.
    def exitSleepStmt(self, ctx:AgentarParser.SleepStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#returnStmt.
    def enterReturnStmt(self, ctx:AgentarParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#returnStmt.
    def exitReturnStmt(self, ctx:AgentarParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#senseStmt.
    def enterSenseStmt(self, ctx:AgentarParser.SenseStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#senseStmt.
    def exitSenseStmt(self, ctx:AgentarParser.SenseStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#goalCheckStmt.
    def enterGoalCheckStmt(self, ctx:AgentarParser.GoalCheckStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#goalCheckStmt.
    def exitGoalCheckStmt(self, ctx:AgentarParser.GoalCheckStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#getTimeStmt.
    def enterGetTimeStmt(self, ctx:AgentarParser.GetTimeStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#getTimeStmt.
    def exitGetTimeStmt(self, ctx:AgentarParser.GetTimeStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#dictDelStmt.
    def enterDictDelStmt(self, ctx:AgentarParser.DictDelStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#dictDelStmt.
    def exitDictDelStmt(self, ctx:AgentarParser.DictDelStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#listAddStmt.
    def enterListAddStmt(self, ctx:AgentarParser.ListAddStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#listAddStmt.
    def exitListAddStmt(self, ctx:AgentarParser.ListAddStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#printStmt.
    def enterPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#printStmt.
    def exitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#loggingStmt.
    def enterLoggingStmt(self, ctx:AgentarParser.LoggingStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#loggingStmt.
    def exitLoggingStmt(self, ctx:AgentarParser.LoggingStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#ifStmt.
    def enterIfStmt(self, ctx:AgentarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#ifStmt.
    def exitIfStmt(self, ctx:AgentarParser.IfStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#blockOrStmt.
    def enterBlockOrStmt(self, ctx:AgentarParser.BlockOrStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#blockOrStmt.
    def exitBlockOrStmt(self, ctx:AgentarParser.BlockOrStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#elseStmt.
    def enterElseStmt(self, ctx:AgentarParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#elseStmt.
    def exitElseStmt(self, ctx:AgentarParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#forStmt.
    def enterForStmt(self, ctx:AgentarParser.ForStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#forStmt.
    def exitForStmt(self, ctx:AgentarParser.ForStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#forBody.
    def enterForBody(self, ctx:AgentarParser.ForBodyContext):
        pass

    # Exit a parse tree produced by AgentarParser#forBody.
    def exitForBody(self, ctx:AgentarParser.ForBodyContext):
        pass


    # Enter a parse tree produced by AgentarParser#forAssignExpr.
    def enterForAssignExpr(self, ctx:AgentarParser.ForAssignExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#forAssignExpr.
    def exitForAssignExpr(self, ctx:AgentarParser.ForAssignExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#whileStmt.
    def enterWhileStmt(self, ctx:AgentarParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#whileStmt.
    def exitWhileStmt(self, ctx:AgentarParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#breakStmt.
    def enterBreakStmt(self, ctx:AgentarParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#breakStmt.
    def exitBreakStmt(self, ctx:AgentarParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#continueStmt.
    def enterContinueStmt(self, ctx:AgentarParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#continueStmt.
    def exitContinueStmt(self, ctx:AgentarParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#doStmt.
    def enterDoStmt(self, ctx:AgentarParser.DoStmtContext):
        pass

    # Exit a parse tree produced by AgentarParser#doStmt.
    def exitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        pass


    # Enter a parse tree produced by AgentarParser#VarDecl.
    def enterVarDecl(self, ctx:AgentarParser.VarDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#VarDecl.
    def exitVarDecl(self, ctx:AgentarParser.VarDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#MessageVarDecl.
    def enterMessageVarDecl(self, ctx:AgentarParser.MessageVarDeclContext):
        pass

    # Exit a parse tree produced by AgentarParser#MessageVarDecl.
    def exitMessageVarDecl(self, ctx:AgentarParser.MessageVarDeclContext):
        pass


    # Enter a parse tree produced by AgentarParser#assignment.
    def enterAssignment(self, ctx:AgentarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AgentarParser#assignment.
    def exitAssignment(self, ctx:AgentarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AgentarParser#SimpleAssignValue.
    def enterSimpleAssignValue(self, ctx:AgentarParser.SimpleAssignValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#SimpleAssignValue.
    def exitSimpleAssignValue(self, ctx:AgentarParser.SimpleAssignValueContext):
        pass


    # Enter a parse tree produced by AgentarParser#GetTimeAssignValue.
    def enterGetTimeAssignValue(self, ctx:AgentarParser.GetTimeAssignValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#GetTimeAssignValue.
    def exitGetTimeAssignValue(self, ctx:AgentarParser.GetTimeAssignValueContext):
        pass


    # Enter a parse tree produced by AgentarParser#SpawnAssignValue.
    def enterSpawnAssignValue(self, ctx:AgentarParser.SpawnAssignValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#SpawnAssignValue.
    def exitSpawnAssignValue(self, ctx:AgentarParser.SpawnAssignValueContext):
        pass


    # Enter a parse tree produced by AgentarParser#DoAssignValue.
    def enterDoAssignValue(self, ctx:AgentarParser.DoAssignValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#DoAssignValue.
    def exitDoAssignValue(self, ctx:AgentarParser.DoAssignValueContext):
        pass


    # Enter a parse tree produced by AgentarParser#GoalCheckAssignValue.
    def enterGoalCheckAssignValue(self, ctx:AgentarParser.GoalCheckAssignValueContext):
        pass

    # Exit a parse tree produced by AgentarParser#GoalCheckAssignValue.
    def exitGoalCheckAssignValue(self, ctx:AgentarParser.GoalCheckAssignValueContext):
        pass


    # Enter a parse tree produced by AgentarParser#AndExpr.
    def enterAndExpr(self, ctx:AgentarParser.AndExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AndExpr.
    def exitAndExpr(self, ctx:AgentarParser.AndExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LeqExpr.
    def enterLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LeqExpr.
    def exitLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AbsExpr.
    def enterAbsExpr(self, ctx:AgentarParser.AbsExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AbsExpr.
    def exitAbsExpr(self, ctx:AgentarParser.AbsExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#GeqExpr.
    def enterGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#GeqExpr.
    def exitGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#NegExpr.
    def enterNegExpr(self, ctx:AgentarParser.NegExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#NegExpr.
    def exitNegExpr(self, ctx:AgentarParser.NegExprContext):
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


    # Enter a parse tree produced by AgentarParser#ModuloExpr.
    def enterModuloExpr(self, ctx:AgentarParser.ModuloExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#ModuloExpr.
    def exitModuloExpr(self, ctx:AgentarParser.ModuloExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#VarReference.
    def enterVarReference(self, ctx:AgentarParser.VarReferenceContext):
        pass

    # Exit a parse tree produced by AgentarParser#VarReference.
    def exitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        pass


    # Enter a parse tree produced by AgentarParser#SliceToExpr.
    def enterSliceToExpr(self, ctx:AgentarParser.SliceToExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#SliceToExpr.
    def exitSliceToExpr(self, ctx:AgentarParser.SliceToExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#SliceFromExpr.
    def enterSliceFromExpr(self, ctx:AgentarParser.SliceFromExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#SliceFromExpr.
    def exitSliceFromExpr(self, ctx:AgentarParser.SliceFromExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#SliceRangeExpr.
    def enterSliceRangeExpr(self, ctx:AgentarParser.SliceRangeExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#SliceRangeExpr.
    def exitSliceRangeExpr(self, ctx:AgentarParser.SliceRangeExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#NeqExpr.
    def enterNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#NeqExpr.
    def exitNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#RandomExpr.
    def enterRandomExpr(self, ctx:AgentarParser.RandomExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#RandomExpr.
    def exitRandomExpr(self, ctx:AgentarParser.RandomExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#DictExpr.
    def enterDictExpr(self, ctx:AgentarParser.DictExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#DictExpr.
    def exitDictExpr(self, ctx:AgentarParser.DictExprContext):
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


    # Enter a parse tree produced by AgentarParser#MessageInitExpr.
    def enterMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MessageInitExpr.
    def exitMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#DictKeysExpr.
    def enterDictKeysExpr(self, ctx:AgentarParser.DictKeysExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#DictKeysExpr.
    def exitDictKeysExpr(self, ctx:AgentarParser.DictKeysExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#DictGetExpr.
    def enterDictGetExpr(self, ctx:AgentarParser.DictGetExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#DictGetExpr.
    def exitDictGetExpr(self, ctx:AgentarParser.DictGetExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#SelfAccessExpr.
    def enterSelfAccessExpr(self, ctx:AgentarParser.SelfAccessExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#SelfAccessExpr.
    def exitSelfAccessExpr(self, ctx:AgentarParser.SelfAccessExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#XorExpr.
    def enterXorExpr(self, ctx:AgentarParser.XorExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#XorExpr.
    def exitXorExpr(self, ctx:AgentarParser.XorExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#LenExpr.
    def enterLenExpr(self, ctx:AgentarParser.LenExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#LenExpr.
    def exitLenExpr(self, ctx:AgentarParser.LenExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MessageAccessExpr.
    def enterMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MessageAccessExpr.
    def exitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#TypeExpr.
    def enterTypeExpr(self, ctx:AgentarParser.TypeExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#TypeExpr.
    def exitTypeExpr(self, ctx:AgentarParser.TypeExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#TupleExpr.
    def enterTupleExpr(self, ctx:AgentarParser.TupleExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#TupleExpr.
    def exitTupleExpr(self, ctx:AgentarParser.TupleExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#OrExpr.
    def enterOrExpr(self, ctx:AgentarParser.OrExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#OrExpr.
    def exitOrExpr(self, ctx:AgentarParser.OrExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#DictValuesExpr.
    def enterDictValuesExpr(self, ctx:AgentarParser.DictValuesExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#DictValuesExpr.
    def exitDictValuesExpr(self, ctx:AgentarParser.DictValuesExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#BeliefAccessExpr.
    def enterBeliefAccessExpr(self, ctx:AgentarParser.BeliefAccessExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#BeliefAccessExpr.
    def exitBeliefAccessExpr(self, ctx:AgentarParser.BeliefAccessExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#AddressOfExpr.
    def enterAddressOfExpr(self, ctx:AgentarParser.AddressOfExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#AddressOfExpr.
    def exitAddressOfExpr(self, ctx:AgentarParser.AddressOfExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#DeepCopyExpr.
    def enterDeepCopyExpr(self, ctx:AgentarParser.DeepCopyExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#DeepCopyExpr.
    def exitDeepCopyExpr(self, ctx:AgentarParser.DeepCopyExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#EqExpr.
    def enterEqExpr(self, ctx:AgentarParser.EqExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#EqExpr.
    def exitEqExpr(self, ctx:AgentarParser.EqExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#NoneExpr.
    def enterNoneExpr(self, ctx:AgentarParser.NoneExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#NoneExpr.
    def exitNoneExpr(self, ctx:AgentarParser.NoneExprContext):
        pass


    # Enter a parse tree produced by AgentarParser#MsgTypeValueExpr.
    def enterMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        pass

    # Exit a parse tree produced by AgentarParser#MsgTypeValueExpr.
    def exitMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
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


    # Enter a parse tree produced by AgentarParser#listLiteral.
    def enterListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#listLiteral.
    def exitListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#dictLiteral.
    def enterDictLiteral(self, ctx:AgentarParser.DictLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#dictLiteral.
    def exitDictLiteral(self, ctx:AgentarParser.DictLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#dictEntry.
    def enterDictEntry(self, ctx:AgentarParser.DictEntryContext):
        pass

    # Exit a parse tree produced by AgentarParser#dictEntry.
    def exitDictEntry(self, ctx:AgentarParser.DictEntryContext):
        pass


    # Enter a parse tree produced by AgentarParser#tupleLiteral.
    def enterTupleLiteral(self, ctx:AgentarParser.TupleLiteralContext):
        pass

    # Exit a parse tree produced by AgentarParser#tupleLiteral.
    def exitTupleLiteral(self, ctx:AgentarParser.TupleLiteralContext):
        pass


    # Enter a parse tree produced by AgentarParser#BasicType.
    def enterBasicType(self, ctx:AgentarParser.BasicTypeContext):
        pass

    # Exit a parse tree produced by AgentarParser#BasicType.
    def exitBasicType(self, ctx:AgentarParser.BasicTypeContext):
        pass


    # Enter a parse tree produced by AgentarParser#PointerType.
    def enterPointerType(self, ctx:AgentarParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by AgentarParser#PointerType.
    def exitPointerType(self, ctx:AgentarParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by AgentarParser#bodyType.
    def enterBodyType(self, ctx:AgentarParser.BodyTypeContext):
        pass

    # Exit a parse tree produced by AgentarParser#bodyType.
    def exitBodyType(self, ctx:AgentarParser.BodyTypeContext):
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