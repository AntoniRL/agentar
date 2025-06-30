# -*- coding: utf-8 -*-
# runtime/agent_instance/message_handler.py
# MessageHandler: handles messages in the context of an agent instance

import logging

from runtime.definicion_containers.variable_container import VariableContainer


class MessageHandler:
    def __init__(self, agent):
        self.agent = agent

    def process_messages(self, message):
        logging.info(f"{self.agent._id.path}:: Received message from {message._sender.path}")
        if self.agent._receive.exists(message._name):
            receive_method = self.agent._receive.get(message._name, message._line)
            for when_method in receive_method:
                self.agent._action_executor.when_block(when_method, "Receive", message)
        else:
            logging.warning(f"{self.agent._id.path}:: No receive method for message '{message._name}' found in agent {self.agent._name}. Ignoring message.")