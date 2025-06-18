# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

class AgentarAgent:
    def __init__(self):
        self._fields = {}
        self._fields_type = {}
        self._beliefs = {}
        self._beliefs_type = {}
        self._sense = []
        self._sub_goals = {}
        self._merge_goals_condition = None
        self._rules = []
        self._receive = {}
        self._actions = {}
        self._initialize = []
        self._destroy = []
        
        self._isMother = False
        self._name = None

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self._name}'\n"
            f"  Fields: {list(self._fields.keys())}\n"
            f"  Actions: {list(self._actions.keys())}\n"
            f"  Receive handlers: {list(self._receive.keys())}\n"
            f"</AgentarAgent>"
        )