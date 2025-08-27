# -*- coding: utf-8 -*- 
# runtime/AgentRunner.py
# AgentRunner: thread class running AgentInstance

import threading
import time
import logging
from runtime.logging_setup import get_agent_logger

class AgentRunner(threading.Thread):
    """
    One thread per agent. Periodically calls step() on the associated AgentInstance.
    """
    def __init__(self, instance, system, agent_id, tick_interval=0.5, **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.agent_id = agent_id
        self.instance = instance
        self.tick_interval = tick_interval
        self.running = threading.Event()
        self.running.set()

    def run(self):
        log = logging.LoggerAdapter(get_agent_logger(self.agent_id.path), {"agent_id": self.agent_id.path})
        try:
            self.instance.initializeAgent()

            while self.running.is_set() and not self.system.terminated.is_set():
                self.instance.step()
                time.sleep(self.tick_interval)
            
            self.instance.destroyAgent()

        except Exception as e:
            logging.error(f"❌ ERROR:: Exception in agent {self.agent_id.path}")
            log.error(f"Exception in agent {self.agent_id.path}: {e}", exc_info=True)
            # Stop system
            self.system.terminated.set()

    def stopAgent(self):
        self.running.clear()