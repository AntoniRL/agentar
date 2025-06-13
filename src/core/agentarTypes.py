# core/agentarTypes.py

from core.agentid import AgentId

# Global mapping: Agentar type string → Python type
AGENTAR_TYPE_MAP = {
    "int": int,
    "float": float,
    "string": str,
    "bool": bool,
    "agentid": AgentId,
    "list": list,
    "dict": dict
}
