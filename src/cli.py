#  -*- coding: utf-8 -*- 
# src/cli.py
# Command Line Interface (CLI) for running Agentar scripts (.agar files)

import sys
from interpreter.AgentarInterpreter import AgentarInterpreter
from ast_tree.print_ast import main as print_ast
from runtime.AgentarSystem import AgentarSystem
import time
import logging

def show_help():
    print("Agentar help")
    print("========================================")
    print("Usage: agentar <command> [options]")
    print("\nCommands:")
    print("  help     Show this help message")
    print("  run        Execute a .agar file")
    print("  tree       Print the AST of a .agar file")
    print("\nExamples:")
    print("  agentar run examples/hello.agar")

def run_file(file_path):
    logging.basicConfig(level=logging.INFO)
    interpreter = AgentarInterpreter()
    mother, agents, messages = interpreter.runAgentar(file_path)
    system = AgentarSystem(mother, agents, messages)
    system.start()

def ast_tree(file_path):
    print_ast(file_path)


def main():
    if len(sys.argv) < 2:
        print("No command provided.\n")
        print("Use 'agentar help' to see available commands.")
        return 1

    command = sys.argv[1]

    if command in ('help' or '--help'):
        show_help()
        return 0
    elif command == 'run':
        if len(sys.argv) < 3:
            print("Error: No file specified for 'run'.\n")
            show_help()
            return 1
        input_file = sys.argv[2]
        try:
            run_file(input_file)
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            return 1
    elif command == 'tree':
        if len(sys.argv) < 3:
            print("Error: No file specified for 'run'.\n")
            show_help()
            return 1
        with open(sys.argv[2], "r") as f:
            source = f.read()
        try:
            ast_tree(source)
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            return 1
    else:
        print(f"Error: Unknown command '{command}'\n")
        print("Use 'agentar help' to see available commands.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
