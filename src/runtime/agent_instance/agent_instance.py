# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from queue import Queue

from core.agent import AgentarAgent
from core.agent_id import AgentId

from runtime.agent_instance.lifecycle import AgentLifecycleManager
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
        self._is_goal_achived = False         # Flag to indicate if the agent's goal is achieved        

        self._runtime = system               # Reference to the AgentarSystem instance

        self._fields.declare("id", self._id, AgentId) # Declare the agent's ID in the fields container # TODO: is it necessary to declare the ID in the fields container?

        self._return_flag = False  # Flag to indicate if a return statement was executed
        self._return_object = None  # Object to return from the action
        self._break_flag = False   # Flag to indicate if a break statement was executed
        self._continue_flag = False  # Flag to indicate if a continue statement was executed

        # Components
        self._lifecycle = AgentLifecycleManager(self)      # Lifecycle manager for the agent instance
        self._executor = StatementExecutor(self)       # Statement executor for the agent instance
        self._evaluator = ExpressionEvaluator(self)    # Expression evaluator for the agent instance
        self._message_handler = MessageHandler(self)       # Message handler for the agent instance
        self._action_executor = ActionExecutor(self)       # Action executor for the agent instance


    def __repr__(self):
        return (
            f"<AgentarAgentInstance name='{self._name}', id='{self._id.path}'\n"
            f"</AgentarAgentInstance>"
        )


    def initializeAgent(self):
        self._lifecycle.initializeAgent()


    def step(self):
        self._lifecycle.step()


    def destroyAgent(self):
        self._lifecycle.destroyAgent()