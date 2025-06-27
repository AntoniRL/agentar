# core/agentarTypes.py

from core.agent_id import AgentId
from ast_tree.nodes import PointerTypeNode, BaseTypeNode
from core.pointer import *


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
            return int, 0
        elif name == "float":
            return float, 0.0
        elif name == "bool":
            return bool, False
        elif name == "string":
            return str, ""
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
    

def check_if_var_is_pointer(variable):
    """
    Check if the given variable type is a pointer type.
    """
    variable_type = type(variable)
    return variable_type in (IntPointer, FloatPointer, BoolPointer, StringPointer, ListPointer)   


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
