# -*- coding: utf-8 -*- 
# runtime/definicion_containers/goles_container.py
# # GoalsContainer: manages the goals of an agent, allowing for declaration, retrieval, and checking existence of goals.

from typing import Dict, Optional
from ast_tree.nodes import ASTNode
from runtime.errors import ASTNodeAlreadyDeclaredError, ASTNodeNotFoundError

class ASTNodeContainer:
    def __init__(self, container_type: Optional[str] = None):
        self._value: Dict[str, ASTNode] = {}
        self._container_type: Optional[str] = container_type

    def declare(self, name: str, value: ASTNode):
        if name in self._value:
            raise ASTNodeAlreadyDeclaredError(name, self._container_type, line=value._line_declaration, first_declaration_line=self._value[name]._line_declaration)
        self._value[name] = value

    def exists(self, name: str) -> bool:
        return name in self._value

    def get(self, name: str, line: int) -> ASTNode:
        if name not in self._value:
            raise ASTNodeNotFoundError(name, self._container_type, line=line)  # TODO: implement the errors with line number
        return self._value[name]

    def items(self):
        return self._value.items()

    def __iter__(self):
        return iter(self._value)
    
    def __repr__(self):
        return f"<{self._container_type}= {list(self._value.keys())}>"