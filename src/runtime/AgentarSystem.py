#  -*- coding: utf-8 -*- 
# runtime/AgentarSystem.py
# System runner: starts/stops mother and other agents

import logging
from core.agent import AgentarAgent
from runtime.AgentInstance import AgentInstance
from runtime.AgentRunner import AgentRunner
from core.agentid import AgentId

class AgentarSystem:
    def __init__(self, mother_decl, agents_decl, messages_decl):
        self.mother_decl = mother_decl
        self.agents_decl = agents_decl          # Dict of agent declarations
        self.messages_decl = messages_decl      # Dict of messages declarations
        self.agents = {}                        # Dict of AgentInstance (agent_id -> AgentInstance)
        self.threads = {}                       # Dict of AgentRunner threads (agent_id -> AgentRunner)

        # create agent time
        # self.time_id = AgentId(".2")
        # self.AgentTime = AgentInstance(AgentarAgent(), agent_id=self.time_id)

        # Create mother
        self.mother_id = AgentId(".1")
        mother_instance = AgentInstance(mother_decl, system=self, id=self.mother_id)
        self.agents[self.mother_id.path] = mother_instance
        self.threads[self.mother_id.path] = AgentRunner(mother_instance, system=self, agent_id=self.mother_id)


    def start(self):
        logging.info("Starting Agentar system...")
        self.threads[self.mother_id.path].start()

    def stop(self):
        for thread in self.threads.values():
            thread.stop()
            thread.join()
        logging.info("Stopping Agentar system...")

    def send_message(self, sender_id, to_id, msg, msg_type):
        pass

    def spawn_agent(self, agent_type_name, args, parent):
        pass