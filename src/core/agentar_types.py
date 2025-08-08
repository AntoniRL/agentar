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
            inner_type, _ = resolve_type(var_type.inner)
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
        


def check_type_compatibility(name, value, type_reference, declaration_line):
    pass





# def check_inner_type_compatibility(name, value, type_reference, declaration_line, place_of_error):
#     # check if every element is of the correct type
#     for index, element in enumerate(value):
#         # when the type_reference is a basicType, we check if the element is of the correct type
#         if not isinstance(type_reference, basicType):
#             if type(element) != type_reference:
#                 place_of_error.append(index)
#                 raise WrongTypeError(name, type_reference, type(element), declaration_line, f"Element at index {place_of_error[:]} is of the wrong type.")
            
#         # when the type_reference is a listType,  we check if the element is of the correct type
#         elif isinstance(type_reference, listType):
#             if type(element) != type_reference._type:
#                 place_of_error.append(index)
#                 raise WrongTypeError(name, type_reference, type(element), declaration_line, f"Element at index {place_of_error[:]} is of the wrong type.")
#             place_of_error.append(index)
#             check_inner_type_compatibility(name, element, type_reference.inner_type, declaration_line, place_of_error)
#             place_of_error.pop()  # Remove the index after checking inner type compatibility

#         # when the type_reference is a dictType, we check if the value and key are of the correct type
#         elif isinstance(type_reference, dictType):
#             # 'element' is a 'key'
#             if type(element) != type_reference.key_type:
#                 place_of_error.append(index)
#                 raise WrongTypeError(name, type_reference.key_type, type(element), declaration_line, f"Key in dict '{element}' is of the wrong type. (index {place_of_error[:]}).")
#             elif type(value[element]) != type_reference.value_type:
#                 place_of_error.append(index)
#                 raise WrongTypeError(name, type_reference.value_type, type(value[element]), declaration_line, f"Value in dict '{value[element]}' is of the wrong type. (index {place_of_error[:]}).")
#             # place_of_error.append(index)
#             # check_inner_type_compatibility

#         # when the type_reference is a tupleType, we check if the element is of the correct type
#         elif isinstance(type_reference, tupleType):
#             pass



# def check_type_compatibility(name, value, type_reference, declaration_line):
#     """
#     Check if the value is of the correct type according to the type_reference.
#     """
#     if not isinstance(type_reference, basicType):
#         if type(value) != type_reference:
#             raise WrongTypeError(name, type_reference, type(value), declaration_line)
#     else:
#         if type(value) != type_reference._type:
#             raise WrongTypeError(name, type_reference._type, type(value), declaration_line)
#         if isinstance(type_reference, listType):
#             check_inner_type_compatibility(name, value, type_reference.inner_type, declaration_line, place_of_error=[])
#         elif isinstance(type_reference, dictType):
#             check_inner_type_compatibility(name, value, type_reference, declaration_line, place_of_error=[])

#     # TODO: What with pointer types?