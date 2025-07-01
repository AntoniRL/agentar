# -*- coding: utf-8 -*- 
# src/core/message.py
# Agentar message class – used for communication between agents

from enum import Enum
from runtime.definicion_containers.variable_container import VariableContainer


class AgentarMessage:
    def __init__(self):
        self._name = None
        self._content = VariableContainer(f"Message")

        self._line_declaration = None

    def __repr__(self):
        return (
            f"<AgentarMessage name='{self._name}' "
            f"content={self._content}>"
        )
