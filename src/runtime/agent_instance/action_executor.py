# -*- coding: utf-8 -*-
# runtime/agent_instance/actions.py
# ActionExecutor: executes actions in the context of an agent instance

from runtime.definicion_containers.variable_container import VariableContainer


class ActionExecutor:
    def __init__(self, agent):
        self.agent = agent

    def sense_world(self):
        if self.agent._sense != []:
            local_vars = VariableContainer("Sense")
            for stmt in self.agent._sense:
                self.agent._executor.execute_stmt(stmt, local_vars)

    
    def when_block(self, when_node, local_vars, message):
        if message is not None:
            for stmt in message._content.items():
                local_vars.declare(stmt[0], stmt[1], type(stmt[1]), message._line)
        if when_node.condition == []:
            for stmt in when_node.statements:
                self.agent._executor.execute_stmt(stmt, local_vars, message)
        else:
            bin_op = self.agent._evaluator.eval_expr(when_node.condition, local_vars, message, when_node._line)
            if bin_op:
                for stmt in when_node.statements:
                    self.agent._executor.execute_stmt(stmt, local_vars, message)