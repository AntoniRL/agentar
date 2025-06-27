# -*- coding: utf-8 -*-
# runtime/errors.py
# Custom exceptions and error listeners used in the Agentar interpreter

from antlr4.error.ErrorListener import ErrorListener

# =============================================================================
# 1. Base class for runtime errors
# =============================================================================

class AgentarRuntimeError(Exception):
    """Base class for all Agentar runtime errors."""
    def __init__(self, message, line=None):
        super().__init__(message)
        self.line = line

    def __str__(self):
        if self.line is not None:
            return f"ERROR at line {self.line}: {super().__str__()}"
        else:
            return f"ERROR: {super().__str__()}" 


# =============================================================================
# 2. errors for various runtime issues
# =============================================================================

class VariableNotFoundError(AgentarRuntimeError):
    """Raised when a variable is used but not declared."""
    def __init__(self, variable_name, line=None):
        message = f"Variable '{variable_name}' not found."
        super().__init__(message, line)


class VariableAlreadyDeclaredError(AgentarRuntimeError):
    """Raised when a variable is declared more than once."""
    def __init__(self, variable_name, line=None, first_declaration_line=None):
        message = f"Variable '{variable_name}' is already declared at line {first_declaration_line}."
        super().__init__(message, line)


class AgentNameAlreadyDeclaredError(AgentarRuntimeError):
    """Raised when an agent is declared more than once."""
    def __init__(self, agent_name, line=None, first_declaration_line=None):
        message = f"Agent '{agent_name}' is already declared at line {first_declaration_line}."
        super().__init__(message, line)


class AgentNotFoundError(AgentarRuntimeError):
    """Raised when an agent is referenced but not declared."""
    def __init__(self, agent_name, line=None):
        message = f"Agent '{agent_name}' not found."
        super().__init__(message, line)


class MessageAlreadyDeclaredError(AgentarRuntimeError):
    """Raised when a message is declared more than once."""
    def __init__(self, message_name, line=None, first_declaration_line=None):
        message = f"Message '{message_name}' is already declared at line {first_declaration_line}."
        super().__init__(message, line)


class MessageNotFoundError(AgentarRuntimeError):
    """Raised when a message is referenced but not declared."""
    def __init__(self, message_name, line=None):
        message = f"Message '{message_name}' not found."
        super().__init__(message, line)


class ASTNodeAlreadyDeclaredError(AgentarRuntimeError):
    """Raised when an AST node is declared more than once."""
    def __init__(self, node_name, container_type, line=None, first_declaration_line=None):
        message = f"{container_type} name '{node_name}' is already declared at line {first_declaration_line}."
        super().__init__(message, line)


class ASTNodeNotFoundError(AgentarRuntimeError):
    """Raised when an AST node is not found."""
    def __init__(self, node_name, container_type, line=None):
        message = f"{container_type} of type '{node_name}' not found."
        super().__init__(message, line)





# =============================================================================
# 3. Error listener for ANTLR
# =============================================================================

# This error listener will throw a SyntaxError when a syntax error is encountered
class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Line {line}:{column} {msg}")


