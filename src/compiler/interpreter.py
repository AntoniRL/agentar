import sys
from antlr4 import *

from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser
from antlr.AgentarVisitor import AgentarVisitor

class AgentarInterpreter(AgentarVisitor):
    def visitPrintStmt(self, ctx):
        text = ctx.STRING().getText()  # Pobiera tekst w cudzysłowach
        print(text[1:-1])  # Obcina cudzysłowy

def run_agentar(file_path):
    input_stream = FileStream(file_path)
    lexer = AgentarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AgentarParser(stream)
    tree = parser.program()
    
    interpreter = AgentarInterpreter()
    interpreter.visit(tree)