# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

from core.agentid import AgentId
import logging
from ast_tree.nodes import VariableDeclNode, AssignmentNode, SpawnNode, SelfAccessNode, LiteralNode, MessageInitNode, SendNode, PrintNode, KillNode, VarRefNode
from core.agentarTypes import AGENTAR_TYPE_MAP
from runtime.MessageInstance import MessageInstance


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
        self.agentInstance = None  # Placeholder for the agent instance  

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.name}', id='{self.agentInstance.id.path}'\n"
            f"  Fields: {list(self.fields.keys())}\n"
            f"  Actions: {list(self.actions.keys())}\n"
            f"  Receive handlers: {list(self.receive.keys())}\n"
            f"</AgentarAgent>"
        )
    
    def execute_action(self, action_name):
        logging.info(f"{self.agentInstance.id.path}:: Executing action...")


    def process_messages(self, inbox):
        logging.info(f"{self.agentInstance.id.path}:: Processing messages...")


    # === Statement Execution ===============================================
    def execute_stmt(self, stmt, local_var, local_var_type):
        logging.info(f"{self.agentInstance.id.path}:: Executing statement...{stmt}") # TODO: remove logging
        # VariableDeclNode handles variable declarations
        if isinstance(stmt, VariableDeclNode):
            if isinstance(stmt.name, SelfAccessNode):
                pass # TODO: handle self-access variable declaration

            elif stmt.value is None:
                local_var[stmt.name] = None
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type)

            elif stmt.value is not None:
                value = self.eval_expr(stmt.value)
                if not AGENTAR_TYPE_MAP[stmt.var_type] == type(value):
                    raise TypeError(f"Type mismatch in variable declaration for {stmt.target}: expected {AGENTAR_TYPE_MAP[stmt.type]}, got {type(value)}")
                local_var[stmt.name] = value
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type)


        # AssignmentNode handles different types of assignments
        elif isinstance(stmt, AssignmentNode):
            if isinstance(stmt.target, SelfAccessNode):
                target = stmt.target.path[1]
                value = self.eval_expr(stmt.value)
                if not self.fields_type[target] == type(value):
                    raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
                self.fields[target] = value
                return 0
            
            elif stmt.index is not None:
                pass # TODO: handle indexed assignment

            elif isinstance(stmt.value, SpawnNode):
                if stmt.target not in local_var_type:
                    raise NameError(f"Variable '{stmt.target}' is not declared.")
                fields = [self.eval_expr(arg) for arg in stmt.value.args] if stmt.value.args else []
                value = self.runtime.spawn_agent(parentInstance = self.agentInstance, agent_type = stmt.value.agent_type, fields = fields)

            elif isinstance(stmt.value, MessageInitNode):
                message = stmt.value
                if message.message_type not in self.runtime.messages_decl:
                    raise NameError(f"Message type '{message.message_type}' is not declared.")
                if self.runtime.messages_decl[message.message_type].content.keys() != message.fields.keys():
                    raise ValueError(f"Message fields do not match declaration for {message.message_type}. Expected {self.runtime.messages_decl[message.message_type].content.keys()}, got {message.fields.keys()}")
                content = {}
                for key, val, ref_type in zip(message.fields.keys(), message.fields.values(), self.runtime.messages_decl[message.message_type].content_type.values()):
                    val = self.eval_expr(val)
                    if not isinstance(val, ref_type):
                        raise TypeError(f"Type mismatch in message field '{val}': expected {ref_type}, got {type(val)}")
                    content[key] = val
                value = MessageInstance(name=message.message_type, content=content)

            else:
                if stmt.target not in local_var_type:
                    raise NameError(f"Variable '{stmt.target}' is not declared.")
                value = self.eval_expr(stmt.value)
                if not local_var_type[stmt.target] == type(value):
                    raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
            
            local_var[stmt.target] = value


        # SendNode handles sending messages
        elif isinstance(stmt, SendNode):
            logging.info(f"{self.agentInstance.id.path}:: Sending message to {stmt.to}...")
            # TODO: Implement message sending logic

        # print statement
        elif isinstance(stmt, PrintNode):
            to_print = [self.eval_expr(value, local_var, local_var_type) for value in stmt.values]
            print(f"AGENT {self.agentInstance.id}::", " ".join(str(v) for v in to_print))

        # KillNode handles agent termination
        elif isinstance(stmt, KillNode):
            if self.agentInstance.isMother:
                self.runtime.killMother()
            else:
                self.runtime.killAgent(self.agentInstance.id)


    def eval_expr(self, expr, local_var=None, local_var_type=None):
        if isinstance(expr, LiteralNode):
            return expr.value
        if isinstance(expr, VarRefNode):
            if expr.name in self.fields:
                return self.fields[expr.name]
            elif expr.name in local_var:
                return local_var[expr.name]
            else:
                raise NameError(f"Variable '{expr.name}' is not declared.")
        if isinstance(expr, SelfAccessNode):
            return self.fields[expr.path[1]] if expr.path[1] in self.fields else None