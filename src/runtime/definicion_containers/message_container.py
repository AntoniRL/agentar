# -*- coding: utf-8 -*- 
# runtime/definicion_containers/message_container.py
# message scope is the scope of messages in the agent instance

from typing import Optional, Dict
from core.message import AgentarMessage
from runtime.errors import MessageAlreadyDeclaredError, MessageNotFoundError

class MessageContainer:
    def __init__(self):
        self._messages: Dict[str, AgentarMessage] = {}

    def declare(self, name: str, message: AgentarMessage):
        if name in self._messages:
            raise MessageAlreadyDeclaredError(name, line=message._line_declaration, first_declaration_line=self._messages[name]._line_declaration)
        self._messages[name] = message

    def exists(self, name: str) -> bool:
        return name in self._messages

    def get(self, name: str) -> AgentarMessage:
        if name not in self._messages:
            raise MessageNotFoundError(name, line=None)  # TODO: implement the errors with line number
        return self._messages[name]

    def items(self):
        return self._messages.items()

    def __iter__(self):
        return iter(self._messages)

    def __repr__(self):
        return f"<Messages declarations:{list(self._messages.keys())}>"