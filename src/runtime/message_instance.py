# -*- coding: utf-8 -*- 
# runtime/MessageInstance.py
# MessageInstance: represents a single message in the Agentar system

from core.agent_id import AgentId
from copy import deepcopy


class MessageInstance():
    def __init__(self, name: str, content = None):
        self._name = name                    # np. 'clean_room'
        self._sender: AgentId = None         # AgentId('.1')
        self._receiver: AgentId = None       # AgentId('.1.2')
        self._type = None                    # np. MessageType.REQUEST
        self._content = content or None        
        self._sending_time = 0                  # czas systemowy


    def __repr__(self):
        return (
            f"<MessageInstance name='{self._name}' "
            f"msgType={self._type} from={self._sender} to={self._receiver} "
            f"time={self._sending_time} content={self._content}>"
        )