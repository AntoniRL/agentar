# -*- coding: utf-8 -*-
# runtime/agent_instance/lifecycle.py
# Lifecycle management for agent instances, including initialization, stepping, and destruction.


import logging

from runtime.definicion_containers.variable_container import VariableContainer


class AgentLifecycleManager:
    def __init__(self, agent):
        self.agent = agent

    def initializeAgent(self):
        logging.info(f"{self.agent._id}:: Initializing agent")
        local_vars = VariableContainer("Initialize")
        for stmt in self.agent._initialize:
            self.agent._executor.execute_stmt(stmt, local_vars)

    def step(self):
        self.agent._action_executor.sense_world()
        if not self.agent._inbox.empty():
            self.agent._message_handler.handle_incoming_messages(self.agent._inbox.get())
        self.agent._action_executor.check_global_goal()
        self.agent._action_executor.follow_rules()

    def destroyAgent(self):
        local_vars = VariableContainer()
        for stmt in self.agent._destroy:
            self.agent._executor.execute_stmt(stmt, local_vars)

        with self.agent._runtime._lock:
            if not self.agent._isMother:
                del self.agent._runtime.agents[self.agent._id.path]
                del self.agent._runtime.threads[self.agent._id.path]