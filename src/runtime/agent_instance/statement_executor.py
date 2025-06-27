# -*- coding: utf-8 -*-
# runtime/agent_instance/statement_executor.py
# StatementExecutor: executes statements in the context of an agent instance


class StatementExecutor:
    def __init__(self, agent):
        self.agent = agent

    def execute_stmt(self, stmt, local_scope):
        if stmt is None:
            return None
        stmt_type = type(stmt).__name__
        handler = getattr(self, f"handle_{stmt_type}", None)
        if handler:
            return handler(stmt, local_scope)
        raise NotImplementedError(f"Unhandled statement type: {stmt_type}")