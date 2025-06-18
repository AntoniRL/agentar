# -*- coding: utf-8 -*- 
# agentar/interpreter/interpreter.py
# main pypeline for runing the Agentar interpreter

import sys
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
from antlr4.error.ErrorListener import ErrorListener

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Line {line}:{column} {msg}")


class AgentarInterpreter:
    def __init__(self):
        self.mother_decl = AgentarAgent()  # Mother agent declaration
        self.agent = AgentarAgent()  
        self.message = AgentarMessage()
        self.agents_decl = {}       # Dict of agents declarations
        self.messages_decl = {}     # Dict of messages declarations

    def runAgentar(self, file_path):
        try:
            input_stream = FileStream(file_path)
            lexer = AgentarLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = AgentarParser(tokens)

            # delete default error listeners
            parser.removeErrorListeners()
            # add custom error listener that throws exceptions
            parser.addErrorListener(ThrowingErrorListener())
            tree = parser.program()
        except SyntaxError as e:
            print(f"ERROR: Syntax error in the file {file_path}: {e}")
            sys.exit(1)

        builder = AgentarToASTBuilder()
        ast_root = builder.visit(tree)

        self.visitAST(ast_root)

        return self.mother_decl, self.agents_decl, self.messages_decl


    def visitAST(self, ast_root):
        for decl in ast_root.declarations:
            if isinstance(decl, MotherNode):
                self.declareAgent(decl)
                self.mother_decl = self.agent
                self.mother_decl._isMother = True
                self.mother_decl._name = "MOTHER"
                self.agent = AgentarAgent()  # Reset for next agent
            elif isinstance(decl, AgentNode):
                self.declareAgent(decl)
                self.agent._name = decl.name
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
            elif isinstance(body, BeliefSectionNode):
                self.BeliefDeclare(body)
            elif isinstance(body, SeanseSectionNode):
                self.SenseDeclare(body)
            elif isinstance(body, GoalSectionNode):
                self.GoalDeclare(body)
            elif isinstance(body, RulesSectionNode):
                self.RulesDeclare(body)
            elif isinstance(body, ReceiveSectionNode):
                self.ReceiveDeclare(body)
            elif isinstance(body, ActionNode):
                self.ActionDeclare(body)
            else:
                raise ValueError(f"Unknown agent body section: {type(body)}")


    def FieldDeclare(self, node):
        for field in node.declarations:
            # chek if field has value or not then make sure it is correct class
            if field.value is None:
                type_name = AGENTAR_TYPE_MAP.get(field.var_type)
                default_value = None
                if type_name in (int, float):
                    default_value = type_name(0)
                elif type_name is str:
                    default_value = ""
                elif type_name is bool:
                    default_value = False
                elif type_name is list:
                    default_value = []
                elif type_name is dict:
                    default_value = {}                
                self.agent._fields[field.name] = default_value
                self.agent._fields_type[field.name] = type_name  # np. int, str, bool
            elif isinstance(field.value, LiteralNode or SpawnNode):
                self.agent._fields[field.name] = field.value.value  # np. 42, "hello", True
                self.agent._fields_type[field.name] = AGENTAR_TYPE_MAP.get(field.var_type)  # np. int, str, bool
            else:
                raise ValueError(f"Unsupported field value type: {type(field.value)}")


    def InitDeclare(self, node):
        for statement in node.statements:
            self.agent._initialize.append(statement)


    def DestroyDeclare(self, node):
        for statement in node.statements:
            self.agent._destroy.append(statement)


    def BeliefDeclare(self, node):
        for belief in node.declarations:
            # chek if field has value or not then make sure it is correct class
            if belief.value is None:
                type_name = AGENTAR_TYPE_MAP.get(belief.var_type)
                default_value = None
                if type_name in (int, float):
                    default_value = type_name(0)
                elif type_name is str:
                    default_value = ""
                elif type_name is bool:
                    default_value = False
                elif type_name is list:
                    default_value = []
                elif type_name is dict:
                    default_value = {}                
                self.agent._beliefs[belief.name] = default_value
                self.agent._beliefs_type[belief.name] = type_name  # np. int, str, bool
            elif isinstance(belief.value, LiteralNode):
                self.agent._beliefs[belief.name] = belief.value.value  # np. 42, "hello", True
                self.agent._beliefs_type[belief.name] = AGENTAR_TYPE_MAP.get(belief.var_type)  # np. int, str, bool
            else:
                raise ValueError(f"Unsupported field value type: {type(belief.value)}")


    def SenseDeclare(self, node):
        for statement in node.statements:
            self.agent._sense.append(statement)


    def GoalDeclare(self, node):
        for goal in node.goals:
            self.agent._sub_goals[goal.name] = goal.condition
        self.agent._merge_goals_condition = node.merge_condition if node.merge_condition else None


    def RulesDeclare(self, node):
        for rule in node.rules:
            self.agent._rules.append(rule)


    def ReceiveDeclare(self, node):
        list_of_blocks = []
        for blok in node.blocks:
             list_of_blocks.append(blok)
        self.agent._receive[node.name] = list_of_blocks        
        
    def ActionDeclare(self, node):
        self.agent._actions[node.name] = node

    
    def declareMessage(self, node):
        self.message._name = node.name
        self.message._content = {field.name: field.value for field in node.fields}
        self.message._content_type = {field.name: AGENTAR_TYPE_MAP.get(field.var_type) for field in node.fields}