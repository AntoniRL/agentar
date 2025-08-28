# -*- coding: utf-8 -*-
# runtime/agent_instance/message_handler.py
# MessageHandler: handles messages in the context of an agent instance

import logging
from copy import deepcopy


from runtime.definicion_containers.variable_container import VariableContainer
from runtime.errors import *
from ast_tree.nodes import AddressOfExprNode
from runtime.message_instance import MessageInstance
from core.agentar_types import MessageType
from core.pointer import Pointer

class MessageHandler:
    def __init__(self, agent):
        self.agent = agent


    def handle_message_init(self, msg_node, local_vars):
        message_type = msg_node.message_type
        
        message_init_content = msg_node.fields
        mess_decl = self.agent._runtime.messages_decl.get(message_type, msg_node._line)
        new_content = deepcopy(mess_decl._content)
        if len(message_init_content) != len(new_content._variables):
            raise MismatchMessageContentError(message_type, len(message_init_content), len(new_content), msg_node._line)
        for name, (new_name, new_value) in zip(new_content._variables.keys(), message_init_content.items()):
            if name != new_name:
                raise MismatchMessageContentError(message_type, name, new_name, msg_node._line)
            new_value = self.agent._evaluator.eval_expr(new_value, local_vars)  # Evaluate the expression to get the value
            if not isinstance(new_value, Pointer):
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
        local_vars.declare(msg_decl_node.name, msg_decl_node.message, MessageInstance, msg_decl_node._line)


    def send_message(self, stmt,  local_vars): 
        msg = self.agent._evaluator.eval_expr(stmt.message, local_vars)
        # --- Create a deep copy of the message to avoid modifying the original message. It helps to prevent issues with shared references.
        content = msg._content
        msg._content = VariableContainer()
        msg = deepcopy(msg)
        msg._content = content
        # ---
        # TODO: msg._sending_time = ...
        msg._type = MessageType(stmt.msg_type)
        msg._sender = self.agent._id
        if stmt.to == "PARENT":
            msg._receiver = self.agent._parent
        else:
            msg._receiver = self.agent._evaluator.eval_expr(stmt.to, local_vars)
        self.agent._runtime.send_message(msg)


    def send_to_children(self, stmt, local_vars):
        msg = self.agent._evaluator.eval_expr(stmt.message, local_vars)
        # --- Create a deep copy of the message to avoid modifying the original message. It helps to prevent issues with shared references.
        content = msg._content
        msg._content = VariableContainer()
        msg = deepcopy(msg)
        msg._content = content
        # ---
        msg._type = MessageType(stmt.msg_type)
        msg._sender = self.agent._id
        agent_type = stmt.agent_type.name
        agent_type = agent_type if agent_type in self.agent._runtime.agents_decl else "_"
        # Prepare the message to be sent to children
        msg_to_send = []
        with self.agent._runtime._lock:
            for child in self.agent._children:
                if agent_type != "_" and agent_type == self.agent._runtime.agents[child.path]._name:
                    new_msg = deepcopy(msg)
                    new_msg._content = content # Restore the content after deepcopy
                    new_msg._receiver = child
                    msg_to_send.append(new_msg)
                elif agent_type == "_":
                    new_msg = deepcopy(msg)
                    new_msg._content = content
                    new_msg._receiver = child
                    msg_to_send.append(new_msg)

        for msg in msg_to_send:
            self.agent._runtime.send_message(msg)


    def send_to_siblings(self, stmt, local_vars):
        msg = self.agent._evaluator.eval_expr(stmt.message, local_vars)
        # --- Create a deep copy of the message to avoid modifying the original message. It helps to prevent issues with shared references.
        content = msg._content
        msg._content = VariableContainer()
        msg = deepcopy(msg)
        msg._content = content
        # ---
        msg._type = MessageType(stmt.msg_type)
        msg._sender = self.agent._id
        agent_type = stmt.agent_type.name
        agent_type = agent_type if agent_type in self.agent._runtime.agents_decl else "_"
        # Prepare the message to be sent to children
        msg_to_send = []
        with self.agent._runtime._lock:
            for child in self.agent._runtime.agents[self.agent._parent.path]._children:
                if agent_type != "_" and agent_type == self.agent._runtime.agents[child.path]._name:
                    new_msg = deepcopy(msg)
                    new_msg._content = content # Restore the content after deepcopy
                    new_msg._receiver = child
                    msg_to_send.append(new_msg)
                elif agent_type == "_":
                    new_msg = deepcopy(msg)
                    new_msg._content = content
                    new_msg._receiver = child
                    msg_to_send.append(new_msg)

        for msg in msg_to_send:
            self.agent._runtime.send_message(msg)


    def process_messages(self, message):
        logging.info(f"{self.agent._id.path}:: Received message from {message._sender.path}")
        if self.agent._receive.exists(message._name):
            receive_method = self.agent._receive.get(message._name, line=None)
            for when_method in receive_method:
                local_vars = VariableContainer(agent=self.agent, scope="Receive")
                self.agent._action_executor.when_block(when_method, local_vars, message)
        else:
            logging.warning(f"{self.agent._id.path}:: No receive method for message '{message._name}' found in agent {self.agent._name}. Ignoring message.")


