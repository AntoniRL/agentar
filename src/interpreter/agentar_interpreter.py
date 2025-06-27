# -*- coding: utf-8 -*- 
# agentar/interpreter/interpreter.py
# main pypeline for runing the Agentar interpreter

import sys
from core.agent import AgentarAgent
from core.message import AgentarMessage
from core.pointer import *
from core.agentar_types import resolve_type
from runtime.definicion_containers.variable_container import VariableContainer
from runtime.definicion_containers.agent_container import AgentContainer
from runtime.definicion_containers.message_container import MessageContainer
from runtime.errors import ThrowingErrorListener

from ast_tree.nodes import *
from ast_tree.builder import AgentarToASTBuilder
from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser
from antlr4 import *


class AgentarInterpreter:
    def __init__(self):
        self.mother_decl = AgentarAgent()           # Mother agent declaration
        self.agent = AgentarAgent()  
        self.message = AgentarMessage()
        self.agents_decl = AgentContainer()           # Structure of agents declarations
        self.messages_decl = MessageContainer()       # Structure of messages declarations

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
                self.mother_decl._line_declaration = decl._line
                self.agent = AgentarAgent()  # Reset for next agent
            elif isinstance(decl, AgentNode):
                self.declareAgent(decl)
                self.agent._name = decl.name
                self.agent._line_declaration = decl._line
                self.agents_decl.declare(decl.name, self.agent)  # Add to the agent container
                self.agent = AgentarAgent()     # Reset for next agent
            elif isinstance(decl, MessageDeclNode):
                self.declareMessage(decl)
                self.message._line_declaration = decl._line
                self.messages_decl.declare(decl.name, self.message)  # Add to the message container
                self.message = AgentarMessage()     # Reset for next message
            

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
            # chek if field has value
            if field.value is None:
                type_name, default_value = resolve_type(field.var_type)     
                self.agent._fields.declare(field.name, default_value, type_name, "Fields", field._line)
            elif isinstance(field.value, LiteralNode):
                type_name, _ = resolve_type(field.var_type)
                self.agent._fields.declare(field.name, field.value, type_name, "Fields", field._line)
            elif isinstance(field.value, ListLiteralNode):
                pass # TODO: implement list literal fields
                type_name, default_value = resolve_type(field.var_type)     
                self.agent._fields.declare(field.name, default_value, type_name, "Fields", field._line)
            elif isinstance(field.value, DictLiteralNode):
                pass # TODO: implement dict literal fields
                type_name, default_value = resolve_type(field.var_type)     
                self.agent._fields.declare(field.name, default_value, type_name, "Fields", field._line)
            elif isinstance(field.value, TupleLiteralNode):
                pass # TODO: implement tuple literal fields
                type_name, default_value = resolve_type(field.var_type)     
                self.agent._fields.declare(field.name, default_value, type_name, "Fields", field._line)
            else:
                raise ValueError(f"ERROR at line {field._line}: Unsupported field value type: {type(field.value)}")


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
                type_name , default_value = resolve_type(belief.var_type)             
                self.agent._beliefs.declare(belief.name, default_value, type_name, "Beliefs", belief._line)
            elif isinstance(belief.value, LiteralNode):
                type_name , _ = resolve_type(belief.var_type) 
                self.agent._beliefs.declare(belief.name, belief.value, type_name, "Beliefs", belief._line)
            elif isinstance(belief.value, ListLiteralNode): # TODO: implement list literal beliefs
                type_name , default_value = resolve_type(belief.var_type)             
                self.agent._beliefs.declare(belief.name, default_value, type_name, "Beliefs", belief._line)
            elif isinstance(belief.value, DictLiteralNode): # TODO: implement dict literal beliefs
                type_name , default_value = resolve_type(belief.var_type)             
                self.agent._beliefs.declare(belief.name, default_value, type_name, "Beliefs", belief._line)
            elif isinstance(belief.value, TupleLiteralNode): # TODO: implement tuple literal beliefs
                type_name , default_value = resolve_type(belief.var_type)             
                self.agent._beliefs.declare(belief.name, default_value, type_name, "Beliefs", belief._line)
            else:
                raise ValueError(f"ERROR at line {belief._line}: Unsupported belief value type: {type(belief.value)}")


    def SenseDeclare(self, node):
        for statement in node.statements:
            self.agent._sense.append(statement)


    def GoalDeclare(self, node):
        for goal in node.goals:
            self.agent._sub_goals.declare(goal.name, goal.condition)
        self.agent._merge_goals_condition = node.merge_condition if node.merge_condition else None


    def RulesDeclare(self, node):
        for rule in node.rules:
            self.agent._rules.append(rule)


    def ReceiveDeclare(self, node):
        list_of_blocks = []
        for blok in node.blocks:
             list_of_blocks.append(blok)
        self.agent._receive.declare(node.name, list_of_blocks)
        
        
    def ActionDeclare(self, node):
        self.agent._actions.declare(node.name, node)

    
    def declareMessage(self, node):
        self.message._name = node.name
        for field in node.fields:
            type_name , default_value = resolve_type(field.var_type)            
            self.message._content.declare(field.name, default_value, type_name, f"{node.name}_message", field._line)

        