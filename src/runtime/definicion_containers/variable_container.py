# -*- coding: utf-8 -*- 
# runtime/definicion_containers/variable_container.py
# variable scope is the scope of variables in the agent instance

from typing import Optional, Dict

from ast_tree.nodes import *
from core.agentar_types import resolve_type
from runtime.agent_instance.expression_evaluator import ExpressionEvaluator
from runtime.errors import VariableAlreadyDeclaredError, VariableNotFoundError, WrongTypeError


class VariableInfo:
    def __init__(self, name: str, value, var_type, scope: str, declaration_line: Optional[int] = None):
        self.name: str = name
        self.value = value
        self.var_type = var_type
        self.scope = scope
        self.declaration_line = declaration_line

    def __repr__(self):
        return f"VariableInfo(name={self.name}, type={self.var_type}, scope={self.scope}, value={self.value})"


class VariableContainer:
    def __init__(self, scope: Optional[str] = None, parent: Optional['VariableContainer'] = None):
        self._variables: Dict[str, VariableInfo] = {}
        self._scope = scope
        self._parent = parent

    def create_child_scope(self, scope_name: str) -> 'VariableContainer':
        """Create a new child scope that can shadow variables from this scope"""
        return VariableContainer(scope_name, parent=self)
    

    # Declare a variable with a name, value, type, and optional declaration line
    def declare(self, name: str, value: Optional[ASTNode], var_type: ASTNode, declaration_line: Optional[int] = None):
        type_name, defoult_value = resolve_type(var_type)
        if name in self._variables:
            raise VariableAlreadyDeclaredError(name, declaration_line, self._variables[name].declaration_line)
        if value is None:
            value = defoult_value
        else: 
            if isinstance(value, ASTNode):
                value = ExpressionEvaluator(None).eval_expr(value)  # Evaluate the expression to get the value
            if type(value) != type_name:
                raise WrongTypeError(name, type_name, type(value), declaration_line)
        self._variables[name] = VariableInfo(name, value, var_type, self._scope, declaration_line)


    def exists(self, name: str) -> bool:
        return name in self._variables or (self._parent is not None and self._parent.exists(name))


    def get(self, name: str, line: int):
        return self._find(name, line).value


    def set(self, name: str, value, line):
        if isinstance(value, ASTNode):
            value = ExpressionEvaluator(None).eval_expr(value)
        var_info = self._find(name, line)
        expexted_type, _ = resolve_type(var_info.var_type)  # Ensure the type is valid
        if type(value) != expexted_type:
            raise WrongTypeError(name, expexted_type, type(value), line)
        var_info.value = value


    def get_info(self, name: str, line: int) -> VariableInfo:
        return self._find(name, line)


    def type_of(self, name: str, line: int) -> Optional[str]:
        return self._find(name, line).var_type


    def scope_of(self, name: str, line: int) -> Optional[str]:
        return self._find(name).scope


    def declared_at(self, name: str, line: int) -> Optional[int]:
        return self._find(name, line).declaration_line


    def _find(self, name: str, line: int) -> VariableInfo:
        var = self._find_or_none(name)
        if not var:
            raise VariableNotFoundError(name, line)
        return var


    def _find_or_none(self, name: str) -> Optional[VariableInfo]:
        if name in self._variables:
            return self._variables[name]
        elif self._parent is not None:
            return self._parent._find_or_none(name)
        else:
            return None


    def items(self):
        return self._variables.items()


    def __iter__(self):
        return iter(self._variables)


    def __repr__(self):
        return f"({list(self._variables.keys())})"