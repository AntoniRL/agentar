# -*- coding: utf-8 -*- 
# runtime/definicion_containers/variable_container.py
# variable scope with shadowing support

from typing import Optional, Dict, List

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
        self._children: List['VariableContainer'] = []
        
        if parent:
            parent._children.append(self)

    def create_child_scope(self, scope_name: str) -> 'VariableContainer':
        """Create a new child scope that can shadow variables from this scope"""
        return VariableContainer(scope_name, parent=self)

    def declare(self, name: str, value: Optional[ASTNode], var_type: ASTNode, 
               declaration_line: Optional[int] = None, allow_shadowing: bool = True):
        type_name, default_value = resolve_type(var_type)
        
        # Check for redeclaration in current scope only
        if name in self._variables:
            raise VariableAlreadyDeclaredError(name, declaration_line, self._variables[name].declaration_line)
        
        # Optionally warn about shadowing (useful for debugging)
        if not allow_shadowing and self._parent and self._parent._find_in_chain(name):
            # You could add a warning system here if needed
            pass
        
        if value is None:
            value = default_value
        else: 
            value = ExpressionEvaluator(None).eval_expr(value)
            if type(value) != type_name:
                raise WrongTypeError(name, type_name, type(value), declaration_line)
        
        self._variables[name] = VariableInfo(name, value, var_type, self._scope, declaration_line)

    def exists(self, name: str) -> bool:
        """Check if variable exists in this scope or any parent scope"""
        return name in self._variables or (self._parent and self._parent.exists(name))

    def exists_in_current_scope(self, name: str) -> bool:
        """Check if variable exists only in current scope"""
        return name in self._variables

    def get(self, name: str, line: int):
        info = self._require_variable(name, line)
        return info.value

    def set(self, name: str, value, line: int):
        info = self._require_variable(name, line)
        expected_type, _ = resolve_type(info.var_type)
        if type(value) != expected_type:
            raise WrongTypeError(name, expected_type, type(value), line)
        info.value = value

    def get_info(self, name: str, line: Optional[int] = None) -> VariableInfo:
        return self._require_variable(name, line or 0)

    def type_of(self, name: str) -> Optional[str]:
        info = self._find_in_chain(name)
        return info.var_type if info else None

    def scope_of(self, name: str) -> Optional[str]:
        info = self._find_in_chain(name)
        return info.scope if info else None

    def declared_at(self, name: str) -> Optional[int]:
        info = self._find_in_chain(name)
        return info.declaration_line if info else None

    def _find_in_chain(self, name: str) -> Optional[VariableInfo]:
        """Find variable in this scope or parent scopes (shadowing resolution)"""
        if name in self._variables:
            return self._variables[name]
        elif self._parent:
            return self._parent._find_in_chain(name)
        return None

    def _require_variable(self, name: str, line: int) -> VariableInfo:
        info = self._find_in_chain(name)
        if not info:
            raise VariableNotFoundError(name, line)
        return info

    def get_all_visible_variables(self) -> Dict[str, VariableInfo]:
        """Get all variables visible from this scope (including shadowed ones)"""
        all_vars = {}
        
        # Start from root and work down, so current scope overrides parents
        if self._parent:
            all_vars.update(self._parent.get_all_visible_variables())
        
        # Current scope variables override parent variables
        all_vars.update(self._variables)
        return all_vars

    def get_scope_chain(self) -> List[str]:
        """Get the chain of scope names from root to current"""
        chain = []
        if self._parent:
            chain.extend(self._parent.get_scope_chain())
        if self._scope:
            chain.append(self._scope)
        return chain

    def items(self):
        """Items only from current scope"""
        return self._variables.items()

    def __iter__(self):
        return iter(self._variables)

    def __repr__(self):
        parent_info = f" -> {self._parent._scope}" if self._parent else ""
        return f"{self._scope}{parent_info}: ({list(self._variables.keys())})"


# Usage example for your interpreter:
class ScopeManager:
    """Helper class to manage scope transitions in your interpreter"""
    
    def __init__(self):
        self.current_scope = VariableContainer("global")
        self.scope_stack = [self.current_scope]
    
    def enter_scope(self, scope_name: str) -> VariableContainer:
        """Enter a new scope (e.g., for loops, functions, blocks)"""
        new_scope = self.current_scope.create_child_scope(scope_name)
        self.current_scope = new_scope
        self.scope_stack.append(new_scope)
        return new_scope
    
    def exit_scope(self) -> VariableContainer:
        """Exit current scope and return to parent"""
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
            self.current_scope = self.scope_stack[-1]
        return self.current_scope
    
    def get_current_scope(self) -> VariableContainer:
        return self.current_scope