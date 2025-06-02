# -*- coding: utf-8 -*- 
# arc/interpreter/AgentarInterpreter.py
# Agentar interpreter class – visits the AST

from interpreter.agenter_builtins import builtins
from core.agent import AgenterAgent
from core.message import AgentarMessage
from ast_tree.nodes import *
from queue import Queue


class AgentInstance:
    def __init__(self, agent_ast, is_mother=False):
        self.agent = AgenterAgent(agent_ast, is_mother)
        self.inbox = Queue()  # Queue for incoming messages

    def receive(self, message: AgentarMessage):
        # Queue incoming message
        self.inbox.append(message)

    def step(self):
        # Process all messages and execute logic
        self.agent.process_messages(self.inbox)
        self.inbox.clear()
        self.agent.execute_step()
