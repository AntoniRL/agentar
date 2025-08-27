# core/agent_id.py

class AgentId:
    def __init__(self, path: str = "."):
        self.path = path  # e.g., ".1.2.3"

    def __str__(self):
        return self.path

    def __eq__(self, other):
        return isinstance(other, AgentId) and self.path == other.path

    def parent(self):
        # Return parent ID
        parts = self.path.strip('.').split('.')
        if len(parts) <= 1:
            return None
        return AgentId('.' + '.'.join(parts[:-1]))

    def child(self, index: int):
        return AgentId(self.path + f".{index}")