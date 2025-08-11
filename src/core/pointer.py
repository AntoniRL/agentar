# -*- coding: utf-8 -*- 
# core/pointer.py
# Pointer: represents a reference to a value in the Agentar system

import threading
from copy import deepcopy

class TypedMeta(type):
    """Meta class for typed structures to enforce type checking on initialization and item assignment."""
    def __repr__(cls):
        return f"<class {cls.__name__}>"

    def __str__(cls):
        return f"<class '{cls.__name__}'>"


class Pointer(metaclass=TypedMeta):
    def __init__(self, target = None):
        self._target: list = target # Using a list to allow mutable reference
        self._address = hex(id(self._target)) # Get the memory address of the target object
        self._lock = threading.RLock()

    def get(self):
        with self._lock:
            return self._target

    def set(self, new_target):
        with self._lock:
            current = self._target
            if hasattr(current, "assign") and isinstance(new_target, type(current)):
                self._target.assign(new_target)
            else:
                self._target = new_target

    def __deepcopy__(self, memodict=None): # TODO: is it necessary?
        if memodict is None:
            memodict = {}
        with self._lock:
            # Check if the object is already in memodict
            if id(self) in memodict:
                return memodict[id(self)]
            
            copied_target = deepcopy(self._target, memodict)
            new_pointer = type(self)(copied_target)

            # Add to memodict
            memodict[id(self)] = new_pointer
            return new_pointer

    def __repr__(self):
        with self._lock:
            return f"Pointer(target={repr(self._target)}, addr={self._address})"

    def __str__(self):
        return str(self._address)