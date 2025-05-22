# -*- coding: utf-8 -*- 
# Główna klasa interpretera – odwiedza AST i wykonuje go.

# agentar/interpreter/interpreter.py

from interpreter.agenter_builtins import builtins
from core.agent import *
from ast_tree.nodes import * 

class AgentarInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, program: Program):
        for stmt in program.statements:
            self.execute(stmt)

    def execute(self, node):
        if isinstance(node, VariableDecl):
            value = self.evaluate(node.expression) if node.expression else None
            self.variables[node.name] = value
        elif isinstance(node, Assignment):
            self.variables[node.name] = self.evaluate(node.expression)
        elif isinstance(node, PrintStatement):
            value = self.evaluate(node.expression)
            builtins["print"](value)
        else:
            raise RuntimeError(f"Nieobsługiwany typ instrukcji: {node}")

    def evaluate(self, expr):
        if isinstance(expr, Literal):
            return expr.value
        elif isinstance(expr, VarReference):
            if expr.name not in self.variables:
                raise NameError(f"Nieznana zmienna: {expr.name}")
            return self.variables[expr.name]
        elif isinstance(expr, BinaryOp):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            if expr.op == '+':
                return left + right
            elif expr.op == '-':
                return left - right
            elif expr.op == '*':
                return left * right
            elif expr.op == '/':
                return left / right
        else:
            raise RuntimeError(f"Nieobsługiwane wyrażenie: {type(expr)}")

