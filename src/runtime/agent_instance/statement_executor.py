# -*- coding: utf-8 -*-
# runtime/agent_instance/statement_executor.py
# StatementExecutor: executes statements in the context of an agent instance


import logging

from ast_tree.nodes import *
from core.agent_id import AgentId
from runtime.errors import *
from core.agentar_types import resolve_type
from runtime.definicion_containers.variable_container import VariableContainer

class StatementExecutor:
    def __init__(self, agent):
        self.agent = agent

    def execute_stmt(self, stmt, local_vars, message=None):
        match stmt:
            case VariableDeclNode(var_type=var_type, name=var_name, value=value_expr, _line=line):
                self.variable_declaration(local_vars, var_name, value_expr, var_type, line)

            case PrintNode() | LoggingNode():
                self.print_stmt(stmt, local_vars, message, stmt._line)
            
            case AssignmentNode():
                self.handle_assignment(stmt, local_vars, message)

            case MessageVarDeclNode():
                self.agent._message_handler.handle_message_declaration(stmt, local_vars)

            case SpawnNode():
                print(stmt)

            case DoNode():
                action_node = self.agent._actions.get(stmt.name, stmt._line)
                parameters = [self.agent._evaluator.eval_expr(param, local_vars, message, stmt._line) for param in stmt.variables]
                return self.agent._action_executor.execute_action(action_node, parameters, stmt._line)

            case GoalCheckNode():
                return self.agent._action_executor.goal_check(stmt, local_vars)

            case GetTimeNode():
                print(stmt)

            case ReturnNode():
                self.agent._return_flag = True
                return self.agent._evaluator.eval_expr(stmt.value, local_vars, message, stmt._line)
            
            case SendNode():
                self.agent._message_handler.send_message(stmt, local_vars)




