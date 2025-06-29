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
    def __init__(self, scope: Optional[str] = None):
        self._variables: Dict[str, VariableInfo] = {}
        self._scope = scope


    # Declare a variable with a name, value, type, and optional declaration line
    def declare(self, name: str, value: Optional[ASTNode], var_type: ASTNode, declaration_line: Optional[int] = None):
        type_name, defoult_value = resolve_type(var_type)  # This will raise an error if the type is not valid
        if name in self._variables:
            raise VariableAlreadyDeclaredError(name, declaration_line, self._variables[name].declaration_line)
        if value is None:
            value = defoult_value
        else: 
            value = ExpressionEvaluator(None).eval_expr(value)  # Evaluate the expression to get the value
            if type(value) != type_name:
                raise WrongTypeError(name, type_name, type(value), declaration_line)
        self._variables[name] = VariableInfo(name, value, var_type, self._scope, declaration_line)


    def exists(self, name: str) -> bool:
        return name in self._variables


    def get(self, name: str, line: int):
        info = self._require_variable(name, line)
        return info.value


    def set(self, name: str, value, line):
        info = self._require_variable(name, line)
        info.value = value


    def get_info(self, name: str) -> VariableInfo:
        return self._require_variable(name)


    def type_of(self, name: str) -> Optional[str]:
        return self._variables[name].var_type if name in self._variables else None


    def scope_of(self, name: str) -> Optional[str]:
        return self._variables[name].scope if name in self._variables else None


    def declared_at(self, name: str) -> Optional[int]:
        return self._variables[name].declaration_line if name in self._variables else None


    def _require_variable(self, name: str, line: int) -> VariableInfo:
        if name not in self._variables:
            raise VariableNotFoundError(name, line)
        return self._variables[name]


    def items(self):
        return self._variables.items()


    def __iter__(self):
        return iter(self._variables)


    def __repr__(self):
        return f"{self._scope}: ({list(self._variables.keys())})"
