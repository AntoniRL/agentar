# Wbudowane funkcje języka Agentar
# -*- coding: utf-8 -*-

# agentar/interpreter/agentar_builtins.py

def builtin_print(value):
    print(value)

# Można dodać więcej:
# def builtin_input(prompt): return input(prompt)
# def builtin_len(x): return len(x)

builtins = {
    "print": builtin_print
}