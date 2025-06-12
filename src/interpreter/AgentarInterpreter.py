# -*- coding: utf-8 -*- 
# agentar/interpreter/interpreter.py
# main pypeline for runing the Agentar interpreter

from core.agent import AgentarAgent
from core.message import AgentarMessage
from core.agentid import AgentId
from ast_tree.nodes import *
from ast_tree.builder import AgentarToASTBuilder
from antlr4 import *
from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser
from dataclasses import is_dataclass
from dataclasses import dataclass, fields
from core.agentarTypes import AGENTAR_TYPE_MAP

class AgentarInterpreter:
    def __init__(self):
        self.mother_decl = AgentarAgent()  # Mother agent declaration
        self.agent = AgentarAgent()  
        self.message = AgentarMessage()
        self.agents_decl = {}       # Dict of agents declarations
        self.messages_decl = {}     # Dict of messages declarations

    def runAgentar(self, file_path):
        input_stream = FileStream(file_path)
        lexer = AgentarLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = AgentarParser(tokens)
        tree = parser.program()

        builder = AgentarToASTBuilder()
        ast_root = builder.visit(tree)

        self.visitAST(ast_root)
        
        return self.mother_decl, self.agents_decl, self.messages_decl


    def visitAST(self, ast_root):
        for decl in ast_root.declarations:
            if isinstance(decl, MotherNode):
                self.declareAgent(decl)
                self.mother_decl = self.agent
                self.mother_decl.isMother = True
                self.mother_decl.name = "MOTHER"
                self.agent = AgentarAgent()  # Reset for next agent
            elif isinstance(decl, AgentNode):
                self.declareAgent(decl)
                self.agent.name = decl.name
                self.agents_decl[decl.name] = self.agent
                self.agent = AgentarAgent()  # Reset for next agent
            elif isinstance(decl, MessageDeclNode):
                self.declareMessage(decl)
                self.messages_decl[decl.name] = self.message
                self.message = AgentarMessage()  # Reset for next message
            else:
                raise ValueError(f"Unknown declaration type: {type(decl)}")
            

    def declareAgent(self, node):
        for body in node.body:
            if isinstance(body, FieldSectionNode):
                self.FieldDeclare(body)
            elif isinstance(body, InitSectionNode):
                self.InitDeclare(body)
            elif isinstance(body, DestroySectionNode):
                self.DestroyDeclare(body)
            elif isinstance(body, ReceiveSectionNode):
                self.ReceiveDeclare(body)
            elif isinstance(body, ActionNode):
                self.ActionDeclare(body)
            else:
                raise ValueError(f"Unknown agent body section: {type(body)}")


    def FieldDeclare(self, node):
        for field in node.declarations:
            if field.value is None:
                self.agent.fields[field.name] = None
                self.agent.fields_type[field.name] = AGENTAR_TYPE_MAP.get(field.var_type)  # np. int, str, bool
            elif isinstance(field.value, LiteralNode or SpawnNode):
                self.agent.fields[field.name] = field.value.value  # np. 42, "hello", True
                self.agent.fields_type[field.name] = AGENTAR_TYPE_MAP.get(field.var_type)  # np. int, str, bool
            else:
                raise ValueError(f"Unsupported field value type: {type(field.value)}")

    def InitDeclare(self, node):
        for statement in node.statements:
            self.agent.initialize.append(statement)

    def DestroyDeclare(self, node):
        for statement in node.statements:
            self.agent.destroy.append(statement)

    def ReceiveDeclare(self, node):
        list_of_blocks = []
        for blok in node.blocks:
             list_of_blocks.append(blok)
        self.agent.receive[node.name] = list_of_blocks        
        
    def ActionDeclare(self, node):
        self.agent.actions[node.name] = node

    
    def declareMessage(self, node):
        self.message.name = node.name
        self.message.content = {field.name: field.value for field in node.fields}
        self.message.content_type = {field.name: AGENTAR_TYPE_MAP.get(field.var_type) for field in node.fields}