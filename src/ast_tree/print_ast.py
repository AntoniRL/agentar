# print_ast.py

from rich.tree import Tree
from rich import print
from builder import AgentarToASTBuilder
from nodes import ASTNode
from antlr4 import InputStream, CommonTokenStream
from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser

def build_rich_tree(node: ASTNode, label="AST"):
    tree = Tree(label)
    _build_tree(tree, node)
    return tree

def _build_tree(rich_tree, node):
    from dataclasses import is_dataclass

    if isinstance(node, list):
        for item in node:
            _build_tree(rich_tree, item)
    elif is_dataclass(node):
        branch = rich_tree.add(f"[bold]{node.__class__.__name__}[/]")
        for field in node.__dataclass_fields__:
            value = getattr(node, field)
            if isinstance(value, (ASTNode, list)):
                sub = branch.add(f"[cyan]{field}[/]")
                _build_tree(sub, value)
            else:
                branch.add(f"[cyan]{field}[/]: {value}")
    else:
        rich_tree.add(str(node))

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "r") as f:
        source = f.read()

    lexer = AgentarLexer(InputStream(source))
    tokens = CommonTokenStream(lexer)
    parser = AgentarParser(tokens)
    tree = parser.program()

    builder = AgentarToASTBuilder()
    ast_root = builder.visit(tree)

    rich_tree = build_rich_tree(ast_root)
    print(rich_tree)

