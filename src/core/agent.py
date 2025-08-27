# -*- coding: utf-8 -*- 
# src/core/agent.py
# Agentar agent class – the main class for running the Agentar interpreter

from runtime.definicion_containers.variable_container import VariableContainer
from runtime.definicion_containers.ASTNode_container import ASTNodeContainer

class AgentarAgent:
    def __init__(self):
        self._fields = VariableContainer(agent=None, scope="Fields")
        self._beliefs = VariableContainer(agent=None, scope="Beliefs")
        self._sense = []
        self._sub_goals = ASTNodeContainer("Goal")
        self._merge_goals_condition = None
        self._rules = []
        self._receive = ASTNodeContainer("ReceiveHandler")
        self._actions = ASTNodeContainer("Action")
        self._initialize = []
        self._destroy = []
        
        self._isMother = False
        self._name = None

        self._line_declaration = None

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self._name}'\n"
            f"  Fields: {list(self._fields)}\n"
            f"  Actions: {list(self._actions)}\n"
            f"  Receive handlers: {list(self._receive)}\n"
            f"</AgentarAgent>"
        )