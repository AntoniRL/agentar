#  -*- coding: utf-8 -*- 
# runtime/AgentarSystem.py
# System runner: starts/stops mother and other agents

import logging
from core.agent import AgentarAgent
from runtime.AgentInstance import AgentInstance
from runtime.AgentRunner import AgentRunner
from core.agentid import AgentId
import threading
from copy import deepcopy

class AgentarSystem:
    def __init__(self, mother_decl, agents_decl, messages_decl):
        self.mother_decl = mother_decl
        self.agents_decl = agents_decl          # Dict of agent declarations
        self.messages_decl = messages_decl      # Dict of messages declarations
        self.agents = {}                        # Dict of AgentInstance (agent_id -> AgentInstance)
        self.threads = {}                       # Dict of AgentRunner threads (agent_id -> AgentRunner)

        self.terminated = threading.Event()     # Event to signal termination of the system
        self.terminated.clear()                 # Clear the termination event

        self._lock = threading.Lock()

        # Create mother
        self.mother_id = AgentId(".1")
        self.mother_instance = AgentInstance(mother_decl, system=self, id=self.mother_id)
        self.agents[self.mother_id.path] = self.mother_instance  # Add mother instance to agents dict
        self.threads[self.mother_id.path] = AgentRunner(self.mother_instance, system=self, agent_id=self.mother_id)

        # Create agent time
        # self.agentTimeId = AgentId(".0")  # Unique ID for agent time
        # self.agentTime = AgentInstance(AgentarAgent(), system=self, id=self.agentTimeId)
        # self.agents[self.agentTimeId.path] = self.agentTime  # Add agent time instance to agents dict
        # self.threads[self.agentTimeId.path] = AgentRunner(self.agentTime, system=self, agent_id=self.agentTimeId)
        # self.create_agent_time()

    def start(self):
        logging.info("Starting Agentar system...")
        self.threads[self.mother_id.path].start()
        # self.threads[self.agentTimeId.path].start()


    def stop(self):
        with self._lock:
            threads_copy = list(self.threads.values())
        for thread in reversed(threads_copy):
            thread.stopAgent()
            thread.join()
            logging.info(f"Thread for agent {thread.agent_id.path} stopped.")
        logging.info("Agentar system stopped.")


    def send_message(self, message):
        receiverId = message._receiver.path
        logging.info(f"{message._sender.path}:: Sending message to {receiverId}...")        
        with self._lock:
            if receiverId in self.agents:
                receiver = self.agents[receiverId]
        if receiver is not None:
            receiver._inbox.put(message)


    def spawn_agent(self, parentInstance: AgentInstance, agent_type: AgentarAgent, fields=None):
        if self.terminated.is_set():
            return None
        
        if agent_type not in self.agents_decl:
            raise ValueError(f"Agent type {agent_type} not found in system declarations.")
        id = parentInstance._id.child(parentInstance._next_child)     # Create new AgentId for the child agent
        parentInstance._next_child += 1                              # Increment child index for next spawn
        parentInstance._children.append(id)                          # Add child id to parent's children list
        new_agent_inst = deepcopy(self.agents_decl[agent_type])               # Get the agent declaration from the system
        agent = AgentInstance(new_agent_inst, system=self, id=id, fields=deepcopy(fields))
        
        with self._lock:
            self.agents[id.path] = agent
            self.threads[id.path] = AgentRunner(agent, system=self, agent_id=id)
            self.threads[id.path].start()
        return id
        
    
    def killChildren(self, agent_id: AgentId, agent_type):
        # Kill all children of the agent
        if agent_type == None: # 
            with self._lock:
                agents_to_kill = []
                for child in self.agents[agent_id.path]._children:
                    agents_to_kill.append(child)
            for aid in agents_to_kill:
                self.killAgent(AgentId(aid))
        # Kill only children of the specified type
        else: 
            with self._lock:
                agents_to_kill = []
                for child in self.agents[agent_id.path]._children:
                    if self.agents[child].name == agent_type:
                        agents_to_kill.append(child)
            for aid in agents_to_kill:
                self.killAgent(AgentId(aid))


    def killAgent(self, agent_id: AgentId):
        agents_to_kill = []

        def collect_descendants(aid):
            with self._lock:
                children = self.agents[aid.path]._children if aid.path in self.agents else []
            for child_id in reversed(children):
                collect_descendants(child_id)
            agents_to_kill.append(aid)

        collect_descendants(agent_id)

        for aid in agents_to_kill:
            if aid.path in self.agents:
                with self._lock:
                    thread = self.threads.get(aid.path)
                thread.stopAgent()
                if thread and thread != threading.current_thread():
                    thread.join()
                logging.info(f"{aid.path}:: Agent killed.")
                

    def killMother(self):
        logging.info("Mother agent requested system shutdown.")
        self.terminated.set()


    def create_agent_time(self):
        # Create agent time instance
        self.agentTimeId = AgentId(".0")
