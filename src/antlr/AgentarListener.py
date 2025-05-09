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



del AgentarParser