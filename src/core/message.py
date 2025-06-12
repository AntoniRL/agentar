# -*- coding: utf-8 -*- 
# src/core/message.py
# Agentar message class – used for communication between agents

from enum import Enum

class MessageType(str, Enum):
    INFORM = "inform"
    ASK = "ask"
    REQUEST = "request"
    CONFIRM = "confirm"
    DENY = "deny"


class AgentarMessage:
    def __init__(self):
        self.name = None
        self.content = {}
        self.content_type = {}

    def __repr__(self):
        return (
            f"<AgentarMessage name='{self.name}' "
            f"content={self.content}>"
        )


def get_message_type(expr):
    mapping = {
        "inform": MessageType.INFORM,
        "ask": MessageType.ASK,  # Zakładam, że chodziło o ASK, a nie REPLY
        "request": MessageType.REQUEST,
        "confirm": MessageType.CONFIRM,
        "deny": MessageType.DENY,
    }
    return mapping.get(expr.value)  # Można dodać domyślną wartość np. .get(expr.value, MessageType.DEFAULT)
