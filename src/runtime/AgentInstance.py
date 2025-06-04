# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from runtime.Agentar_builtins import builtins
from core.agent import AgentarAgent
from core.message import AgentarMessage
from core.agentid import AgentId
from core.agentarTypes import AGENTAR_TYPE_MAP
from ast_tree.nodes import *
from queue import Queue
import logging


class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None, fields = None):
        self.agent = agent_ast
        self.agent.runtime = system
        self.agent.AgetnInstance = self
        self.isMother = self.agent.isMother
        self.id = id
        self.parent = id.parent() if not self.isMother else None
        self.children = []
        self.next_child = 1

        if fields is not None:
            for key, value, val_type in zip(self.agent.fields.keys(), fields, self.agent.fields_type.values()):
                if type(value) == val_type:
                    self.agent.fields[key] = value

        self.now = 1 # time step counter (Agent perception time)
        self.inbox = Queue()  # Queue for incoming messages

    def initialize(self):
        logging.info(f"{self.id}:: Initializing agent")
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.initialize:
            self.agent.execute_stmt(stmt, local_var, local_var_type)

    def step(self):
        # logging.info(f"Agent {self.id} stepping at time {self.now}") #TODO : remove logging
        self.now += 1

    def destroy(self):
        logging.info(f"{self.id}:: Destroying agent") #TODO : remove logging
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.destroy:
            self.agent.execute_stmt(stmt, local_var, local_var_type)