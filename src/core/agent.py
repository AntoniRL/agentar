# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

class AgentarAgent:
    def __init__(self):
        self.fields = {}
        self.fields_type = {}
        self.beliefs = {}
        self.beliefs_type = {}
        self.goles = {}
        self.rules = {}
        self.receive = {}
        self.actions = {}
        self.initialize = []
        self.destroy = []
        
        self.isMother = False
        self.name = None

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.name}'\n"
            f"  Fields: {list(self.fields.keys())}\n"
            f"  Actions: {list(self.actions.keys())}\n"
            f"  Receive handlers: {list(self.receive.keys())}\n"
            f"</AgentarAgent>"
        )