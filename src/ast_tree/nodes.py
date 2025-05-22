# Definicje klas AST (np. AgentDef, Send, If, Loop). To czyste obiekty danych.

class ASTNode:
    pass

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class VarReference(ASTNode):
    def __init__(self, name):
        self.name = name

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op  # "+", "-", "*", "/"
        self.right = right

class VariableDecl(ASTNode):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

class Assignment(ASTNode):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

class PrintStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements