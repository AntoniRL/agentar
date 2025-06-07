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
