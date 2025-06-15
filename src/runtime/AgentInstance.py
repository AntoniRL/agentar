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
from copy import deepcopy



class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None, fields = None):
        for key, value in agent_ast.__dict__.items():  # Copy all attributes from the agent_AST to the instance
            setattr(self, key, value)
        self.agent = agent_ast
        self.isMother = self.agent.isMother
        self.id = id        
        self.parent = id.parent() if not self.isMother else None
        self.children = []                  # List of agent children [AgentId]
        self.next_child = 1
        self.now = 1                        # time step counter (Agent perception time)
        self.inbox = Queue()                # Queue for incoming messages
        self.isGoalAchieved = False         # Flag to indicate if the agent's goal is achieved        

        self.runtime = system               # Reference to the AgentarSystem instance

        # Initialize agent fields from the agent declaration
        if fields is not None:
            for key, value, val_type in zip(self.agent.fields.keys(), fields, self.agent.fields_type.values()):
                if type(value) == val_type:
                    self.fields[key] = value
                    self.fields_type[key] = val_type

        self.fields["id"] = self.id   # Set the agent's id in its fields (Make it issier to access)
        self.fields_type["id"] = AgentId

        self.return_flag = False  # Flag to indicate if a return statement was executed
        self.break_flag = False   # Flag to indicate if a break statement was executed

    def __repr__(self):
        return (
            f"<AgentarAgent name='{self.agent.name}', id='{self.id.path}'\n"
            f"</AgentarAgent>"
        )


    def initializeAgent(self):
        logging.info(f"{self.id}:: Initializing agent")
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.initialize:          # Execute the agent's initialization statements
            self.execute_stmt(stmt, local_var, local_var_type)


    def step(self):
        self.sense_world()                          # Sense the world and update beliefs
        if not self.inbox.empty():
            self.process_messages(self.inbox.get()) # Process incoming messages (first from the inbox)
        self.check_goals()                          # Check if the agent's goals are achieved
        if not self.isGoalAchieved:                 # If the goal is not achieved, follow rules
            self.follow_rules()


    def destroyAgent(self):
        local_var = {}
        local_var_type = {}
        for stmt in self.agent.destroy:             # Execute the agent's destruction statements
            self.execute_stmt(stmt, local_var, local_var_type)

        with self.runtime._lock:
            if not self.isMother:
                del self.runtime.agents[self.id.path]
                del self.runtime.threads[self.id.path]    

    
    def sense_world(self):
        if self.sense != []:        # If the agent has any sense statements, execute them
            local_var = {}
            local_var_type = {}
            for stmt in self.sense:
                self.execute_stmt(stmt, local_var, local_var_type)


    def process_messages(self, message):
        logging.info(f"{self.id.path}:: Received message from {message.sender.path}")
        # comper the name of the message with the agent's receive method
        if message.name in self.agent.receive:
            # Get the corresponding method from the agent's receive method
            receive_method = self.agent.receive[message.name]

            for when_met in receive_method:          # Iterate over all when blocks in the receive method
                self.when_block(when_met, message)
        else:
            logging.warning(f"{self.id.path}:: No receive method for message '{message.name}' found in agent {self.agent.name}. Ignoring message.")


    def check_goals(self):
        if self.agent.goals == {}:
            self.isGoalAchieved = True
            return
        else:
            for goal, conditions in self.agent.goals.items():
                check_the_condition = self.eval_expr(conditions)  # Evaluate the goal conditions
                if not check_the_condition:  # If the goal conditions are met
                    self.isGoalAchieved = False
                    break
                else:
                    self.isGoalAchieved = True
                    

    def follow_rules(self):
        for rule in self.rules:
            if isinstance(rule, WhenBlockNode):
                self.when_block(rule, None)  # Execute the when block if it exists


    def when_block(self, when_node, message):
            local_var = {}
            local_var_type = {}
            if message is not None:
                for stmt in message.content.items():
                    # Initialize local variables from message content
                    local_var[stmt[0]] = stmt[1]
                    local_var_type[stmt[0]] = type(stmt[1])
            if when_node.conditions == []:
                # If there is no condition, execute the statements directly
                for stmt in when_node.statements:
                    self.execute_stmt(stmt, local_var, local_var_type, message=message)
            else:
                bin_op = self.eval_expr(when_node.conditions, message=message)
                if bin_op:
                    for stmt in when_node.statements:
                        self.execute_stmt(stmt, local_var, local_var_type, message=message)


    def execute_action(self, action_node, variables=None):
        logging.info(f"{self.id.path}:: Executing action '{action_node.name}'...")
        if variables != None:    
            local_var = {}
            local_var_type = {}
            for i, stmt in enumerate(action_node.parameters):
                if type(variables[i]) == AGENTAR_TYPE_MAP.get(stmt.param_type):
                    # Initialize local variables from action parameters
                    local_var[stmt.name] = variables[i]
                    local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.param_type)
                else:
                    raise TypeError(f"Type mismatch in action parameter '{stmt.name}': expected {AGENTAR_TYPE_MAP.get(stmt.param_type)}, got {type(variables[i])}")
        return_type = action_node.return_type
        if return_type == "void":
            for stmt in action_node.body:
                self.execute_stmt(stmt, local_var, local_var_type)
        if return_type != "void":
            for stmt in action_node.body:
                if self.return_flag:
                    self.return_flag = False
                    break
                to_return =  self.execute_stmt(stmt, local_var, local_var_type)
            return to_return


    def check_goal(self, stmt, local_var, local_var_type):
        goal_to_check = stmt.goal_name
        if goal_to_check in self.agent.goals:
            conditions = self.goals[goal_to_check]
            check_the_condition = self.eval_expr(conditions, local_var, local_var_type)
            if check_the_condition:
                return True
            else:
                return False
        else:
            raise NameError(f"Goal '{goal_to_check}' is not declared.")



    def execute_stmt(self, stmt, local_var, local_var_type, message=None):
        # logging.info(f"{self.id.path}:: Executing statement...{stmt}") # TODO: remove logging

        # VariableDeclNode handles variable declarations
        if isinstance(stmt, VariableDeclNode):
            if stmt.value is None:
                local_var[stmt.name] = None
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type)

            elif stmt.value is not None:
                value = self.eval_expr(stmt.value, local_var, local_var_type, message=message)
                if not AGENTAR_TYPE_MAP[stmt.var_type] == type(value):
                    raise TypeError(f"Type mismatch in variable declaration for {stmt.name}: expected {AGENTAR_TYPE_MAP[stmt.var_type]}, got {type(value)}")
                local_var[stmt.name] = value
                local_var_type[stmt.name] = AGENTAR_TYPE_MAP.get(stmt.var_type) 
                

        # AssignmentNode handles different types of assignments
        elif isinstance(stmt, AssignmentNode):
            if isinstance(stmt.target, SelfAccessNode):
                target = stmt.target.path[1]
                value = self.eval_expr(stmt.value, local_var, local_var_type, message=message)
                if stmt.index is None:
                    if not self.fields_type[target] == type(value):
                        raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
                    self.fields[target] = value
                elif stmt.index == "add":
                    if not self.fields_type[target] == list:
                        raise TypeError(f"Type mismatch in assignment to {target}: expected list, got {type(self.fields[target])}")
                    self.fields[target].append(value)
                elif isinstance(stmt.index, IndexRangeNode):
                    pass # TODO: handle index range assignment
                else: 
                    if not self.fields_type[target] == list:
                        raise TypeError(f"Type mismatch in assignment to {target}: expected list, got {type(self.fields[target])}")
                    index = self.eval_expr(stmt.index, local_var, local_var_type)
                    self.fields[target][index] = value
                return 0
            
            elif stmt.index is not None:
                target = stmt.target
                value = self.eval_expr(stmt.value, local_var, local_var_type)
                if stmt.index == "add":
                    local_var[target].append(value)
                else:
                    index = self.eval_expr(stmt.index, local_var, local_var_type)
                    local_var[target][index] = value
                return 0

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

            # When do action return a value 
            elif isinstance(stmt.value, DoNode):
                value = self.execute_stmt(stmt.value, local_var, local_var_type, message=message)
            
            elif isinstance(stmt.value, GoalCheckNode):
                value = self.check_goal(stmt.value, local_var, local_var_type)

            else:
                if stmt.target not in local_var_type:
                    raise NameError(f"Variable '{stmt.target}' is not declared.")
                value = self.eval_expr(stmt.value, local_var, local_var_type, message=message)
                if not local_var_type[stmt.target] == type(value):
                    raise TypeError(f"Type mismatch in assignment to {target}: expected {self.fields_type[target]}, got {type(value)}")
            
            local_var[stmt.target] = value
        # end of AssignmentNode ----

        # SendNode handles sending messages
        elif isinstance(stmt, SendNode):
            msg = self.eval_expr(stmt.message, local_var, local_var_type)
            msg.type = MessageType(stmt.msg_type) if stmt.msg_type else MessageType.INFORM
            msg.sender = self.id
            if stmt.to == "PARENT":
                msg.receiver = self.parent
            else:
                msg.receiver = self.eval_expr(stmt.to, local_var, local_var_type)
            # TODO: msg.send_time = ...
            self.runtime.send_message(msg)


        # SendToChildrenNode handles sending messages to children
        elif isinstance(stmt, SendToChildrenNode):
            msg = self.eval_expr(stmt.message, local_var, local_var_type)
            msg.type = MessageType(stmt.msg_type) if stmt.msg_type else MessageType.INFORM
            msg.sender = self.id
            # TODO: msg.send_time = ...
            agent_type = stmt.agent_type.name
            agent_type = agent_type if agent_type in self.runtime.agents_decl else "_"
            # Prepare the message to be sent to children
            msg_to_send = []
            with self.runtime._lock:
                for child in self.children:
                    if agent_type != "_" and agent_type == self.runtime.agents[child].name:
                        new_msg = deepcopy(msg)
                        new_msg.receiver = AgentId(child)
                        msg_to_send.append(new_msg)
                    elif agent_type == "_":
                        new_msg = deepcopy(msg)
                        new_msg.receiver = AgentId(child)
                        msg_to_send.append(new_msg)

            for msg in msg_to_send:
                self.runtime.send_message(msg)


        elif isinstance(stmt, SendToSiblingsNode):
            msg = self.eval_expr(stmt.message, local_var, local_var_type)
            msg.type = MessageType(stmt.msg_type) if stmt.msg_type else MessageType.INFORM
            msg.sender = self.id
            # TODO: msg.send_time = ...
            agent_type = stmt.agent_type.name
            agent_type = agent_type if agent_type in self.runtime.agents_decl else "_"
            # Prepare the message to be sent to children
            msg_to_send = []
            with self.runtime._lock:
                for child in self.runtime.agents[self.parent.path].children:
                    if child == self.id.path:  # Skip sending message to self
                        continue
                    if agent_type != "_" and agent_type == self.runtime.agents[child].name:
                        new_msg = deepcopy(msg)
                        new_msg.receiver = AgentId(child)
                        msg_to_send.append(new_msg)
                    elif agent_type == "_":
                        new_msg = deepcopy(msg)
                        new_msg.receiver = AgentId(child)
                        msg_to_send.append(new_msg)

            for msg in msg_to_send:
                self.runtime.send_message(msg)
            

        # print statement
        elif isinstance(stmt, PrintNode):
            to_print = [self.eval_expr(value, local_var, local_var_type, message) for value in stmt.values]
            # make printing id of AgentId objects more readable
            for i, value in enumerate(to_print):
                if type(value) is list:
                    for j, val in enumerate(value):
                        if type(val) == AgentId:
                            to_print[i][j] = val.path                
            print(f"AGENT {self.id}::", " ".join(str(v) for v in to_print))
            logging.info(f"{self.id.path}:: (PRINTING) " + " ".join(str(v) for v in to_print))


        # KillNode handles agent termination
        elif isinstance(stmt, KillNode):
            if stmt.agent_id is not None:
                agent_id = self.eval_expr(stmt.agent_id, local_var, local_var_type)
                self.runtime.killAgent(agent_id)
            else:
                if self.isMother:
                    self.runtime.killMother()
                else:
                    self.runtime.killAgent(self.id)


        # SllepNode handles sleeping for a specified duration
        elif isinstance(stmt, SleepNode):
            duration = self.eval_expr(stmt.duration, local_var, local_var_type)
            logging.info(f"{self.id.path}:: Sleeping for {duration}s...")
            time.sleep(duration)


        # DoNode handles executing actions
        elif isinstance(stmt, DoNode):
            logging.info(f"{self.id.path}:: Executing action '{stmt.name}'")
            if stmt.name in self.agent.actions:
                variables = []
                for param in stmt.variables:
                    variables.append(self.eval_expr(param))
                action = self.agent.actions[stmt.name]
                if isinstance(action, ActionNode):
                    if action.return_type == "void":
                        self.execute_action(action, variables)
                    else:
                        return self.execute_action(action, variables)


        # ReturnNode handles returning values from actions        
        elif isinstance(stmt, ReturnNode):
            if stmt.value is not None:
                self.return_flag = True
                return self.eval_expr(stmt.value, local_var, local_var_type, message=message)
            else:
                return None


        # IfStmtNode handles conditional statements
        elif isinstance(stmt, IfStmtNode):
            condition = self.eval_expr(stmt.conditions, local_var, local_var_type)
            if condition:
                for statement in stmt.statements:
                    self.execute_stmt(statement, local_var, local_var_type)
            else:
                if stmt.elseStmt is not None:
                    for statement in stmt.elseStmt.statements:
                        self.execute_stmt(statement, local_var, local_var_type)

        
        # ForLoopNode handles for loops
        elif isinstance(stmt, ForLoopNode):
            self.execute_stmt(stmt.initialize, local_var, local_var_type)
            def check_condition():
                return self.eval_expr(stmt.condition, local_var, local_var_type)
            def update_loop_var():
                self.execute_stmt(stmt.update, local_var, local_var_type)
            while check_condition() and not self.break_flag:
                for statement in stmt.body:
                    self.execute_stmt(statement, local_var, local_var_type)
                update_loop_var()
            self.break_flag = False  # Reset break flag after loop execution


        elif isinstance(stmt, WhileLoopNode):
            def check_condition():
                return self.eval_expr(stmt.condition, local_var, local_var_type)
            while check_condition() and not self.break_flag:
                for statement in stmt.body:
                    self.execute_stmt(statement, local_var, local_var_type)
            self.break_flag = False  # Reset break flag after loop execution


        elif isinstance(stmt, BreakNode):
            self.break_flag = True


        elif isinstance(stmt, SenseNode):
            self.sense_world()  # Sense the world and update beliefs

    
        elif isinstance(stmt, KillChildrenNode):
            agent_type = stmt.agent_type.name if stmt.agent_type is not None else None
            self.runtime.killChildren(self.id, agent_type)  # Kill all children of the agent with the specified type



