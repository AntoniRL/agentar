# -*- coding: utf-8 -*-
# runtime/agent_instance/statement_executor.py
# StatementExecutor: executes statements in the context of an agent instance


import logging
import time
from copy import deepcopy

from ast_tree.nodes import *
from core.agent_id import AgentId
from runtime.errors import *
# from core.agentar_types import resolve_type
from runtime.definicion_containers.variable_container import VariableContainer
from core.typed_structures import TypedList, TypedDict


class StatementExecutor:
    def __init__(self, agent):
        self.agent = agent

    def execute_stmt(self, stmt, local_vars, message=None, deref=False):
        match stmt:
            case VariableDeclNode(var_type=var_type, name=var_name, value=value_expr, _line=line):
                local_vars.declare(var_name, value_expr, var_type, line)


            case PrintNode() | LoggingNode():
                self.print_stmt(stmt, local_vars, message, stmt._line)
            

            case AssignmentNode():
                self.handle_assignment(stmt, local_vars, message)


            case SpawnNode():
                return self.spawn_agent(stmt, local_vars, message) 


            case MessageVarDeclNode():
                self.agent._message_handler.handle_message_declaration(stmt, local_vars)
            

            case SendNode():
                self.agent._message_handler.send_message(stmt, local_vars)
            

            case SendToChildrenNode():
                self.agent._message_handler.send_to_children(stmt, local_vars)


            case SendToSiblingsNode():
                self.agent._message_handler.send_to_siblings(stmt, local_vars)


            case KillNode():
                if stmt.agent_id:
                    agent_id = self.agent._evaluator.eval_expr(stmt.agent_id, local_vars, message, stmt._line)
                    self.agent._runtime.kill_agent(agent_id, stmt._line)
                elif self.agent._isMother:
                    self.agent._runtime.kill_mother()
                else:
                    self.agent._runtime.kill_agent(self.agent._id, stmt._line)


            case KillChildrenNode():
                agent_type = stmt.agent_type.name if stmt.agent_type else None
                self.agent._runtime.kill_children(self.agent._id, agent_type, stmt._line) # kill all children of this agent with the specified type


            case GoalCheckNode():
                return self.agent._action_executor.goal_check(stmt, local_vars)


            case DoNode():
                action_node = self.agent._actions.get(stmt.name, stmt._line)
                parameters = [self.agent._evaluator.eval_expr(param, local_vars, message, stmt._line) for param in stmt.variables]
                return self.agent._action_executor.execute_action(action_node, parameters, stmt._line)


            case ReturnNode():
                self.agent._return_flag = True
                return self.agent._evaluator.eval_expr(stmt.value, local_vars, message, stmt._line)


            case SleepNode():
                dutarion = self.agent._evaluator.eval_expr(stmt.duration, local_vars, message, stmt._line)
                if not isinstance(dutarion, (int, float)):
                    raise WrongTypeError("Sleep duration", "int or float", type(dutarion), stmt._line)
                logging.info(f"{self.agent._id.path}:: Sleeping for {dutarion} seconds")
                time.sleep(dutarion)


            case IfStmtNode():
                local_vars = local_vars.create_child_scope("if")
                condition = self.agent._evaluator.eval_expr(stmt.conditions, local_vars, message, stmt._line)
                if condition:
                    for statement in stmt.statements:
                        if self.agent._break_flag or self.agent._return_flag:
                            break
                        self.execute_stmt(statement, local_vars, message, stmt._line)
                else:
                    if stmt.elseStmt is not None:
                        for statement in stmt.elseStmt:
                            if self.agent._break_flag or self.agent._return_flag:
                                break
                            self.execute_stmt(statement, local_vars, message, stmt._line)


            case ForLoopNode():
                local_vars_for = local_vars.create_child_scope("for")
                self.execute_stmt(stmt.initialize, local_vars_for, message, stmt._line)  # Initialize loop variable
                def check_condition():
                    return self.agent._evaluator.eval_expr(stmt.condition, local_vars_for, message, stmt._line)
                def update_loop_var():
                    self.execute_stmt(stmt.update, local_vars_for, message, stmt._line)
                while check_condition() and not self.agent._break_flag and not self.agent._return_flag:
                    local_vars_iter = local_vars_for.create_child_scope("for iteration")
                    for statement in stmt.body:
                        self.execute_stmt(statement, local_vars_iter, message, stmt._line)
                        if self.agent._continue_flag: # If continue flag is set, skip to the next iteration
                            self.agent._continue_flag = False
                            update_loop_var()
                            break
                    update_loop_var()
                self.agent._break_flag = False  # Reset break flag after loop execution
                self.agent._continue_flag = False  # Reset continue flag after loop execution


            case WhileLoopNode():
                def check_condition():
                    return self.agent._evaluator.eval_expr(stmt.condition, local_vars, message, stmt._line)
                while check_condition() and not self.agent._break_flag and not self.agent._return_flag:
                    local_vars_iter = local_vars.create_child_scope("while iteration")
                    for statement in stmt.body:
                        self.execute_stmt(statement, local_vars_iter, message, stmt._line)
                        if self.agent._continue_flag: # If continue flag is set, skip to the next iteration
                            self.agent._continue_flag = False
                            break
                self.agent._continue_flag = False  # Reset continue flag after loop execution
                self.agent._break_flag = False  # Reset break flag after loop execution


            case BreakNode():
                self.agent._break_flag = True


            case ContinueNode():
                self.agent._continue_flag = True


            case SenseNode():
                self.agent._action_executor.sense_world()


            case ListAddNode(base=base, value=value):
                base = self.agent._evaluator.eval_expr(base, local_vars, message, stmt._line)
                value = self.agent._evaluator.eval_expr(value, local_vars, message, stmt._line)
                print(type(base))
                if isinstance(base, TypedList):
                    base.append(value)
                else:
                    raise WrongTypeError("base", "TypedList", type(base), stmt._line)


            case DictDelNode(base=base, key=key):
                # Both Dict and List 'del' operator in one case
                base = self.agent._evaluator.eval_expr(base, local_vars, message, stmt._line)
                key = self.agent._evaluator.eval_expr(key, local_vars, message, stmt._line)
                if isinstance(base, TypedDict):
                    del base[key]
                elif isinstance(base, TypedList):
                    base._check_type(key)
                    del base[key]
                else:
                    raise WrongTypeError("base", "TypedDict or TypedList", type(base), stmt._line)



