# -*- coding: utf-8 -*-
# runtime/agent_instance/expression_evaluator.py
# ExpressionEvaluator: evaluates expressions in the context of an agent instance

class ExpressionEvaluator:
    def __init__(self, agent):
        self.agent = agent

    def eval_expr(self, expr, local_scope):
        if expr is None:
            return None
        expr_type = type(expr).__name__
        handler = getattr(self, f"eval_{expr_type}", None)
        if handler:
            return handler(expr, local_scope)
        raise NotImplementedError(f"Unhandled expression type: {expr_type}")

    def eval_LiteralNode(self, expr, _):
        return expr.value

    def eval_VarRefNode(self, expr, local_scope):
        if local_scope.exists(expr.name):
            return local_scope.get(expr.name)
        if self.agent._var_scope.exists(expr.name):
            return self.agent._var_scope.get(expr.name)
        raise NameError(f"Variable '{expr.name}' not found")
