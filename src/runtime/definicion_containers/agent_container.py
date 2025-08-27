# -*- coding: utf-8 -*- 
# runtime/definicion_containers/agent_container.py
# agent scope is the scope of agents in the system

from typing import Optional, Dict
from core.agent import AgentarAgent
from runtime.errors import AgentNameAlreadyDeclaredError, AgentNotFoundError

class AgentContainer:
    def __init__(self):
        self._agents: Dict[str, AgentarAgent] = {}

    def declare(self, name: str, agent: AgentarAgent):
        if name in self._agents:
            raise AgentNameAlreadyDeclaredError(name, line=agent._line_declaration, first_declaration_line=self._agents[name]._line_declaration)
        self._agents[name] = agent

    def exists(self, name: str) -> bool:
        return name in self._agents

    def get(self, name: str) -> AgentarAgent:
        if name not in self._agents:
            raise AgentNotFoundError(name, line=None)  # TODO: implement the errors with line number
        return self._agents[name]

    def items(self):
        return self._agents.items()

    def __iter__(self):
        return iter(self._agents)
    
    def __repr__(self):
        return f"<Agents declarations: {list(self._agents.keys())}>"