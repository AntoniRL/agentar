# -*- coding: utf-8 -*- 
# src/core/message.py
# Agentar message class – used for communication between agents

from enum import Enum
from runtime.definicion_containers.variable_container import VariableContainer


class MessageType(str, Enum):
    INFORM = "inform"
    ASK = "ask"
    REQUEST = "request"
    CONFIRM = "confirm"
    DENY = "deny"


class AgentarMessage:
    def __init__(self):
        self._name = None
        self._content = VariableContainer()

        self._line_declaration = None

    def __repr__(self):
        return (
            f"<AgentarMessage name='{self._name}' "
            f"content={self._content}>"
        )


def get_message_type(expr):
    mapping = {
        "inform": MessageType.INFORM,
        "ask": MessageType.ASK,
        "request": MessageType.REQUEST,
        "confirm": MessageType.CONFIRM,
        "deny": MessageType.DENY,
    }
    return mapping.get(expr.value)
