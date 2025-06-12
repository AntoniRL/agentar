# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from runtime.MessageInstance import MessageInstance
from core.agent import AgentarAgent
from core.message import MessageType, get_message_type
from core.agentid import AgentId
from core.agentarTypes import AGENTAR_TYPE_MAP
from ast_tree.nodes import *
from queue import Queue
import logging
import time


class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None, fields = None):
        self.agent = agent_ast
        self.isMother = self.agent.isMother
        self.id = id        
        self.parent = id.parent() if not self.isMother else None
        self.children = []                  # List of agent children [AgentId]
        self.next_child = 1
        self.now = 1                        # time step counter (Agent perception time)
        self.inbox = Queue()                # Queue for incoming messages

        self.runtime = system               # Reference to the AgentarSystem instance
        self.fields = self.agent.fields                   # Agent Instance fields (variables)
        self.fields_type = self.agent.fields_type         # Agent Instance fields types (variables types)

        if fields is not None:
            for key, value, val_type in zip(self.agent.fields.keys(), fields, self.agent.fields_type.values()):
                if type(value) == val_type:
                    self.fields[key] = value
                    self.fields_type[key] = val_type

        self.fields["id"] = self.id   # Set the agent's id in its fields (Make it issier to access)
        self.fields_type["id"] = AgentId


    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.agent.name}', id='{self.id.path}'\n"
            f"</AgentarAgent>"
        )


    def initialize(self):
        logging.info(f"{self.id}:: Initializing agent")
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.initialize:
            self.execute_stmt(stmt, local_var, local_var_type)


    def step(self):
        # logging.info(f"Agent {self.id} stepping at time {self.now}") #TODO : remove logging
        if not self.inbox.empty():
            self.process_messages(self.inbox.get())


    def destroy(self):
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.destroy:
            self.execute_stmt(stmt, local_var, local_var_type)

        with self.runtime._lock:
            if not self.isMother:
                del self.runtime.agents[self.id.path]
                del self.runtime.threads[self.id.path]    

    def execute_action(self, action_name):
        logging.info(f"{self.id.path}:: Executing action...")


    def process_messages(self, message):
        logging.info(f"{self.id.path}:: I received message from {message.sender.path}") # TODO: message.sender to str a nie AgentId
        # comper the name of the message with the agent's receive method
        if message.name in self.agent.receive:
            # Get the corresponding method from the agent's receive method
            receive_method = self.agent.receive[message.name]

            for when_met in receive_method:
                self.when_block(when_met, message)
        else:
            logging.warning(f"{self.id.path}:: No receive method for message '{message.name}' found in agent {self.agent.name}. Ignoring message.")


    def when_block(self, when_node, message):
            local_var = {}
            local_var_type = {}
            for stmt in message.content.items():
                # Initialize local variables from message content
                local_var[stmt[0]] = stmt[1]
                local_var_type[stmt[0]] = type(stmt[1])
            if when_node.conditions == []:
                # If there is no condition, execute the statements directly
                for stmt in when_node.statements:
                    self.execute_stmt(stmt,local_var, local_var_type, message=message)
            else:
                bin_op = self.eval_expr(when_node.conditions, message=message)
                if bin_op:
                    for stmt in when_node.statements:
                        self.execute_stmt(stmt, local_var, local_var_type, message=message)


    def execute_stmt(self, stmt, local_var, local_var_type, message=None):
        # logging.info(f"{self.id.path}:: Executing statement...{stmt}") # TODO: remove logging

        # VariableDeclNode handles variable declarations
        if isinstance(stmt, VariableDeclNode):
            if stmt.value is None:
                local_var[stmt.name] = None
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type)

            elif stmt.value is not None:
                value = self.eval_expr(stmt.value)
                if not AGENTAR_TYPE_MAP[stmt.var_type] == type(value):
                    raise TypeError(f"Type mismatch in variable declaration for {stmt.target}: expected {AGENTAR_TYPE_MAP[stmt.type]}, got {type(value)}")
                local_var[stmt.name] = value
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type)


        # AssignmentNode handles different types of assignments
        elif isinstance(stmt, AssignmentNode):
            if isinstance(stmt.target, SelfAccessNode):
                target = stmt.target.path[1]
                value = self.eval_expr(stmt.value)
                if not self.fields_type[target] == type(value):
                    raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
                self.fields[target] = value
                return 0
            
            elif stmt.index is not None:
                pass # TODO: handle indexed assignment

            elif isinstance(stmt.value, SpawnNode):
                if stmt.target not in local_var_type:
                    raise NameError(f"Variable '{stmt.target}' is not declared.")
                fields = [self.eval_expr(arg) for arg in stmt.value.args] if stmt.value.args else []
                value = self.runtime.spawn_agent(parentInstance = self , agent_type = stmt.value.agent_type, fields = fields)

            elif isinstance(stmt.value, MessageInitNode):
                message = stmt.value
                if message.message_type not in self.runtime.messages_decl:
                    raise NameError(f"Message type '{message.message_type}' is not declared.")
                if self.runtime.messages_decl[message.message_type].content.keys() != message.fields.keys():
                    raise ValueError(f"Message fields do not match declaration for {message.message_type}. Expected {self.runtime.messages_decl[message.message_type].content.keys()}, got {message.fields.keys()}")
                content = {}
                content_type = {}
                for key, val, ref_type in zip(message.fields.keys(), message.fields.values(), self.runtime.messages_decl[message.message_type].content_type.values()):
                    val = self.eval_expr(val)
                    if not isinstance(val, ref_type):
                        raise TypeError(f"Type mismatch in message field '{val}': expected {ref_type}, got {type(val)}")
                    content_type[key] = ref_type
                    content[key] = val
                value = MessageInstance(name=message.message_type, content=content)

            else:
                if stmt.target not in local_var_type:
                    raise NameError(f"Variable '{stmt.target}' is not declared.")
                value = self.eval_expr(stmt.value)
                if not local_var_type[stmt.target] == type(value):
                    raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
            
            local_var[stmt.target] = value


        # SendNode handles sending messages
        elif isinstance(stmt, SendNode):
            logging.info(f"{self.id.path}:: Sending message to {self.eval_expr(stmt.to, local_var, local_var_type)}...")
            msg = self.eval_expr(stmt.message, local_var, local_var_type)
            msg.type = MessageType(stmt.msg_type) if stmt.msg_type else MessageType.INFORM
            msg.sender = self.id
            msg.receiver = self.eval_expr(stmt.to, local_var, local_var_type)
            # TODO: msg.send_time = ...
            self.runtime.send_message(msg)
            

        # print statement
        elif isinstance(stmt, PrintNode):
            to_print = [self.eval_expr(value, local_var, local_var_type, message) for value in stmt.values]
            print(f"AGENT {self.id}::", " ".join(str(v) for v in to_print))
            logging.info(f"{self.id.path}:: (PRINTING) " + " ".join(str(v) for v in to_print))  # TODO: remove logging

        # KillNode handles agent termination
        elif isinstance(stmt, KillNode):
            if self.isMother:
                self.runtime.killMother()
            else:
                self.runtime.killAgent(self.id)

        elif isinstance(stmt, SleepNode):
            duration = self.eval_expr(stmt.duration, local_var, local_var_type)
            logging.info(f"{self.id.path}:: Sleeping for {duration}s...") # TODO: remove logging
            time.sleep(duration)



    def eval_expr(self, expr, local_var=None, local_var_type=None, message=None):
        # TODO: add type checking for local_var and local_var_type
        
        if isinstance(expr, LiteralNode):
            if expr.value == 'inform':
                return MessageType.INFORM
            elif expr.value == 'ask':
                return MessageType.REPLY
            elif expr.value == 'request':
                return MessageType.REQUEST
            elif expr.value == 'confirm':
                return MessageType.CONFIRM
            elif expr.value == 'deny':
                return MessageType.DENY
            else:
                return expr.value
        
        elif isinstance(expr, VarRefNode):
            if expr.name in self.fields:
                return self.fields[expr.name]
            elif expr.name in local_var:
                return local_var[expr.name]
            else:
                raise NameError(f"Variable '{expr.name}' is not declared.")
            
        elif isinstance(expr, SelfAccessNode):
            name = expr.path[1]
            if hasattr(self, name) or name in self.fields:
                return (
                    self.fields[name] if name in self.fields
                    else getattr(self, name) if hasattr(self, name)
                    else None
                )
            else:
                raise NameError(f"Variable '{name}' is not declared.")  
            
        elif isinstance(expr, MsgAccessNode):
            name = expr.path[1]
            if hasattr(message, name) or name in message.content:
                return (
                    message.content[name] if name in message.content
                    else getattr(message, name) if hasattr(message, name)
                    else None
                )
            else:
                raise NameError(f"Variable '{name}' is not declared.")  

        elif isinstance(expr, BinaryOpNode): 
            left = expr.left
            right = expr.right
            operator = expr.op

            if isinstance(left, BinaryOpNode):
                left = self.eval_expr(left, message=message)
            if isinstance(right, BinaryOpNode):
                right = self.eval_expr(right, message=message)

            if not isinstance(left, bool):
                left = self.eval_expr(left, message=message)
            if not isinstance(right, bool):
                right = self.eval_expr(right, message=message)

            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                return left / right
            elif operator == '%':
                return left % right
            elif operator == '**':
                return left ** right
            elif operator == '==':
                return left == right
            elif operator == '!=':
                return left != right
            elif operator == '<':
                return left < right
            elif operator == '<=':
                return left <= right
            elif operator == '>':
                return left > right
            elif operator == '>=':
                return left >= right
            elif operator == 'AND':
                return left and right
            elif operator == 'OR':
                return left or right
            elif operator == 'XOR':
                return left ^ right
            else:
                raise ValueError(f"Unknown operator: {operator}")