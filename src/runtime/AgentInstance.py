# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from runtime.Agentar_builtins import builtins
from core.agent import AgentarAgent
from core.message import AgentarMessage
from core.agentid import AgentId
from ast_tree.nodes import *
from queue import Queue


class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, id: AgentId = None, fields = None):
        self.agent = agent_ast
        self.isMother = self.agent.isMother
        self.id = id
        self.parent = id.parent() if not self.isMother else None
        self.children = []
        self.next_child = 1

        if fields is not None:
            for key, value in zip(self.agent.fields.keys(), fields):
                self.agent.fields[key] = value

        self.now = 1 # time step counter (Agent perception time)
        self.inbox = Queue()  # Queue for incoming messages

    def step(self):
        pass

    def receive_msg(self, message: AgentarMessage):
        pass

    def spawn_child(self, agent_ast):
        pass
