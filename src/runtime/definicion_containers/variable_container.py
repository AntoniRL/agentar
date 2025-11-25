# -*- coding: utf-8 -*- 
# runtime/definicion_containers/variable_container.py
# variable scope is the scope of variables in the agent instance

from typing import Optional, Dict
from copy import deepcopy

from ast_tree.nodes import *
from core.agentar_types import resolve_type
from runtime.errors import VariableAlreadyDeclaredError, VariableNotFoundError, WrongTypeError, NotAssignableError, AgentarRuntimeError
from core.pointer import Pointer
from core.variable_info import VariableInfo
from runtime.agent_instance.expression_evaluator import ExpressionEvaluator
from core.typed_structures import TypedList, TypedDict, TypedTuple

# VariableContainer (self._variables) is a set of VariableInfo objects, where each VariableInfo contains:
# - name: name of the variable
# - value: Pointer(value) to the value of the variable
# - var_type: type of the variable (e.g., int, str, list, dict, etc.)
# - scope: scope of the variable (e.g., "global", "local", "when_block", etc.)
# - declaration_line: line number where the variable was declared

class VariableContainer:
    def __init__(self, agent=None, scope: Optional[str] = None, parent_container: Optional['VariableContainer'] = None):
        self._agent = agent  # Reference to the agent instance where this container is used (to get fields, etc.)
        self._variables: Dict[str, VariableInfo] = {}
        self._scope = scope
        self._parent_container = parent_container  # Parent container for scope resolution


    def create_child_scope(self, scope_name: str) -> 'VariableContainer':
        """Create a new child scope that can shadow variables from this scope"""
        return VariableContainer(self._agent, scope_name, parent_container=self)
    

    def declare(self, name: str, value: Optional[ASTNode], var_type, declaration_line: Optional[int] = None, message=None):
        """Declare a variable in the current scope."""
        try:
            if name in self._variables:
                raise VariableAlreadyDeclaredError(name, declaration_line, self._variables[name].declaration_line)
            
            reference_type, default_value = resolve_type(var_type)

            if value is not None:
                if not isinstance(value, (int, float, str, bool, Pointer, TypedList, TypedDict, TypedTuple)): 
                    if self._agent is None:
                        value = ExpressionEvaluator(None).eval_expr(value, self)  # Evaluate the expression to get the value (for VariableContainer Fields and Beliefs) (self == variable_container of place where the declaration is called)
                    else:
                        value = self._agent._evaluator.eval_expr(value, self, message=message)  # Evaluate the expression to get the value. (self == variable_container of place where the declaration is called)
                if not isinstance(value, reference_type):
                    raise WrongTypeError(name, reference_type, type(value), declaration_line)

                default_value = Pointer(default_value)
                default_value.set(value)  # Set the value in the Pointer
            else:
                default_value = Pointer(default_value)  # Initialize with default value

            self._variables[name] = VariableInfo(name, default_value, var_type, self._scope, declaration_line) 

        except Exception as e:
                raise AgentarRuntimeError(e, declaration_line) from e


    def exists(self, name: str) -> bool:
        return name in self._variables or (self._parent_container is not None and self._parent_container.exists(name))


    def get_pointer(self, name: str, line: int) -> Pointer:
        return self._find(name, line).value


    def get(self, name: str, line: int, deref=False):
        if deref: 
            if isinstance(self._find(name, line).value.get(), (int, TypedDict, str, float, bool, TypedList, TypedTuple)):
                return self._find(name, line).value.get()
            else:
                return self._find(name, line).value.get().get()  # Get the value from the Pointer.Pointer
        else:
            return self._find(name, line).value.get()  # Get the value from the Pointer

    def set(self, target: str, value, line, deref=False):
        try:
            if isinstance(target, tuple):
                name, sub = target
                variable = self._find(name, line)

                if deref:
                    container = variable.value.get().get()
                else:
                    container = variable.value.get()

                if isinstance(container, TypedList):
                    container._check_type(value)
                    if isinstance(sub, slice):
                        container.assign(value, sub)
                    else:
                        container[sub] = value
                elif isinstance(container, TypedTuple):
                    raise NotAssignableError(name, TypedTuple, line)
                else:
                    container[sub] = value
                return

            variable = self._find(target, line)

            if deref:
                # with reference
                inner = variable.value.get()
                if not isinstance(inner, Pointer):
                    raise WrongTypeError(target, Pointer, type(inner), line)

                current_value = inner.get()
                expected_type = type(current_value)
                if not isinstance(value, expected_type):
                    raise WrongTypeError(target, expected_type, type(value), line)

                inner.set(value)
            else:
                # without reference
                current_value = variable.value.get()
                expected_type, _ = resolve_type(variable.var_type)
                if not isinstance(value, expected_type):
                    raise WrongTypeError(target, expected_type, type(value), line)

                variable.value.set(value)

        except Exception as e:
            raise AgentarRuntimeError(e, line) from e


    def get_info(self, name: str, line: int) -> VariableInfo:
        return self._find(name, line)


    def type_of(self, name: str, line: int) -> Optional[str]:
        return self._find(name, line).var_type


    def scope_of(self, name: str, line: int) -> Optional[str]:
        return self._find(name, line).scope


    def declared_at(self, name: str, line: int) -> Optional[int]:
        return self._find(name, line).declaration_line


    def _find(self, name: str, line: int) -> Pointer:
        var = self._find_or_none(name)
        if not var:
            raise VariableNotFoundError(name, line)
        return var


    def _find_or_none(self, name: str) -> Optional[Pointer]:
        if name in self._variables:
            return self._variables[name]  # Return the VariableInfo object
        elif self._parent_container is not None:
            return self._parent_container._find_or_none(name)
        else:
            return None


    def items(self):
        return self._variables.items()
    

    def values(self):
        return self._variables.values()


    def __iter__(self):
        return iter(self._variables)


    def __repr__(self):
        return f"({list(self._variables.keys())})"
    
