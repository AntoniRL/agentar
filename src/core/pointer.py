# -*- coding: utf-8 -*- 
# core/pointer.py
# Pointer: represents a reference to a value in the Agentar system

import threading

class Pointer:
    def __init__(self, target = None):
        self._target: list = [target] # Using a list to allow mutable reference
        self._address = hex(id(self._target)) # Get the memory address of the target object
        self._lock = threading.RLock()

    def get(self):
        with self._lock:
            return self._target[0]

    def set(self, new_target):
        with self._lock:
            current = self._target[0]
            if hasattr(current, "assign") and isinstance(new_target, type(current)):
                self._target[0].assign(new_target)
            else:
                self._target[0] = new_target

    def __deepcopy__(self, memodict={}):
        return self

    def __repr__(self):
        with self._lock:
            return f"Pointer(target={repr(self._target)}, addr={self._address})"

    def __str__(self):
        return str(self._address)