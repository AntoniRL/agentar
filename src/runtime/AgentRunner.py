# -*- coding: utf-8 -*- 
# runtime/AgentRunner.py
# AgentRunner: thread class running AgentInstance

import threading
import time
import logging

class AgentRunner(threading.Thread):
    """
    One thread per agent. Periodically calls step() on the associated AgentInstance.
    """
    def __init__(self, instance, system, agent_id, tick_interval=0.5):
        super().__init__()
        self.system = system
        self.agent_id = agent_id
        self.instance = instance
        self.tick_interval = tick_interval
        self.running = True

    def run(self):
        self.instance.initialize()

        while self.running:
            self.instance.step()
            time.sleep(self.tick_interval)
        
        self.instance.destroy()

        # if the agent is not the mother, remove it from the system
        if (self.agent_id.path != self.system.mother_id.path) and (self.system and self.agent_id in self.system.threads):
                del self.system.agents[self.agent_id]
                del self.system.threads[self.agent_id]

    def stop(self):
        self.running = False