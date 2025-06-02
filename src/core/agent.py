# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

from core.agentid import AgentId

class AgentarAgent:
    def __init__(self):
        self.fields = {}
        self.receive = {}
        self.actions = {}
        self.initialize = []
        self.destroy = []
        
        self.isMother = False
        self.name = None
        self.id = None 
        self.parent = None
        self.children = []
        self.next_child = 1
        self.now = 1

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