# -*- coding: utf-8 -*-
# runtime/agent_instance/actions.py
# ActionExecutor: executes actions in the context of an agent instance

import logging
from copy import deepcopy

from runtime.definicion_containers.variable_container import VariableContainer
from ast_tree.nodes import WhenBlockNode
from runtime.errors import *
from core.pointer import Pointer

class ActionExecutor:
    def __init__(self, agent):
        self.agent = agent

    def sense_world(self):
        if self.agent._sense != []:
            local_vars = VariableContainer(self.agent,"Sense")
            for stmt in self.agent._sense:
                self.agent._executor.execute_stmt(stmt, local_vars)


    def follow_rules(self):
        for rule in self.agent._rules:
            if isinstance(rule, WhenBlockNode):
                self.when_block(rule, "Rules", message=None)


    def when_block(self, when_node, name_of_local_vars, message):
        local_vars = VariableContainer(agent = self.agent, scope = name_of_local_vars)
        if message is not None:
            for var_info in message._content.values():
                local_vars.declare(var_info.name, var_info.value.get(), var_info.var_type, when_node._line)
        if when_node.conditions == []:
            for stmt in when_node.statements:
                self.agent._executor.execute_stmt(stmt, local_vars, message)
        else:
            bin_op = self.agent._evaluator.eval_expr(when_node.conditions, local_vars, message, when_node._line)
            if bin_op:
                for stmt in when_node.statements:
                    self.agent._executor.execute_stmt(stmt, local_vars, message)

    
    def check_global_goal(self):
        if self.agent._sub_goals == {}:
            self.agent._is_goal_achieved = True
            return
        else:
            sub_goals_results = VariableContainer("SubGoals")
            for goal_name, condition in self.agent._sub_goals._value.items():
                sub_goal_value = self.agent._evaluator.eval_expr(condition, sub_goals_results, None, condition._line)
                sub_goals_results.declare(goal_name, sub_goal_value, bool, condition._line)
            if self.agent._merge_goals_condition is not None:
                merge_result = self.agent._evaluator.eval_expr(self.agent._merge_goals_condition, sub_goals_results, None, self.agent._merge_goals_condition._line)
                if merge_result:
                    self.agent._is_goal_achieved = True
                else:
                    self.agent._is_goal_achieved = False
            else: 
                self.agent._is_goal_achieved = all(sub_goals_results.get(goal_name, condition._line) for goal_name, condition in self.agent._sub_goals._value.items()) 
        if self.agent._is_goal_achieved:
            pass # logging.info(f"{self.agent._id.path}:: Global goal achieved!")


    def goal_check(self, stmt, local_vars):
        goal_to_check = stmt.goal_name
        if goal_to_check not in self.agent._sub_goals._value:
            raise ASTNodeNotFoundError(goal_to_check, "Goal", stmt._line)
        condition = self.agent._sub_goals._value[goal_to_check]
        sub_goals_results = VariableContainer("SubGoals")
        return self.agent._evaluator.eval_expr(condition, sub_goals_results, None, condition._line)
        


    def execute_action(self, action_node, parameters, line_of_call_action=None):
        local_vars = VariableContainer(agent=self.agent, scope="Action")
        # Initialize parameters
        for i, param_decl in enumerate(action_node.parameters):
            self.agent._executor.execute_stmt(param_decl, local_vars, None)

            if local_vars.get(param_decl.name, action_node._line) == None and i >= len(parameters):
                raise NoValueInActionCall(param_decl.name, line_of_call_action, action_node._line)

            if parameters is not None and i < len(parameters):
                arg = parameters[i]

                if isinstance(arg, Pointer):
                    local_vars.set(param_decl.name, arg, action_node._line)
                else:
                    arg = deepcopy(arg)
                    local_vars.set(param_decl.name, arg, action_node._line)

        return_type = self.agent._evaluator.eval_expr(action_node.return_type, local_vars, None, action_node._line)

        for stmt in action_node.body:
            return_object = self.agent._executor.execute_stmt(stmt, local_vars, None)
            if self.agent._return_flag:
                self.agent._return_flag = False
                break
        if return_type != 'void':
            if type(return_object) != return_type:
                raise WrongTypeError("Return value", return_type, type(self.agent._return_object), action_node._line)
            return return_object