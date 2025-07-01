# -*- coding: utf-8 -*-
# runtime/agent_instance/message_handler.py
# MessageHandler: handles messages in the context of an agent instance

import logging

from runtime.definicion_containers.variable_container import VariableContainer
from runtime.errors import *
from ast_tree.nodes import AddressOfExprNode
from copy import deepcopy
from runtime.message_instance import MessageInstance

class MessageHandler:
    def __init__(self, agent):
        self.agent = agent




    def send_message(self, stmt,  message): 
        pass


    def process_messages(self, message):
        logging.info(f"{self.agent._id.path}:: Received message from {message._sender.path}")
        if self.agent._receive.exists(message._name):
            receive_method = self.agent._receive.get(message._name, message._line)
            for when_method in receive_method:
                self.agent._action_executor.when_block(when_method, "Receive", message)
        else:
            logging.warning(f"{self.agent._id.path}:: No receive method for message '{message._name}' found in agent {self.agent._name}. Ignoring message.")


    def handle_message_init(self, msg_node):
        message_type = msg_node.message_type
        if not self.agent._runtime.messages_decl.exists(message_type):
            raise ASTNodeNotFoundError(message_type, "Message declaration", msg_node._line)
        
        message_init_content = msg_node.fields
        mess_decl = self.agent._runtime.messages_decl.get(message_type, msg_node._line)
        new_content = deepcopy(mess_decl._content)
        if len(message_init_content) != len(new_content._variables):
            raise MismatchMessageContentError(message_type, len(message_init_content), len(new_content), msg_node._line)
        for name, (new_name, new_value) in zip(new_content._variables.keys(), message_init_content.items()):
            if name != new_name:
                raise MismatchMessageContentError(message_type, name, new_name, msg_node._line)
            if not isinstance(new_value, AddressOfExprNode):
                new_value = deepcopy(new_value)
            new_content.set(name, new_value, msg_node._line)
        message_instance = MessageInstance(message_type, new_content) 
        return message_instance
    

    def handle_message_declaration(self, msg_decl_node, local_vars):
        message_type = msg_decl_node.message_type
        if not self.agent._runtime.messages_decl.exists(message_type):
            raise ASTNodeNotFoundError(message_type, "Message declaration", msg_decl_node._line)
        if message_type != msg_decl_node.message.message_type:
            raise MismatchTypeWithDeclarationError(message_type, msg_decl_node.message.message_type, msg_decl_node._line)
        message_instance = self.handle_message_init(msg_decl_node.message)
        # TODO: How to handle the message instance in the local variables?
        local_vars.declare(msg_decl_node.name, message_instance, "Mess", msg_decl_node._line)