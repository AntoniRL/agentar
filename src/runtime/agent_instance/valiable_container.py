# -*- coding: utf-8 -*- 
# runtime/agent_instance/variable_scope.py
# variable scope is the scope of variables in the agent instance

from typing import Optional, Dict

class VariableInfo:
    def __init__(
        self,
        name: str,
        value,
        var_type: str,
        scope: str,  # 'local', 'field', 'belief', 'message', etc.
        declaration_line: Optional[int] = None
    ):
        self.name = name
        self.value = value
        self.var_type = var_type
        self.scope = scope
        self.declaration_line = declaration_line

    def __repr__(self):
        return f"VariableInfo(name={self.name}, type={self.var_type}, scope={self.scope}, value={self.value})"


class VariableContainer:
    def __init__(self):
        self._variables: Dict[str, VariableInfo] = {}

    def declare(self, name: str, value, var_type: str, scope: str, declaration_line: Optional[int] = None):
        if name in self._variables:
            raise ValueError(f"Variable '{name}' is already declared.")
        self._variables[name] = VariableInfo(name, value, var_type, scope, declaration_line)

    def exists(self, name: str) -> bool:
        return name in self._variables

    def get(self, name: str):
        info = self._require_variable(name)
        return info.value

    def set(self, name: str, value):
        info = self._require_variable(name)
        info.value = value

    def get_info(self, name: str) -> VariableInfo:
        return self._require_variable(name)

    def type_of(self, name: str) -> Optional[str]:
        return self._variables[name].var_type if name in self._variables else None

    def scope_of(self, name: str) -> Optional[str]:
        return self._variables[name].scope if name in self._variables else None

    def declared_at(self, name: str) -> Optional[int]:
        return self._variables[name].declaration_line if name in self._variables else None

    def _require_variable(self, name: str) -> VariableInfo:
        if name not in self._variables:
            raise NameError(f"Variable '{name}' not found.")
        return self._variables[name]

    def items(self):
        return self._variables.items()

    def __iter__(self):
        return iter(self._variables)

    def __repr__(self):
        return f"VariableContainer({list(self._variables.keys())})"
