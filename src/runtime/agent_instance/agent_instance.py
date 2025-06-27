# -*- coding: utf-8 -*- 
# runtime/AgentInstance.py
# Agent instance: represents a single agent in the Agentar system

from queue import Queue

from core.agent import AgentarAgent
from core.agent_id import AgentId

class AgentInstance:
    def __init__(self, agent_ast: AgentarAgent, system, id: AgentId = None, fields = None):
        for key, value in agent_ast.__dict__.items():  # Copy all attributes from the agent_AST to the instance
            setattr(self, key, value)
        self._agent = agent_ast
        self._isMother = self._agent._isMother
        self._id = id        
        self._parent = id.parent() if not self._isMother else None
        self._children = []                  # List of agent children [AgentId]
        self._next_child = 1
        self._now = 1                        # time step counter (Agent perception time)
        self._inbox = Queue()                # Queue for incoming messages
        self._isGoalAchieved = False         # Flag to indicate if the agent's goal is achieved        

        self._runtime = system               # Reference to the AgentarSystem instance

        # Initialize agent fields from the agent declaration
        if fields is not None:
            for key, value, val_type in zip(self._agent._fields.keys(), fields, self._agent._fields_type.values()):
                if type(value) == val_type:
                    self._fields[key] = value
                    self._fields_type[key] = val_type

        self._fields["id"] = self._id   # Set the agent's id in its fields (Make it issier to access)
        self._fields_type["id"] = AgentId

        self._return_flag = False  # Flag to indicate if a return statement was executed
        self._return_object = None  # Object to return from the action
        self._break_flag = False   # Flag to indicate if a break statement was executed
        self._continue_flag = False  # Flag to indicate if a continue statement was executed

        # TODO: Components
        self.executor = StatementExecutor(self)
        self.evaluator = ExpressionEvaluator(self)
        self.message_handler = MessageHandler(self)
        self.lifecycle = AgentLifecycleManager(self)
        self.action_executor = ActionExecutor(self)


    def __repr__(self):
        return (
            f"<AgentarAgent name='{self._name}', id='{self._id.path}'\n"
            f"</AgentarAgent>"
        )


    def initialize(self):
        self.lifecycle.initialize()


    def step(self):
        self.lifecycle.step()


    def destroy(self):
        self.lifecycle.destroy()