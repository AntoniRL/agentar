# src/ast_tree/nodes.py

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Union

# === Base AST class ===
@dataclass
class ASTNode:
    pass

# === Program and declarations ===
@dataclass
class ProgramNode(ASTNode):
    declarations: List[ASTNode]  # AgentNode, MotherNode, MessageDeclNode


@dataclass
class AgentNode(ASTNode):
    name: str
    body: List[ASTNode]  # FieldSectionNode, InitSectionNode, etc.


@dataclass
class MotherNode(ASTNode):
    body: List[ASTNode]


@dataclass
class MessageDeclNode(ASTNode):
    name: str
    fields: List[VariableDeclNode]


# === Agent sections ===
@dataclass
class FieldSectionNode(ASTNode):
    declarations: List[VariableDeclNode]


@dataclass
class BeliefSectionNode(ASTNode):
    declarations: List[VariableDeclNode]


@dataclass
class SeanseSectionNode(ASTNode):
    statements: List[ASTNode]


@dataclass
class GoalSectionNode(ASTNode):
    goals: List[ASTNode]
    merge_condition: ASTNode


@dataclass
class GoalBlockNode(ASTNode):
    name: str
    condition: List[ASTNode]


@dataclass
class RulesSectionNode(ASTNode):
    rules: List[ASTNode]


@dataclass
class InitSectionNode(ASTNode):
    statements: List[ASTNode]


@dataclass
class DestroySectionNode(ASTNode):
    statements: List[ASTNode]


@dataclass
class ReceiveSectionNode(ASTNode):
    name: str
    blocks: List[ASTNode]  # WhenBlockNode or statements


@dataclass
class WhenBlockNode(ASTNode):
    conditions: List[ASTNode]
    statements: List[ASTNode]


@dataclass
class ActionNode(ASTNode):
    name: str
    parameters: List[ParameterNode]
    return_type: str
    body: List[ASTNode]


@dataclass
class ParameterNode(ASTNode):
    param_type: str
    name: str


# === Statements ===
@dataclass
class PrintNode(ASTNode):
    values: List[ASTNode]


@dataclass
class AssignmentNode(ASTNode):
    target: Union[ASTNode]
    value: ASTNode
    index: Optional[ASTNode] = None

@dataclass
class IndexRangeNode(ASTNode):
    start: Optional[ASTNode] = None
    end: Optional[ASTNode] = None


@dataclass
class VariableDeclNode(ASTNode):
    var_type: str
    name: str
    value: Optional[ASTNode] = None


@dataclass
class SendNode(ASTNode):
    to: ASTNode
    message: ASTNode
    msg_type: Optional[str] = None


@dataclass
class SendToChildrenNode(ASTNode):
    agent_type: ASTNode
    message: ASTNode
    msg_type: Optional[str] = None


@dataclass
class SendToSiblingsNode(ASTNode):
    agent_type: ASTNode
    message: ASTNode
    msg_type: Optional[str] = None


@dataclass
class SpawnNode(ASTNode):
    agent_type: str
    args: List[ASTNode]


@dataclass
class KillNode(ASTNode):
    agent_id: ASTNode


@dataclass
class KillChildrenNode(ASTNode):
    agent_type: ASTNode


@dataclass
class DoNode(ASTNode):
    name: str
    variables: List[ASTNode]



# === Expressions ===
@dataclass
class LiteralNode(ASTNode):
    value: Union[int, float, str, bool]


@dataclass
class VarRefNode(ASTNode):
    name: str


@dataclass
class BinaryOpNode(ASTNode):
    op: str
    left: ASTNode
    right: ASTNode


@dataclass
class NotNode(ASTNode):
    operand: ASTNode


@dataclass
class IndexAccessNode(ASTNode):
    base: ASTNode
    index: ASTNode

@dataclass
class SliceAccessNode(ASTNode):
    base: ASTNode
    start: Optional[ASTNode] = None
    end: Optional[ASTNode] = None


@dataclass
class MessageInitNode(ASTNode):
    message_type: str
    fields: dict  # str -> ASTNode


@dataclass
class SelfAccessNode(ASTNode):
    path: List[str]  # e.g., ['self.', 'text', ...]


@dataclass
class MsgAccessNode(ASTNode):
    path: List[str]  # e.g., ['msg', 'content', 'text']


@dataclass
class BelAccessNode(ASTNode):
    path: List[str]  # e.g., ['bel', 'text', ...]


@dataclass
class MapLiteralNode(ASTNode):
    entries: dict  # Dict[str, ASTNode]


@dataclass
class ListLiteralNode(ASTNode):
    elements: List[ASTNode]


@dataclass
class AgentIdNode(ASTNode):
    path: str  # np. '.1.2.3'


@dataclass
class SleepNode(ASTNode):
    duration: ASTNode


@dataclass
class ReturnNode(ASTNode):
    value: Optional[ASTNode] = None


@dataclass
class IfStmtNode(ASTNode):
    conditions: List[ASTNode]
    statements: List[ASTNode]
    elseStmt: ASTNode


@dataclass
class ElseStmtNode(ASTNode):
    statements: List[ASTNode]


@dataclass
class ForLoopNode(ASTNode):
    initialize: ASTNode
    condition: ASTNode
    update: ASTNode
    body: List[ASTNode]


@dataclass
class WhileLoopNode(ASTNode):
    condition: ASTNode
    body: List[ASTNode]


@dataclass
class BreakNode(ASTNode):
    pass


@dataclass
class SenseNode(ASTNode):
    pass


@dataclass
class GoalCheckNode(ASTNode):
    goal_name: str


@dataclass
class GetFromWorldNode(ASTNode):
    x: ASTNode
    y: ASTNode

@dataclass
class SetInWorldNode(ASTNode):
    x: ASTNode
    y: ASTNode
    value: ASTNode


@dataclass
class LenNode(ASTNode):
    base: ASTNode


@dataclass
class TypeExprNode(ASTNode):
    base: ASTNode


@dataclass
class BaseTypeNode(ASTNode):
    name: str  # np. 'int', 'list', 'bool', ...

@dataclass
class PointerTypeNode(ASTNode):
    inner: ASTNode  # inny TypeNode, np. BaseTypeNode lub kolejny PointerTypeNode


@dataclass
class AddressOfExprNode(ASTNode):
    variable: ASTNode