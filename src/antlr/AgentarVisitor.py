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



del AgentarParser