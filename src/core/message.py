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
        self.sender = None
        self.receiver = None
        self.type = MessageType.INFORM
        self.content = {}
        self.send_time = None

    def __repr__(self):
        return (
            f"<AgentarMessage name='{self.name}' "
            f"from={self.sender} to={self.receiver} "
            f"type={self.type} time={self.send_time} "
            f"content={self.content}>"
        )
