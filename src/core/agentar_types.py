# core/agentarTypes.py

from core.agent_id import AgentId
from ast_tree.nodes import PointerTypeNode, BaseTypeNode
from core.pointer import *
from runtime.message_instance import MessageInstance

from enum import Enum


# Global mapping: Agentar type string → Python type
AGENTAR_TYPE_MAP = {
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
    "agentid": AgentId,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "void": 'void',  # Special case for void type
}


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
        "msgType_deny": MessageType.DENY,
    }
    return mapping.get(expr.value)


# Function to resolve AST type nodes to Agentar types and their default values.
def resolve_type(var_type):
    if isinstance(var_type, PointerTypeNode):
        inner = var_type.inner
        if isinstance(inner, BaseTypeNode):
            if inner.name == "int": return IntPointer, None
            elif inner.name == "float": return FloatPointer, None
            elif inner.name == "bool": return BoolPointer, None
            elif inner.name == "string": return StringPointer, None
            elif inner.name == "list": return ListPointer, None
            elif inner.name == "dict": return DictPointer, None
            elif inner.name == "tuple": return TuplePointer, None
            else: raise TypeError(f"Unsupported pointer base type: {inner.name}")  
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
        elif name == "list":
            return list, []
        elif name == "dict":
            return dict, {}
        elif name == "agentid":
            return AgentId, AgentId()
        elif name == "void":
            return 'void', None
        elif name == "tuple":
            return tuple, ()
    else:
        raise TypeError(f"Unknown AST type: {type(var_type)}")


# Function to resolve normal types (not AST nodes) to Agentar types and their default values.
def resolve_type_normal(var_type):
    if var_type == AgentId:
        return var_type, None
    elif var_type == MessageInstance:
        return var_type, None
    elif isinstance(var_type, (int, float, str, bool)):
        return var_type, None
    elif var_type == list:
        return var_type, []
    elif var_type == dict:
        return var_type, {}
    elif var_type == tuple:
        return var_type, ()