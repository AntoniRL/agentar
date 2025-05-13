# -*- coding: utf-8 -*- 
# Główna klasa interpretera – odwiedza AST i wykonuje go.

import sys
from antlr4 import *

from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser
from antlr.AgentarVisitor import AgentarVisitor

class AgentarInterpreter(AgentarVisitor):
    def __init__(self):
        self.variables = {}  # Przechowuje zmienne
    
    # Obsługa wyrażeń -------------------------------------------
    def visitIntLiteral(self, ctx):
        return int(ctx.INT().getText())
    
    def visitFloatLiteral(self, ctx):
        return float(ctx.FLOAT().getText())
    
    def visitStringLiteral(self, ctx):
        return ctx.STRING().getText()[1:-1]  # Usuwa cudzysłowy
    
    def visitBoolLiteral(self, ctx):
        return ctx.BOOL().getText() == 'true'
    
    def visitVarReference(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.variables:
            raise NameError(f"Nieznana zmienna: {var_name}")
        return self.variables[var_name]
    
    # Operacje matematyczne -------------------------------------
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right
    
    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        return left * right if op == '*' else left / right
    
    # Instrukcje ------------------------------------------------
    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
    
    def visitVariableDecl(self, ctx):
        var_name = ctx.ID().getText()
        if ctx.expression():
            self.variables[var_name] = self.visit(ctx.expression())
    
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        self.variables[var_name] = self.visit(ctx.expression())

