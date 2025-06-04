# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

from core.agentid import AgentId
import logging
from ast_tree.nodes import VariableDeclNode, AssignmentNode, SpawnNode, SelfAccessNode, LiteralNode
from core.agentarTypes import AGENTAR_TYPE_MAP

class AgentarAgent:
    def __init__(self):
        self.fields = {}
        self.fields_type = {}
        self.receive = {}
        self.actions = {}
        self.initialize = []
        self.destroy = []
        
        self.isMother = False
        self.name = None   

        self.runtime = None  # Placeholder for runtime context     

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.name}' id={self.id}>\n"
            f"  Fields: {list(self.fields.keys())}\n"
            f"  Actions: {list(self.actions.keys())}\n"
            f"  Receive handlers: {list(self.receive.keys())}\n"
            f"  Init statements: {len(self.initialize)}\n"
            f"  Destroy statements: {len(self.destroy)}\n"
            f"</AgentarAgent>"
        )
    
    def execute_action(self, action_name):
        logging.info("Executing action...")

    def process_messages(self, inbox):
        logging.info("Processing messages...")

    def execute_stmt(self, stmt, local_var, local_var_type):
        logging.info(f"Executing statement...{stmt}") # TODO: remove logging
        if isinstance(stmt, VariableDeclNode):
            value = self.eval_expr(stmt.value) if stmt.value else None
            var_type = stmt.var_type
            # TODO: handle var_type properly
            local_var[stmt.name] = value
            local_var_type[stmt.name] = var_type

        elif isinstance(stmt, AssignmentNode):
            if isinstance(stmt.target, SelfAccessNode):
                self.fields[stmt.target.path[1]] = self.eval_expr(stmt.value)
                self.fields_type[stmt.target.path[1]] = type(self.eval_expr(stmt.value))
                print(self.fields, self.fields_type)  # TODO: remove print
            elif isinstance(stmt.value, LiteralNode):
                pass
                # if checkType(type(stmt.value.value), local_var_type.get(stmt.target)):
                #     local_var[stmt.target] = stmt.value.value
                #     local_var_type[stmt.target] = type(stmt.value.value)


    def eval_expr(self, expr):
        if isinstance(expr, SpawnNode):
            logging.info(f"Spawning agent of type {expr.agent_type} with args {expr.args}")
            return None
        elif isinstance(expr, LiteralNode):
            return expr.value