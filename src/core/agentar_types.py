# -*- coding: utf-8 -*- 
# core/agentar_types.py
# File with utility functions and types for the Agentar system

from os import name
from runtime.errors import WrongTypeError
from core.agent_id import AgentId
from ast_tree.nodes import ASTNode, PointerTypeNode, BaseTypeNode, ListTypeNode, DictTypeNode, TupleTypeNode, AnyTypeNode
from core.pointer import Pointer
from runtime.message_instance import MessageInstance
from core.typed_structures import TypedList, TypedDict, TypedTuple

from enum import Enum

class MessageType(str, Enum):
    INFORM = "msgType_inform"
    ASK = "msgType_ask"
    REQUEST = "msgType_request"
    CONFIRM = "msgType_confirm"
    DENY = "msgType_deny"


def get_message_type(expr):
    mapping = {
        "msgType_inform": MessageType.INFORM,
        "msgType_ask": MessageType.ASK,
        "msgType_request": MessageType.REQUEST,
        "msgType_confirm": MessageType.CONFIRM,
        "msgType_deny": MessageType.DENY
    }
    return mapping.get(expr.value)


# Global mapping: Agentar type string → Python type
AGENTAR_TYPE_MAP = {
    "int": int,
    "float": float,
    "str": str,
    "bool": bool,
    "agentid": AgentId,
    "void": 'void',  # Special case for void type
}


# Function to resolve AST type nodes to Agentar types and their default values.
def resolve_type(var_type):
    if isinstance(var_type, ASTNode):
        if isinstance(var_type, PointerTypeNode):
            inner_type, _ = resolve_type(var_type.inner_type)
            return Pointer, Pointer(inner_type)
        
        elif isinstance(var_type, ListTypeNode):
            inner_type, default_value = resolve_type(var_type.inner_type)
            return TypedList, TypedList(inner_type, default_value)

        elif isinstance(var_type, DictTypeNode):
            key_type, _ = resolve_type(var_type.key_type)
            value_type, _ = resolve_type(var_type.value_type)
            return dict, TypedDict(key_type, value_type)
    
        elif isinstance(var_type, TupleTypeNode):
            elements_type = [resolve_type(element)[0] for element in var_type.elements_type]
            return tuple, TypedTuple(elements_type)
        
        elif isinstance(var_type, AnyTypeNode):
            return AnyTypeNode, None

        elif isinstance(var_type, BaseTypeNode):
            name = var_type.name
            if name == "int":
                return int, None
            elif name == "float":
                return float, None
            elif name == "bool":
                return bool, None
            elif name == "string":
                return str, None
            elif name == "agentid":
                return AgentId, AgentId()
            elif name == "void":
                return 'void', None
        else:
            raise TypeError(f"Unknown AST type: {type(var_type)}")
    else:
        if var_type == AgentId:
            return var_type, None
        elif var_type == MessageInstance:
            return var_type, None
        elif isinstance(var_type, (int, float, str, bool)):
            return var_type, None
        elif var_type == list:
            raise NotImplementedError("TypedList is not implemented yet")
        elif var_type == dict:
            raise NotImplementedError("TypedDict is not implemented yet")
        elif var_type == tuple:
            raise NotImplementedError("TypedTuple is not implemented yet")
        else:
            raise TypeError(f"Unknown type: {var_type}")
