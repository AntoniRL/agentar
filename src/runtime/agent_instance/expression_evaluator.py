# -*- coding: utf-8 -*-
# runtime/agent_instance/expression_evaluator.py
# ExpressionEvaluator: evaluates expressions in the context of an agent instance

from ast_tree.nodes import *
from core.agentar_types import MessageType
from core.agent_id import AgentId
from core.agentar_types import resolve_type
from core.pointer import Pointer
from runtime.errors import *
from core.variable_info import VariableInfo
from core.typed_structures import TypedList, TypedDict, TypedTuple


from copy import deepcopy
import random

class ExpressionEvaluator:
    def __init__(self, agent):
        self.agent = agent

    def eval_expr(self, expr, local_vars=None, message=None, line=None, deref=False):
        match expr:

            case LiteralNode(value=value):
                match value:
                    case 'msgType_inform':
                        return MessageType.INFORM
                    case 'msgType_ask':
                        return MessageType.ASK
                    case 'msgType_request':
                        return MessageType.REQUEST
                    case 'msgType_confirm':
                        return MessageType.CONFIRM
                    case 'msgType_deny':
                        return MessageType.DENY
                    case _:
                        return value


            case AgentIdNode(path=path):
                return AgentId(path)


            case AgentId():
                return expr  # Return the AgentId instance as is
            

            case NegExprNode(base=base, _line=line):
                value = self.eval_expr(base, local_vars, message, line, deref)
                if isinstance(value, (int, float)):
                    return -value
                else:
                    raise WrongTypeError(base.name, "int or float", type(value).__name__, line) 
            

            case NoneExprNode():
                return None
            

            case ParentShadowNode(base=base, _line=line):
                value = self.eval_expr(base, local_vars._parent_container, message, line, deref)
                return value
            

            case VarRefNode(name=name, _line=line):
                if name == "_":
                    return "_"
                else:
                    return local_vars.get(name, line, deref)

            case BaseTypeNode():
                return resolve_type(expr)[0] # TODO: Check if it works correctly with all types
            

            case LenNode(base=base, _line=line):
                value = self.eval_expr(base, local_vars, message, line, deref)
                if isinstance(value, (list, str, tuple, dict)):
                    return len(value)
                else:
                    raise WrongTypeError(base.name, "list, string, tuple or dict", type(value).__name__, line)
                

            case AbsExprNode(base=base, _line=line):
                value = self.eval_expr(base, local_vars, message, line, deref)
                if isinstance(value, (int, float)):
                    return abs(value)
                else:
                    raise WrongTypeError(base.name, "int or float", type(value).__name__, line)
                

            case TypeExprNode(base=base, _line=line):
                value = self.eval_expr(base, local_vars, message, line, deref)
                return type(value)
            

            case ListLiteralNode(elements=elements, _line=line):
                newList = TypedList(AnyTypeNode)
                for item in elements:
                    newList.append(self.eval_expr(item, local_vars, message, line, deref))
                return newList

            case IndexAccessNode(name=name, index=index, _line=line):
                base_value = self.eval_expr(name, local_vars, message, line, deref)
                index_value = self.eval_expr(index, local_vars, message, line, deref)
                if type(base_value) in (TypedList, TypedTuple):
                    if isinstance(index_value, int):
                        if index_value < -len(base_value) or index_value >= len(base_value):
                            raise IndexOutOfRangeError(index_value, len(base_value), line)
                        else:
                            return base_value[index_value]
                    else:
                        raise WrongTypeError("index", int, type(index_value), line)
                elif type(base_value) == TypedDict:
                    return base_value[index_value]
                elif isinstance(base_value, list):
                    return base_value[index_value]
                else:
                    raise WrongTypeError("base", "TypedList, TypedDict, TypedTuple or Pointer", type(base_value), line)
                    

            case SliceAccessNode(base=base, start=start, end=end, _line=line):
                base_value = self.eval_expr(base, local_vars, message, line, deref)
                start_value = self.eval_expr(start, local_vars, message, line, deref) if start is not None else 0
                end_value = self.eval_expr(end, local_vars, message, line, deref) if end is not None else None
                if type(base_value) in (TypedList, TypedTuple):
                    if end_value is None: end_value = len(base_value)
                    if isinstance(start_value, int) and isinstance(end_value, int):
                        if start_value <= abs(len(base_value)) and end_value <= abs(len(base_value)):
                            return base_value[start_value:end_value]
                        else:
                            raise IndexOutOfRangeError(f"slice [{start_value}:{end_value}]", len(base_value), line)
                    else:
                        raise WrongTypeError("slice indices", "int", f"{type(start_value)} and {type(end_value)}", line)
                else:
                    raise WrongTypeError("base", "list or tuple", type(base_value), line)
            

            case SelfAccessNode(path=path, _line=line):
                name = path[1]
                if hasattr(self.agent, name):
                    return getattr(self.agent, name)
                elif self.agent._fields.exists(name):
                    return self.agent._fields.get(name, line, deref)
                else:
                    raise VariableNotFoundError(f"self.{name}", line)
                

            case MsgAccessNode(path=path, _line=line):
                name = path[1]
                if hasattr(message, name):
                    return getattr(message, name)
                elif message._content.exists(name):
                    return message._content.get(name, line, deref)
                else:
                    raise VariableNotFoundError(f"msg.{name}", line)
                

            case MessageInitNode():
                return self.agent._message_handler.handle_message_init(expr, local_vars)
                
            
            case BelAccessNode(path=path, _line=line):
                name = path[1]
                if self.agent._beliefs.exists(name):
                    return self.agent._beliefs.get(name, line, deref)
                else:
                    raise VariableNotFoundError(f"bel.{name}", line)
                

            case TupleLiteralNode(elements=elements, _line=line):
                items = tuple(self.eval_expr(item, local_vars, message, line, deref) for item in elements)
                return TypedTuple(AnyTypeNode, items)
            

            case DictValuesNode(base=base, _line=line):
                base_value = self.eval_expr(base, local_vars, message, line, deref)
                if isinstance(base_value, TypedDict):
                    return base_value.values()
                else:
                    raise WrongTypeError(base_value, "dict", type(base_value).__name__, line)
                

            case DictGetNode(base=base, key=key, _line=line):
                base_value = self.eval_expr(base, local_vars, message, line, deref)
                key_value = self.eval_expr(key, local_vars, message, line, deref)
                if isinstance(base_value, TypedDict):
                    if key_value in base_value:
                        return base_value[key_value]
                    else:
                        return None
                else:
                    raise WrongTypeError(base_value, "dict", type(base_value).__name__, line)
                

            case DerefExprNode(pointer=pointer, _line=line):
                return self.eval_expr(pointer, local_vars, message, line, deref=True)
                
            

            case AddressOfExprNode(variable=variable, _line=line):
                if isinstance(variable, SelfAccessNode):
                    local_pointer = self.agent._fields.get_pointer(variable.path[1], line)
                else:
                    local_pointer = local_vars.get_pointer(variable.name, line)
                return local_pointer


            case RandomExprNode(start=start, end=end, _line=line):
                start = self.eval_expr(start, local_vars, message, line, deref)
                end = self.eval_expr(end, local_vars, message, line, deref)
                if isinstance(start, int) and isinstance(end, int):
                    if start > end:
                        raise ValueError(f"Start value {start} cannot be greater than end value {end}.")
                    return random.randint(start, end)
                else:
                    raise WrongTypeError("random() parameters", "int", f"{type(start).__name__} and {type(end).__name__}", line)   # TODO: check the appiriance of error in the tests
                

            case BinaryOpNode(left=left, right=right, op=op, _line=line):
                if isinstance(left, BinaryOpNode) or not isinstance(left, (bool, int, float, str)):
                    left = self.eval_expr(left, local_vars, message, line, deref)
                if isinstance(right, BinaryOpNode) or not isinstance(right, (bool, int, float, str)):
                    right = self.eval_expr(right, local_vars, message, line, deref)

                match op:
                    case '+':
                        return left + right
                    case '-':
                        return left - right
                    case '*':
                        return left * right
                    case '/':
                        if right == 0:
                            raise ZeroDivisionError("Division by zero is not allowed.")
                        return left / right
                    case '%':
                        if right == 0:
                            raise ZeroDivisionError("Modulo by zero is not allowed.")
                        return left % right
                    case '**':
                        return left ** right
                    case '==':
                        return left == right
                    case '!=':
                        return left != right
                    case '<':
                        return left < right
                    case '<=':
                        return left <= right
                    case '>':
                        return left > right
                    case '>=':
                        return left >= right
                    case 'AND':
                        return left and right
                    case 'OR':
                        return left or right
                    case 'XOR':
                        return left ^ right
                    case 'NOT':
                        return not left
                    case _:
                        raise UnsupportedOperatorError(op, line)