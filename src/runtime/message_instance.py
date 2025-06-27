# -*- coding: utf-8 -*- 
# runtime/MessageInstance.py
# MessageInstance: represents a single message in the Agentar system

from core.message import AgentarMessage, MessageType
from core.agent_id import AgentId
from copy import deepcopy


class MessageInstance():
    def __init__(self, name: str, content: dict = None, content_type: dict = None):
        self._name = name                    # np. 'clean_room'
        self._sender: AgentId = None         # AgentId('.1')
        self._receiver: AgentId = None       # AgentId('.1.2')
        self._type = MessageType.INFORM      # np. MessageType.REQUEST
        self._content = content or {}        # np. {'task': 3, 'value': 1.2}
        self._content_type = content_type or {}    # np. {'task': int, 'value': float}
        self._sending_time = 0                  # czas systemowy

    def __repr__(self):
        return (
            f"<MessageInstance name='{self._name}' "
            f"type={self._type} from={self._sender} to={self._receiver} "
            f"time={self._sending_time} content={self._content}>"
        )