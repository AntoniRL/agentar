# -*- coding: utf-8 -*- 
# runtime/MessageInstance.py
# MessageInstance: represents a single message in the Agentar system

from core.message import AgentarMessage, MessageType
from core.agentid import AgentId


class MessageInstance():
    def __init__(self, name: str, content: dict = None):
        self.name = name                    # np. 'clean_room'
        self.sender: AgentId = None         # AgentId('.1')
        self.receiver: AgentId = None       # AgentId('.1.2')
        self.type = MessageType.INFORM      # np. MessageType.REQUEST
        self.content = content or {}        # np. {'task': 3, 'value': 1.2}
        self.content_type = {}              # np. {'task': int, 'value': float}
        self.send_time = 0                  # czas systemowy

    def __repr__(self):
        return (
            f"<MessageInstance name='{self.name}' "
            f"type={self.type} from={self.sender} to={self.receiver} "
            f"time={self.send_time} content={self.content}>"
        )