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
        message = f"{container_type} with name '{node_name}' not found."
        super().__init__(message, line)


class WrongTypeError(AgentarRuntimeError):
    """Raised when a value is of the wrong type."""
    def __init__(self, var_name, expected_type, actual_type, line=None):
        message = f"'{var_name}' expected type '{expected_type}', but got '{actual_type}'."
        super().__init__(message, line)


class IndexOutOfRangeError(AgentarRuntimeError):
    """Raised when an index is out of range for a list or array."""
    def __init__(self, index, length, line=None):
        message = f"Index {index} out of range for length {length}."
        super().__init__(message, line)


class KeyNotFoundError(AgentarRuntimeError):
    """Raised when a key is not found in a dictionary."""
    def __init__(self, key, line=None):
        message = f"Key '{key}' not found in dictionary."
        super().__init__(message, line)


class UnsupportedOperatorError(AgentarRuntimeError):
    """Raised when an unsupported operator is used."""
    def __init__(self, operator, line=None):
        message = f"Unsupported operator '{operator}'."
        super().__init__(message, line)


class NoValueInActionCall(AgentarRuntimeError):
    def __init__(self, param_name, line_of_call_action, line=None):
        message = f"Parameter '{param_name}' has no value. Declare it in action call in line {line_of_call_action}"
        super().__init__(message, line)


class MismatchTypeWithDeclarationError(AgentarRuntimeError):
    def __init__(self, expected_type, actual_type, line=None):
        message = f"Mismach of message type and declaration. Message type '{expected_type}' but declaration '{actual_type}'."
        super().__init__(message, line)


class MismatchMessageContentError(AgentarRuntimeError):
    """Raised when the content of a message does not match its declaration."""
    def __init__(self, message_type, expected_length, actual_length, line=None):
        message = f"Message '{message_type}' content mismatch: expected {expected_length} fields, but got {actual_length}."
        super().__init__(message, line) 


class FieldWithNoneValueError(AgentarRuntimeError):
    """Raised when a field is accessed but not declared."""
    def __init__(self, field_name, line=None):
        message = f"Field '{field_name}' doas not have a value. Declare it in the agent declaration or agent spawn() method."
        super().__init__(message, line)

# =============================================================================
# 3. Error listener for ANTLR
# =============================================================================

# This error listener will throw a SyntaxError when a syntax error is encountered
class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"Line {line}:{column} {msg}")


