# -*- coding: utf-8 -*- 
# core/typed_structures.py
# Typed structures for the Agentar system

from copy import deepcopy

from core.pointer import Pointer
from ast_tree.nodes import AnyTypeNode
from runtime.errors import WrongTypeError


class TypedMeta(type):
    """Meta class for typed structures to enforce type checking on initialization and item assignment."""
    def __repr__(cls):
        return f"<Typed class {cls.__name__}>"

    def __str__(cls):
        return f"<class '{cls.__name__}'>"


# ------------------------------------------------------------------------------------------------------------

class TypedList(metaclass=TypedMeta):
    def __init__(self, inner_type, items=None):
        self.inner_type = inner_type
        self.items = []
        if items is not None:
            for item in (items if isinstance(items, list) else [items]):
                self._check_type(item)
                self.items.append(Pointer(item))

    def _is_type_allowed(self, item):
        return (
            isinstance(self.inner_type, type) and issubclass(self.inner_type, AnyTypeNode)
        ) or isinstance(item, self.inner_type)

    def _check_type(self, item):
        if not self._is_type_allowed(item):
            raise TypeError(f"Expected type {self.inner_type.__name__}, got {type(item).__name__}")

    def __getitem__(self, index):
        if isinstance(index, slice):
            # if slicing, return a new TypedList with the sliced items
            new_items = [ptr.get() for ptr in self.items[index]]
            return TypedList(self.inner_type, new_items)
        return self.items[index].get()

    def pointer(self, index):
        return self.items[index]  # return Pointer object directly

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            if not isinstance(value, TypedList):
                raise TypeError("Slice assignment requires a TypedList") # TODO: implement error handling
            self.assign(value, index)
        else:
            self._check_type(value)
            self.items[index].set(value)

    def __delitem__(self, index):
        del self.items[index]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for ptr in self.items:
            yield ptr.get()

    def __deepcopy__(self, memodict={}):
        if memodict is None:
            memodict = {}
        if id(self) in memodict:
            return memodict[id(self)]
        
        copied = TypedList(self.inner_type)
        
        memodict[id(self)] = copied
        
        for ptr in self.items:
            copied_value = deepcopy(ptr.get(), memodict)
            copied.items.append(Pointer(copied_value))
        
        return copied

    def __repr__(self):
        return str([ptr.get() for ptr in self.items])
    
    def __str__(self):
        return str([ptr.get() for ptr in self.items])
    
    def report(self):
        """Generate a report of the TypedList."""
        values = []
        for ptr in self.items:
            val = ptr.get()
            if hasattr(val, "report") and callable(val.report):
                values.append(val.report())
            else:
                values.append(repr(val))  # lub str(val), jeśli chcesz ładniej
        return f"TypedList(inner_type={self.inner_type}, items=[{', '.join(values)}])"
    

    def append(self, item):
        self._check_type(item)
        self.items.append(Pointer(item))

    def extend(self, iterable):
        for item in iterable:
            self._check_type(item)
            self.items.append(Pointer(item))

    def insert(self, index, item):
        self._check_type(item)
        self.items.insert(index, Pointer(item))

    def remove(self, item):
        for i, ptr in enumerate(self.items):
            if ptr.get() == item:
                del self.items[i]
                return
        raise ValueError(f"{item} not found")

    def pop(self, index=-1):
        return self.items.pop(index).get()

    def clear(self):
        self.items.clear()

    def index(self, item):
        for idx, ptr in enumerate(self.items):
            if ptr.get() == item:
                return idx
        raise ValueError(f"{item} not found")

    def count(self, item):
        return sum(1 for ptr in self.items if ptr.get() == item)

    def copy(self):
        new_list = TypedList(self.inner_type)
        new_list.items = self.items.copy()
        return new_list
    
    def assign(self, value, index = None):
        if not isinstance(value, TypedList):
            raise TypeError("Only TypedList can be assigned") 

        if self.inner_type == value.inner_type:
            pass
        elif self.inner_type == AnyTypeNode:
            pass
        elif value.inner_type == AnyTypeNode:
            for item in value:
                self._check_type(item)
        else:
            raise TypeError(f"Incompatible inner_type: {self.inner_type} != {value.inner_type}")

        copied_items = []
        for ptr in value.items:
            copied_value = deepcopy(ptr.get())
            copied_items.append(Pointer(copied_value))

        if index is None:
            self.items = copied_items
        else:
            indices = list(range(*index.indices(len(self.items))))
            if len(indices) != len(copied_items):
                raise ValueError(f"Slice length mismatch: {len(indices)} positions to assign, but {len(copied_items)} values provided.")
            for i, ptr in zip(indices, copied_items):
                self.items[i] = ptr
    

# ----------------------------------------------------------------------------------------------------------


class TypedDict:
    def __init__(self, inner_type, items=None):
        self.inner_type = inner_type
        self.items = {}
        if items is not None:
            for key, value in items.items():
                self._check_type(value)
                self.items[key] = Pointer(value)

    def _check_type(self, value):
        if not isinstance(value, self.inner_type):
            raise TypeError(f"Expected type {self.inner_type.__name__}, got {type(value).__name__}")

    def __getitem__(self, key):
        return self.items[key].get()

    def pointer(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self._check_type(value)
        if key in self.items:
            self.items[key].set(value)
        else:
            self.items[key] = Pointer(value)

    def __delitem__(self, key):
        del self.items[key]

    def __contains__(self, key):
        return key in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def items_values(self):
        return {k: ptr.get() for k, ptr in self.items.items()}

    def __repr__(self):
        values = self.items_values()
        return f"TypedDict(inner_type={self.inner_type.__name__}, items={values})"

    def get(self, key, default=None):
        return self.items[key].get() if key in self.items else default

    def pop(self, key, default=None):
        if key in self.items:
            return self.items.pop(key).get()
        if default is not None:
            return default
        raise KeyError(key)

    def clear(self):
        self.items.clear()

    def keys(self):
        return self.items.keys()

    def values(self):
        return [ptr.get() for ptr in self.items.values()]

    def items_list(self):
        return [(k, ptr.get()) for k, ptr in self.items.items()]


# -----------------------------------------------------------------------------------------------------------


class TypedTuple:
    def __init__(self, inner_type, items):
        if not isinstance(items, tuple):
            raise TypeError("TypedTuple requires a tuple as input.")
        self.inner_type = inner_type
        self.items = []
        for item in items:
            self._check_type(item)
            self.items.append(Pointer(item))

    def _check_type(self, item):
        if not isinstance(item, self.inner_type):
            raise TypeError(f"Expected type {self.inner_type.__name__}, got {type(item).__name__}")

    def __getitem__(self, index):
        return self.items[index].get()

    def pointer(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for ptr in self.items:
            yield ptr.get()

    def __repr__(self):
        values = tuple(ptr.get() for ptr in self.items)
        return f"TypedTuple(inner_type={self.inner_type.__name__}, items={values})"

    def count(self, item):
        return sum(1 for ptr in self.items if ptr.get() == item)

    def index(self, item):
        for i, ptr in enumerate(self.items):
            if ptr.get() == item:
                return i
        raise ValueError(f"{item} not found")
