# -*- coding: utf-8 -*-
# runtime/agent_instance/statement_executor.py
# StatementExecutor: executes statements in the context of an agent instance


import logging

from ast_tree.nodes import *
from core.agent_id import AgentId
from runtime.errors import *
from core.agentar_types import resolve_type

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
        match stmt.value:
            case SpawnNode():
                value = self.execute_stmt(stmt.value, local_vars, message)
            case DoNode():
                value = self.execute_stmt(stmt.value, local_vars, message)
            case GoalCheckNode():
                value = self.execute_stmt(stmt.value, local_vars, message)
            case GetTimeNode():
                value = self.execute_stmt(stmt.value, local_vars, message)
            case _:
                value = self.agent._evaluator.eval_expr(stmt.value, local_vars, message, stmt._line)

        self.assign_to_target(stmt.target, value, local_vars, message, stmt._line)

    
    # TODO: handle_spawn should return AgentId
    def assign_to_target(self, target_node, value, local_vars, message, line):
        print(target_node)
        match target_node:
            case VarRefNode(name=name):
                local_vars.set(name, value, line)
            case IndexAccessNode():
                pass 
            case SelfAccessNode():
                target = target_node.path[1]
                self.assign_to_storage()
            case BelAccessNode():
                pass
            case MessageInitNode():
                pass

    
    def assign_to_storage(self, storage, target, value):
        pass