# ---EVAL_EXPR-----------------------------------
    def eval_expr(self, expr, local_var=None, local_var_type=None, message=None):
        # TODO: add type checking for local_var and local_var_type

        if isinstance(expr, LiteralNode):
            if expr.value == 'inform':
                return MessageType.INFORM
            elif expr.value == 'ask':
                return MessageType.ASK
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
            elif expr.name == "_":
                return "_"
            else:
                raise NameError(f"Variable '{expr.name}' is not declared.")
            
        elif isinstance(expr, IndexAccessNode):
            base = self.eval_expr(expr.base, local_var, local_var_type, message=message)
            index = self.eval_expr(expr.index, local_var, local_var_type, message=message)
            if index < 0 or index >= len(base):
                raise IndexError(f"Index {index} out of bounds for list of length {len(base)}.")
            return base[index]
        

        elif isinstance(expr, SliceAccessNode):
            base = self.eval_expr(expr.base, local_var, local_var_type, message=message)
            start = self.eval_expr(expr.start, local_var, local_var_type, message=message) if expr.start is not None else None
            end = self.eval_expr(expr.end, local_var, local_var_type, message=message) if expr.end is not None else None
            if start is not None and (start < 0 or start >= len(base)):
                raise IndexError(f"Start index {start} out of bounds for list of length {len(base)}.")
            if end is not None and (end < -len(base) or end > len(base)):
                raise IndexError(f"End index {end} out of bounds for list of length {len(base)}.")
            return base[start:end] if start is not None and end is not None else base[start:] if start is not None else base[:end] if end is not None else base

            
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

        elif isinstance(expr, BelAccessNode):
            name = expr.path[1]
            if name in self.beliefs:
                return (self.beliefs[name])
            else:
                raise NameError(f"Variable '{name}' is not declared.") 
            
        elif isinstance(expr, ListLiteralNode):
            return [self.eval_expr(item, local_var, local_var_type) for item in expr.elements]

        elif isinstance(expr, BinaryOpNode): 
            left = expr.left
            right = expr.right
            operator = expr.op

            if isinstance(left, BinaryOpNode):
                left = self.eval_expr(left, local_var, local_var_type, message=message)
            if isinstance(right, BinaryOpNode):
                right = self.eval_expr(right, local_var, local_var_type, message=message)

            if not isinstance(left, bool):
                left = self.eval_expr(left, local_var, local_var_type, message=message)
            if not isinstance(right, bool):
                right = self.eval_expr(right, local_var, local_var_type, message=message)

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