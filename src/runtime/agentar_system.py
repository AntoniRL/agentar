#  -*- coding: utf-8 -*- 
# runtime/AgentarSystem.py
# System runner: starts/stops mother and other agents

import logging
import threading
from copy import deepcopy

from core.agent import AgentarAgent
from core.agent_id import AgentId
from runtime.agent_instance.agent_instance import AgentInstance
from runtime.agent_runner import AgentRunner
from runtime.agent_time import AgentTime
from runtime.errors import FieldWithNoneValueError


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

        # TODO: Create agent time
        # self.agentTime = AgentTime(system=self, agent_id=AgentId(".0"))
        # self.threads[self.agentTime.agent_id.path] = self.agentTime
        # self.agents[self.agentTime.agent_id.path] = self.agentTime  # Add agent time to agents dict
        


    def start(self):
        logging.info("Starting Agentar system...")
        self.threads[self.mother_id.path].start()
        # self.threads[self.agentTime.agent_id.path].start()


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
            if receiverId in self.agents.keys():
                receiver = self.agents[receiverId]
        if receiver is not None:
            receiver._inbox.put(message)


    def spawn_agent(self, parentInstance: AgentInstance, agent_type: AgentarAgent, fields=None, line=None):
        if self.terminated.is_set():
            return None
        agent_decl = deepcopy(self.agents_decl.get(agent_type))

        for key, value in fields.items():
            agent_decl._fields.set(key, value, line)

        # check if all fields has values in the agent instance
        for field_name in agent_decl._fields._variables.keys():
            if agent_decl._fields.get(field_name, line) is None:
                raise FieldWithNoneValueError(field_name, line)
        
        id = parentInstance._id.child(parentInstance._next_child)  # Create new AgentId for the child agent
        parentInstance._next_child += 1                           # Increment child index for next spawn
        parentInstance._children.append(id)                       # Add child id to parent's children list
        agent = AgentInstance(agent_decl, system=self, id=id)  # Create
        with self._lock:
            self.agents[id.path] = agent
            self.threads[id.path] = AgentRunner(agent, system=self, agent_id=id)
            self.threads[id.path].start()
        return id

    
    def kill_children(self, agent_id: AgentId, agent_type, line=None):
        # Kill all children of the agent
        if agent_type == None: # 
            with self._lock:
                agents_to_kill = []
                for child in self.agents[agent_id.path]._children:
                    agents_to_kill.append(child)
            for aid in agents_to_kill:
                self.kill_agent(aid)
        # Kill only children of the specified type
        else: 
            with self._lock:
                agents_to_kill = []
                for child in self.agents[agent_id.path]._children:
                    if self.agents[child.path]._name == agent_type:
                        agents_to_kill.append(child)
            for aid in agents_to_kill:
                self.kill_agent(aid)


    def kill_agent(self, agent_id: AgentId, line=None):
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
                # Remove agent from its parent's children list
                parent_id = aid.parent()
                if parent_id and parent_id.path in self.agents:
                    with self._lock:
                        if aid in self.agents[parent_id.path]._children:
                            self.agents[parent_id.path]._children.remove(aid)
                # Remove agent from the system's agents and threads
                with self._lock:
                    thread = self.threads.get(aid.path)
                thread.stopAgent()
                if thread and thread != threading.current_thread():
                    thread.join()
                logging.info(f"{aid.path}:: Agent killed.")
                

    def kill_mother(self):
        logging.info("Mother agent requested system shutdown.")
        self.terminated.set()
