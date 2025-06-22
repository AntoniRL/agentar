# -*- coding: utf-8 -*- 
# runtime/AgentTime.py
# AgentTime: 
import threading
import time
import logging

class AgentTime(threading.Thread):
    """
    AgentTime: Thread that periodically calls step() on the AgentInstance.
    """
    def __init__(self, system, agent_id, tick_interval=0.5, **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.agent_id = agent_id
        self.tick_interval = tick_interval
        self.running = threading.Event()
        self.running.set()
        self._TIME = 0 # Global time variable, can be used by agents

    def getTime(self):
        return self._TIME

    def run(self):
        while self.running.is_set() and not self.system.terminated.is_set():
            time.sleep(self.tick_interval)
            self._TIME += 1

    def stopAgent(self):
        self.running.clear()