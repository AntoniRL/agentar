# -*- coding: utf-8 -*-
# runtime/error.py
# file for defining custom exceptions used in the interpreter

class AgentarRuntimeError(Exception):
    """Bazowy wyjątek dla wszystkich błędów wykonania w interpreterze."""
    def __init__(self, message, node=None, line=None):
        super().__init__(message)
        self.node = node
        self.line = line


class VariableNotFoundError(AgentarRuntimeError):
    pass


class TypeMismatchError(AgentarRuntimeError):
    pass


class AssignmentError(AgentarRuntimeError):
    pass


class MessageDispatchError(AgentarRuntimeError):
    pass


class GoalEvaluationError(AgentarRuntimeError):
    pass