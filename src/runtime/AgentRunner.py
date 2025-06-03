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
    def __init__(self, instance, tick_interval=1.0):
        super().__init__()
        self.instance = instance
        self.tick_interval = tick_interval
        self.running = True

    def run(self):
        while self.running:
            logging.info(f"[RUN] {self.instance.id}")
            # self.instance.step()
            time.sleep(self.tick_interval)

    def stop(self):
        self.running = False