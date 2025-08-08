# -*- coding: utf-8 -*- 
# core/variable_info.py
# VariableInfo: represents information about a variable in the Agentar system

from typing import Optional

class VariableInfo:
    def __init__(self, name: str, value, var_type, scope: str, declaration_line: Optional[int] = None):
        self.name: str = name
        self.value = value
        self.var_type = var_type
        self.scope = scope
        self.declaration_line = declaration_line

    def __repr__(self):
        return f"VariableInfo(name={self.name}, var_type={self.var_type}, scope={self.scope}, value={self.value})"