# ------------------------------------------
#  Extra methods for handling specific statements
# ------------------------------------------

    def variable_declaration(self, local_vars, var_name, value_expr, var_type, line):
        local_vars.declare(var_name, value_expr, var_type, line)


    def print_stmt(self, stmt, local_vars, message, line): 
        value = stmt.values
        to_print = [self.agent._evaluator.eval_expr(value, local_vars, message, line) for value in value]
        # make printing id of AgentId objects more readable
        for i, value in enumerate(to_print):
            if type(value) is list:
                for j, val in enumerate(value):
                    if type(val) == AgentId:
                        to_print[i][j] = val.path   
        if isinstance(stmt, PrintNode):
            print(f"AGENT {self.agent._id.path}::", " ".join(str(v) for v in to_print))
            logging.info(f"{self.agent._id.path}:: (PRINTING) " + " ".join(str(v) for v in to_print))
        else: 
            logging.info(f"{self.agent._id.path}:: (LOGGING) " + " ".join(str(v) for v in to_print))


    

    # ---- Handle assignment 
    def handle_assignment(self, stmt, local_vars, message=None):
        if isinstance(stmt.value, (SpawnNode, DoNode, GoalCheckNode, GetTimeNode)):
            value = self.execute_stmt(stmt.value, local_vars, message)
        else:
            value = self.agent._evaluator.eval_expr(stmt.value, local_vars, message, stmt._line)

        self.assign_to_target(stmt.target, value, local_vars, message, stmt._line)


    def assign_to_target(self, target_node, value, local_vars, message, line):
        match target_node:
            case VarRefNode(name=name):
                local_vars.set(name, value, line)

            case IndexAccessNode(base=base, index=index):
                container = self._resolve_container(base, local_vars, message, line)
                index_value = self.agent._evaluator.eval_expr(index, local_vars, message, line)
                self._validate_index_assignment(container, index_value, value, line)
                container[index_value] = value

            case SliceAccessNode(base=base, start=start, end=end):
                container = self._resolve_container(base, local_vars, message, line)
                start_value = self.agent._evaluator.eval_expr(start, local_vars, message, line) if start else 0
                end_value = self.agent._evaluator.eval_expr(end, local_vars, message, line) if end else None
                self._validate_slice_assignment(container, start_value, value, line)
                container[start_value:end_value] = value

            case SelfAccessNode(path=path):
                target_name = path[1]
                self.agent._fields.set(target_name, value, line)

            case BelAccessNode(path=path):
                target_name = path[1]
                self.agent._beliefs.set(target_name, value, line)

            case _:
                raise AgentarRuntimeError(f"Unsupported assignment target: {target_node}", line)
            

    def _resolve_container(self, base_node, local_vars, message, line):
        match base_node:
            case VarRefNode(name=name):
                return local_vars.get(name, line)
            case IndexAccessNode(base=base, index=index):
                parent_container = self._resolve_container(base, local_vars, message, line)
                index_value = self.agent._evaluator.eval_expr(index, local_vars, message, line)
                self._validate_index_access(parent_container, index_value, line)
                return parent_container[index_value]
            case SelfAccessNode(path=path):
                return self.agent._fields.get(path[1], line)
            case BelAccessNode(path=path):
                return self.agent._beliefs.get(path[1], line)
            case _:
                return self.agent._evaluator.eval_expr(base_node, local_vars, message, line)
            

    def _validate_index_assignment(self, container, index, value, line):
        if not hasattr(container, '__getitem__') or not hasattr(container, '__setitem__'):
            raise AgentarRuntimeError(f"Object of type {type(container).__name__} does not support item assignment", line)
        if isinstance(container, tuple):
            raise AgentarRuntimeError(f"Tuple object does not support item assignment", line)
        if isinstance(container, list):
            if not isinstance(index, int):
                raise AgentarRuntimeError(f"List indices must be integers, not {type(index).__name__}", line)
            if index >= len(container) or index < -len(container):
                raise AgentarRuntimeError(f"List index {index} out of range for list of length {len(container)}", line)
        elif isinstance(container, dict):
            try:
                hash(index)
            except TypeError:
                raise AgentarRuntimeError(f"Unhashable type: '{type(index).__name__}' cannot be used as dictionary key", line)
        elif isinstance(container, str):
            raise AgentarRuntimeError(f"String object does not support item assignment", line)
        elif not hasattr(container, '__setitem__'):
            raise AgentarRuntimeError(f"Object of type {type(container).__name__} does not support item assignment", line)
        

    def _validate_index_access(self, container, index, line):        
        if not hasattr(container, '__getitem__'):
            raise AgentarRuntimeError(f"Object of type {type(container).__name__} is not subscriptable", line)
        if isinstance(container, (list, tuple)):
            if not isinstance(index, int):
                raise AgentarRuntimeError(f"List/tuple indices must be integers, not {type(index).__name__}", line)
            if index >= len(container) or index < -len(container):
                raise AgentarRuntimeError(f"Index {index} out of range for {type(container).__name__} of length {len(container)}", line)
        elif isinstance(container, dict):
            if index not in container:
                raise AgentarRuntimeError(f"Key '{index}' not found in dictionary", line)
        elif isinstance(container, str):
            if not isinstance(index, int):
                raise WrongTypeError(f"String indices must be integers, not {type(index).__name__}", line)
            if index >= len(container) or index < -len(container):
                raise AgentarRuntimeError(f"String index {index} out of range for string of length {len(container)}", line)
            

    def _validate_slice_assignment(self, container, start, end, value, line):        
        if not hasattr(container, '__getitem__') or not hasattr(container, '__setitem__'):
            raise WrongTypeError(f"Object of type {type(container).__name__} does not support slice assignment", line)
        if isinstance(container, tuple):
            raise WrongTypeError(f"Tuple object does not support slice assignment", line)
        if isinstance(container, str):
            raise WrongTypeError(f"String object does not support slice assignment", line)
        if isinstance(container, dict):
            raise WrongTypeError(f"Dictionary object does not support slice assignment", line)
        if isinstance(container, list):
            if isinstance(value, str):
                pass
            elif not hasattr(value, '__iter__'):
                raise WrongTypeError(f"Can only assign an iterable to a slice", line)
            try:
                current_slice = container[start:end]
                if hasattr(value, '__len__') and len(current_slice) != len(value):
                    pass
            except Exception:
                pass