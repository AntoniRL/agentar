# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from runtime.Agentar_builtins import builtins
from runtime.MessageInstance import MessageInstance
from core.agent import AgentarAgent
from core.message import AgentarMessage
from core.agentid import AgentId
from core.agentarTypes import AGENTAR_TYPE_MAP
from ast_tree.nodes import *
from queue import Queue
import logging
import time


class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None, fields = None):
        self.agent = agent_ast
        self.isMother = self.agent.isMother
        self.id = id        
        self.parent = id.parent() if not self.isMother else None
        self.children = []                  # List of agent children [AgentId]
        self.next_child = 1
        self.now = 1                        # time step counter (Agent perception time)
        self.inbox = Queue()                # Queue for incoming messages
        self.runtime = system               # Reference to the AgentarSystem instance
        self.fields = self.agent.fields                   # Agent Instance fields (variables)
        self.fields_type = self.agent.fields_type         # Agent Instance fields types (variables types)

        if fields is not None:
            for key, value, val_type in zip(self.agent.fields.keys(), fields, self.agent.fields_type.values()):
                if type(value) == val_type:
                    self.fields[key] = value
                    self.fields_type[key] = val_type

        self.fields["id"] = self.id   # Set the agent's id in its fields (Make it issier to access)
        self.fields_type["id"] = AgentId


    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.agent.name}', id='{self.id.path}'\n"
            f"</AgentarAgent>"
        )


    def initialize(self):
        logging.info(f"{self.id}:: Initializing agent")
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.initialize:
            self.execute_stmt(stmt, local_var, local_var_type)


    def step(self):
        # logging.info(f"Agent {self.id} stepping at time {self.now}") #TODO : remove logging
        self.now += 1


    def destroy(self):
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.destroy:
            self.execute_stmt(stmt, local_var, local_var_type)
        
        if not self.runtime.shutdown:
            with self.runtime.mutex:
                if not self.isMother:
                    del self.runtime.agents[self.id.path]
                    del self.runtime.threads[self.id.path]    

    def execute_action(self, action_name):
        logging.info(f"{self.id.path}:: Executing action...")


    def process_messages(self, inbox):
        logging.info(f"{self.id.path}:: Processing messages...")


    def execute_stmt(self, stmt, local_var, local_var_type):
        logging.info(f"{self.id.path}:: Executing statement...{stmt}") # TODO: remove logging

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
                value = self.runtime.spawn_agent(parentInstance = self , agent_type = stmt.value.agent_type, fields = fields)

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
            logging.info(f"{self.id.path}:: Sending message to {stmt.to}...")
            # TODO: Implement message sending logic

        # print statement
        elif isinstance(stmt, PrintNode):
            to_print = [self.eval_expr(value, local_var, local_var_type) for value in stmt.values]
            print(f"AGENT {self.id}::", " ".join(str(v) for v in to_print))

        # KillNode handles agent termination
        elif isinstance(stmt, KillNode):
            if self.isMother:
                self.runtime.killMother()
            else:
                self.runtime.killAgent(self.id)

        elif isinstance(stmt, SleepNode):
            duration = self.eval_expr(stmt.duration, local_var, local_var_type)
            logging.info(f"{self.id.path}:: Sleeping for {duration}s...") # TODO: remove logging
            time.sleep(duration)


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