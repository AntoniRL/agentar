# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from queue import Queue
import logging

from core.agent import AgentarAgent
from core.agent_id import AgentId
from runtime.definicion_containers.variable_container import VariableContainer

from runtime.agent_instance.statement_executor import StatementExecutor
from runtime.agent_instance.expression_evaluator import ExpressionEvaluator
from runtime.agent_instance.message_handler import MessageHandler
from runtime.agent_instance.action_executor import ActionExecutor


class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None):
        for key, value in agent_ast.__dict__.items():  # Copy all attributes from the agent_AST to the instance
            setattr(self, key, value)
        self._id = id        
        self._parent = id.parent() if not self._isMother else None
        self._children = []                  # List of agent children [AgentId]
        self._next_child = 1
        self._now = 1                        # time step counter (Agent perception time)
        self._inbox = Queue()                # Queue for incoming messages
        self._is_goal_achieved = False         # Flag to indicate if the agent's goal is achieved

        self._runtime = system               # Reference to the AgentarSystem instance

        # self._fields.declare("id", self._id, AgentId) # Declare the agent's ID in the fields container # TODO: is it necessary to declare the ID in the fields container?

        self._return_flag = False  # Flag to indicate if a return statement was executed
        self._return_object = None  # Object to return from the action
        self._break_flag = False   # Flag to indicate if a break statement was executed
        self._continue_flag = False  # Flag to indicate if a continue statement was executed

        # Components
        self._executor = StatementExecutor(self)       # Statement executor for the agent instance
        self._evaluator = ExpressionEvaluator(self)    # Expression evaluator for the agent instance
        self._message_handler = MessageHandler(self)       # Message handler for the agent instance
        self._action_executor = ActionExecutor(self)       # Action executor for the agent instance


    @property
    def name(self):
        return self._name
    @property
    def is_goal_achieved(self):
        return self._is_goal_achieved
    @property
    def id(self):
        return self._id
    @property
    def parent(self):
        return self._parent
    @property
    def children(self):
        return self._children

    def __repr__(self):
        return (
            f"<AgentarAgentInstance name='{self._name}', id='{self._id.path}'\n"
            f"</AgentarAgentInstance>"
        )


    def initializeAgent(self):
        """
        Initialize the agent instance by executing its initialization statements.
        """
        logging.info(f"{self._id}:: Initializing agent")
        local_vars = VariableContainer(agent=self, scope="Initialize")
        for stmt in self._initialize:
            self._executor.execute_stmt(stmt, local_vars)


    def step(self):
        """
        Perform a single step in the agent's lifecycle, executing its actions and processing messages.
        """
        self._action_executor.sense_world()
        qsize = self._inbox.qsize()
        batch = min( max(1, qsize // 2), 10 )
        for _ in range(batch):
            if not self._inbox.empty():
                self._message_handler.process_messages(self._inbox.get())
        # if not self._inbox.empty():
        #     self._message_handler.process_messages(self._inbox.get())
        self._action_executor.check_global_goal()
        self._action_executor.follow_rules()


    def destroyAgent(self):
        """
        Destroy the agent instance by executing its destruction statements and cleaning up resources.
        """
        local_vars = VariableContainer(agent=self, scope="Destroy")
        for stmt in self._destroy:
            self._executor.execute_stmt(stmt, local_vars)

        # Clean up the agent instance
        with self._runtime._lock:
            if not self._isMother:
                del self._runtime.agents[self._id.path]
                del self._runtime.threads[self._id.path]