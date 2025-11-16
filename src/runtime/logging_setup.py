# -*- coding: utf-8 -*- 
# runtime/logging_setup.py
# Logging setup for Agentar agent thread

import logging, os, re
from logging.handlers import RotatingFileHandler

def _safe_filename(name: str) -> str:
    return re.sub(r'[^A-Za-z0-9_.-]+', '_', name)

def get_agent_logger(agent_id: str) -> logging.Logger:
    """
    - File: logs/<agent_id>.log
    - Console: shows WARNING/ERROR only from this agent
    """
    name = f"agentar.agent.{agent_id}"
    logger = logging.getLogger(name)
    if getattr(logger, "_configured", False):
        return logger

    os.makedirs("logs/agents", exist_ok=True)

    # --- handler to the file: logs/agents/<agent_id>.log ---
    fh = RotatingFileHandler(
        f"logs/agents/{_safe_filename(agent_id)}.log",
        mode='w',
        maxBytes=5_000_000,
        backupCount=3,
        encoding="utf-8"
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(
        "[%(asctime)s] %(levelname)s %(threadName)s %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    ))

    # for console
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)   # you can raise it to WARNING if you want
    ch.setFormatter(logging.Formatter(
        "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    ))

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.addHandler(ch)        # to show in console
    logger.propagate = False     # do not duplicate to the root logger
    logger._configured = True
    return logger
