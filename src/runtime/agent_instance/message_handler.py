# -*- coding: utf-8 -*-
# runtime/agent_instance/message_handler.py
# MessageHandler: handles messages in the context of an agent instance


class MessageHandler:
    def __init__(self, agent):
        self.agent = agent

    def process_messages(self, message):
        pass

    def handle_message_init(self, msg_node):
        pass