# ------------------------------------------
#  Extra methods for handling specific statements
# ------------------------------------------

    def spawn_agent(self, spawn_node, local_vars, message):
        if spawn_node.args:
            fields = {}
            for arg in spawn_node.args:
                key, value = arg
                value_to_assign = self.agent._evaluator.eval_expr(value, local_vars, message, spawn_node._line)
                if isinstance(value, AddressOfExprNode):
                    fields[key] = value_to_assign
                else:
                    fields[key] = deepcopy(value_to_assign)
        else:
            fields = {}
        return self.agent._runtime.spawn_agent(parentInstance=self.agent, agent_type=spawn_node.agent_type, fields=fields, line=spawn_node._line)


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


# --- Handle assignment 
    def handle_assignment(self, stmt, local_vars, message=None):
        if isinstance(stmt.value, (SpawnNode, DoNode, GoalCheckNode, GetTimeNode)):
            value = self.execute_stmt(stmt.value, local_vars, message)
        else:
            value = self.agent._evaluator.eval_expr(stmt.value, local_vars, message, stmt._line)

        self.assign_to_target(stmt.target, value, local_vars, message, stmt._line)


    def assign_to_target(self, target_node, value, local_vars, message, line, deref=False):
        match target_node:
            case VarRefNode(name=name):
                local_vars.set(name, value, line, deref)

            case IndexAccessNode(name=name, index=index):
                index_value = self.agent._evaluator.eval_expr(index, local_vars, message, line, deref)
                if isinstance(name, SelfAccessNode):
                    target_name = name.path[1]
                    self.agent._fields.set((target_name, index_value), value, line, deref)
                elif isinstance(name, BelAccessNode):
                    target_name = name.path[1]
                    self.agent._beliefs.set((target_name, index_value), value, line, deref)
                else:
                    local_vars.set((name.name, index_value), value, line, deref)

            case SliceAccessNode(name=name, start=start, end=end):
                start_value = self.agent._evaluator.eval_expr(start, local_vars, message, line) if start else 0
                end_value = self.agent._evaluator.eval_expr(end, local_vars, message, line) if end else None
                if isinstance(name, SelfAccessNode):
                    target_name = name.path[1]
                    self.agent._fields.set((target_name, slice(start_value, end_value)), value, line, deref)
                elif isinstance(name, BelAccessNode):
                    target_name = name.path[1]
                    self.agent._beliefs.set((target_name, slice(start_value, end_value)), value, line, deref)
                else:
                    local_vars.set((name.name, slice(start_value, end_value)), value, line, deref)

            case SelfAccessNode(path=path):
                target_name = path[1]
                self.agent._fields.set(target_name, value, line, deref)

            case BelAccessNode(path=path):
                target_name = path[1]
                self.agent._beliefs.set(target_name, value, line, deref)

            case DerefExprNode(pointer=pointer, _line=line):
                self.assign_to_target(pointer, value, local_vars, message, line, deref=True)   

            case _:
                raise AgentarRuntimeError(f"Unsupported assignment target: {target_node}", line)
            