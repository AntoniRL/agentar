# src/core/pointer.py
# -*- coding: utf-8 -*-
# Pointer class: thread-safe reference wrapper for mutable objects

import threading
from copy import deepcopy


def get_pointer_type(value):
    """
    Returns the type of pointer based on the value type.
    """
    if isinstance(value, int):
        return IntPointer
    elif isinstance(value, float):
        return FloatPointer
    elif isinstance(value, bool):
        return BoolPointer
    elif isinstance(value, str):
        return StringPointer
    elif isinstance(value, list):
        return ListPointer
    else:
        raise TypeError(f"Unsupported type for pointer: {type(value)}")


class BasePointer:
    def __init__(self, ref = None):
        self._ref = ref
        self._lock = threading.RLock()

    def get(self):
        with self._lock:
            return self._ref

    def set(self, value):
        with self._lock:
            self._ref = value

    def __repr__(self):
        with self._lock:
            return f"Pointer({repr(self._ref)})"

    def __str__(self):
        return str(self.get())
    


class IntPointer(BasePointer):
    def __add__(self, other): return self.get() + other
    def __radd__(self, other): return other + self.get()
    def __sub__(self, other): return self.get() - other
    def __rsub__(self, other): return other - self.get()
    def __mul__(self, other): return self.get() * other
    def __rmul__(self, other): return other * self.get()
    def __truediv__(self, other): return self.get() / other
    def __rtruediv__(self, other): return other / self.get()
    def __mod__(self, other): return self.get() % other
    def __rmod__(self, other): return other % self.get()

    def __eq__(self, other): return self.get() == other
    def __lt__(self, other): return self.get() < other
    def __le__(self, other): return self.get() <= other
    def __gt__(self, other): return self.get() > other
    def __ge__(self, other): return self.get() >= other



class FloatPointer(BasePointer):
    def __add__(self, other): return self.get() + other
    def __radd__(self, other): return other + self.get()
    def __sub__(self, other): return self.get() - other
    def __rsub__(self, other): return other - self.get()
    def __mul__(self, other): return self.get() * other
    def __rmul__(self, other): return other * self.get()
    def __truediv__(self, other): return self.get() / other
    def __rtruediv__(self, other): return other / self.get()

    def __eq__(self, other): return self.get() == other
    def __lt__(self, other): return self.get() < other
    def __le__(self, other): return self.get() <= other
    def __gt__(self, other): return self.get() > other
    def __ge__(self, other): return self.get() >= other



class BoolPointer(BasePointer):
    def __bool__(self): return bool(self.get())
    def __eq__(self, other): return self.get() == other   
    def __lt__(self, other): return self.get() < other
    def __le__(self, other): return self.get() <= other
    def __gt__(self, other): return self.get() > other
    def __ge__(self, other): return self.get() >= other



class StringPointer(BasePointer):
    def __add__(self, other): return self.get() + str(other)
    def __eq__(self, other): return self.get() == other
    def __contains__(self, item): return item in self.get()
    def __len__(self): return len(self.get())



class ListPointer(BasePointer):
    def __getitem__(self, key):
        with self._lock:
            return self._ref[key]

    def __setitem__(self, key, value):
        with self._lock:
            self._ref[key] = value

    def append(self, value):
        with self._lock:
            self._ref.append(value)

    def pop(self, index=-1):
        with self._lock:
            return self._ref.pop(index)

    def __len__(self):
        with self._lock:
            return len(self._ref)

    def __iter__(self):
        with self._lock:
            return iter(deepcopy(self._ref))

    def __contains__(self, item):
        with self._lock:
            return item in self._ref
        


