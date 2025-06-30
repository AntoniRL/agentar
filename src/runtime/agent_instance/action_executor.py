# -*- coding: utf-8 -*-
# runtime/agent_instance/actions.py
# ActionExecutor: executes actions in the context of an agent instance

import logging

from runtime.definicion_containers.variable_container import VariableContainer
from ast_tree.nodes import WhenBlockNode


class ActionExecutor:
    def __init__(self, agent):
        self.agent = agent

    def sense_world(self):
        if self.agent._sense != []:
            local_vars = VariableContainer("Sense")
            for stmt in self.agent._sense:
                self.agent._executor.execute_stmt(stmt, local_vars)


    def follow_rules(self):
        for rule in self.agent._rules:
            if isinstance(rule, WhenBlockNode):
                self.when_block(rule, "Rules", message=None)


    def when_block(self, when_node, local_vars_name, message):
        local_vars = VariableContainer(f"{local_vars_name}")
        if message is not None:
            for stmt in message._content.items():
                local_vars.declare(stmt[0], stmt[1], type(stmt[1]), message._line)
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
            self.agetn._is_goal_achived = True
            return
        else:
            sub_goals_results = VariableContainer("SubGoals")
            for goal_name, condition in self.agent._sub_goals._value.items():
                sub_goal_value = self.agent._evaluator.eval_expr(condition, sub_goals_results, None, condition._line)
                sub_goals_results.declare(goal_name, sub_goal_value, bool, condition._line)
            if self.agent._merge_goals_condition is not None:
                merge_result = self.agent._evaluator.eval_expr(self.agent._merge_goals_condition, sub_goals_results, None, self.agent._merge_goals_condition._line)
                if merge_result:
                    self.agent._is_goal_achived = True
                else:
                    self.agent._is_goal_achived = False
            else: 
                self.agent._is_goal_achived = all(sub_goals_results.get(goal_name, condition._line) for goal_name, condition in self.agent._sub_goals._value.items()) 
        if self.agent._is_goal_achived:
            pass # logging.info(f"{self.agent._id.path}:: Global goal achieved!")


    def execute_action(self, action_node, variables):
        pass