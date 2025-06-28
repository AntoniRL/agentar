# -*- coding: utf-8 -*-
# runtime/agent_instance/actions.py
# ActionExecutor: executes actions in the context of an agent instance

class ActionExecutor:
    def __init__(self, agent):
        self.agent = agent

    def execute_action(self, action_node, variables=None):
        pass

    def check_goal(self, stmt, local_scope):
        pass

    def when_block(self, when_node, message):
        pass