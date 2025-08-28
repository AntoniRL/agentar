# -*- coding: utf-8 -*- 
# core/typed_structures.py
# Typed structures for the Agentar system

from copy import deepcopy
from typing import Union

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
        print()
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


class TypedDict(metaclass=TypedMeta):
    def __init__(self, key_type, value_type, items=None):
        self.key_type = key_type
        self.value_type = value_type
        self.items = {}
        if items is not None:
            if not isinstance(items, dict):
                raise TypeError("Items for TypedDict must be a dict")
            for k, v in items.items():
                self._check_key_type(k)
                self._check_value_type(v)
                self.items[k] = Pointer(v)

    def _is_key_allowed(self, key):
        return (
            isinstance(self.key_type, type) and issubclass(self.key_type, AnyTypeNode)
        ) or isinstance(key, self.key_type)

    def _is_value_allowed(self, value):
        return (
            isinstance(self.value_type, type) and issubclass(self.value_type, AnyTypeNode)
        ) or isinstance(value, self.value_type)

    def _check_key_type(self, key):
        if not self._is_key_allowed(key):
            raise TypeError(f"Expected key type {self.key_type.__name__}, got {type(key).__name__}")

    def _check_value_type(self, value):
        if not self._is_value_allowed(value):
            raise TypeError(f"Expected value type {self.value_type.__name__}, got {type(value).__name__}")

    def __getitem__(self, key):
        self._check_key_type(key) # TODO: implement ERROR
        if key not in self.items:
            raise KeyError(f"Key {repr(key)} not found in TypedDict") # TODO: implement ERROR
        return self.items[key].get()

    def pointer(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self._check_key_type(key)
        self._check_value_type(value)
        print([type(k) for k in self.items.keys()])
        print(type(key), type(self.items), key, self.items)
        if key in self.items:
            print("I am here :)))")
            self.items[key].set(value)
        else:
            print("I am here :(((")
            self.items[key] = Pointer(value)

    def __delitem__(self, key):
        del self.items[key]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for key in self.items:
            yield key

    def items_view(self):
        return ((k, ptr.get()) for k, ptr in self.items.items())

    def __deepcopy__(self, memodict={}):
        if id(self) in memodict:
            return memodict[id(self)]
        
        copied = TypedDict(self.key_type, self.value_type)
        memodict[id(self)] = copied
        
        for k, ptr in self.items.items():
            copied.items[deepcopy(k, memodict)] = Pointer(deepcopy(ptr.get(), memodict))
        return copied

    def __repr__(self):
        return str({k: ptr.get() for k, ptr in self.items.items()})

    def __str__(self):
        return repr(self)

    def report(self):
        values = []
        for k, ptr in self.items.items():
            val = ptr.get()
            if hasattr(val, "report") and callable(val.report):
                values.append(f"{repr(k)}: {val.report()}")
            else:
                values.append(f"{repr(k)}: {repr(val)}")
        return f"TypedDict(key_type={self.key_type}, value_type={self.value_type}, items={{ {', '.join(values)} }})"

    
    def keys(self):
        ks = [deepcopy(k) for k in self.items.keys()]
        return TypedList(self.key_type, ks)
    
    def values(self):
        vs = [deepcopy(ptr.get()) for ptr in self.items.values()]
        return TypedList(self.value_type, vs)


    def assign(self, value):
        if not isinstance(value, TypedDict):
            raise TypeError("Only TypedDict can be assigned")

        if (self.key_type == value.key_type or self.key_type == AnyTypeNode or value.key_type == AnyTypeNode) and \
           (self.value_type == value.value_type or self.value_type == AnyTypeNode or value.value_type == AnyTypeNode):
            pass
        else:
            raise TypeError("Incompatible key/value types")

        copied_items = {}
        for k, ptr in value.items.items():
            self._check_key_type(k)
            self._check_value_type(ptr.get())
            copied_items[deepcopy(k)] = Pointer(deepcopy(ptr.get()))
        self.items = copied_items


# ------------------------------------------------------------------------------------------------------------

class TypedTuple(metaclass=TypedMeta):
    def __init__(self, inner_type, items=None):
        self.inner_type = inner_type
        self.items = []
        if items is not None:
            for item in (items if isinstance(items, tuple) else (items,)):
                self._check_type(item)
                self.items.append(Pointer(item))
        self.items = tuple(self.items)  # immutability

    def _is_type_allowed(self, item, index=0):
        return (
            isinstance(self.inner_type, type) and issubclass(self.inner_type, AnyTypeNode)
        ) or isinstance(item, self.inner_type[index])

    def _check_type(self, item, index=0):
        if not self._is_type_allowed(item, index):
            raise TypeError(f"Expected type {self.inner_type.__name__}, got {type(item).__name__}")

    def __getitem__(self, index):
        if isinstance(index, slice):
            return TypedTuple(self.inner_type, tuple(ptr.get() for ptr in self.items[index]))
        return self.items[index].get()

    def pointer(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
    
    def _value_items(self):
        return tuple(ptr.get() for ptr in self.items)
    
    def __eq__(self, other):
        if isinstance(other, TypedTuple):
            return self._value_items() == other._value_items()
        return NotImplemented
    
    def __hash__(self):
        return hash(self._value_items())

    def __iter__(self):
        for ptr in self.items:
            yield ptr.get()

    def __deepcopy__(self, memodict={}):
        if id(self) in memodict:
            return memodict[id(self)]
        
        copied = TypedTuple(self.inner_type)
        memodict[id(self)] = copied
        copied.items = tuple(Pointer(deepcopy(ptr.get(), memodict)) for ptr in self.items)
        return copied

    def __repr__(self):
        return str(tuple(ptr.get() for ptr in self.items))

    def __str__(self):
        return repr(self)

    def report(self):
        values = []
        for ptr in self.items:
            val = ptr.get()
            if hasattr(val, "report") and callable(val.report):
                values.append(val.report())
            else:
                values.append(repr(val))
        return f"TypedTuple(inner_type={self.inner_type}, items=({', '.join(values)}))"

    def assign(self, value):
        if not isinstance(value, TypedTuple):
            raise TypeError("Only TypedTuple can be assigned") 

        if self.inner_type == value.inner_type:
            pass
        elif self.inner_type == AnyTypeNode:
            pass
        elif value.inner_type == AnyTypeNode:
            for index, item in enumerate(value):
                self._check_type(item, index)
        else:
            raise TypeError(f"Incompatible inner_type: {self.inner_type} != {value.inner_type}")

        self.items = tuple(Pointer(deepcopy(ptr.get())) for ptr in value.items)

