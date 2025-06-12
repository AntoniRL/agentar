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
    print("  help         Show this help message")
    print("  run          Execute a .agar file")
    print("    -r         Log output to console")
    print("    -f / -file    Log output to agentar.log")
    print("    -t <seconds>  Set maximum runtime for the script (default is 5 seconds)")
    print("  tree         Print the AST of a .agar file")
    print("\nExamples:")
    print("  agentar run examples/hello.agar -r -t 10")

def run_file(file_path, max_runtime):
    interpreter = AgentarInterpreter()
    mother, agents, messages = interpreter.runAgentar(file_path)
    system = AgentarSystem(mother, agents, messages)
    system.start()
    start_time = time.time()
    while not system.terminated.is_set():
        if time.time() - start_time > max_runtime:
            logging.warning("Timeout reached. Stopping system.")
            system.terminated.set()  # Signal termination
            break
        time.sleep(0.1)
    system.stop()


def ast_tree(file_path):
    print_ast(file_path)

def logging_setup(raport_flag=False, to_file=False):
    if raport_flag:
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s',
                        datefmt='%H:%M:%S')
    elif to_file:
        
        logging.basicConfig(filename='agentar.log',  # write to a file
                            filemode='w',            # 'a' = append, 'w' = overwrite
                            level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s',
                            datefmt='%H:%M:%S')
    else:
        logging.basicConfig(level=logging.ERROR, format='[%(asctime)s] %(levelname)s: %(message)s',
                            datefmt='%H:%M:%S')


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
            print("Use 'agentar help' to see available commands.")
            return 1
        input_file = sys.argv[2]

        if "-r" in sys.argv:
            raport_flag = True
        else:
            raport_flag = False

        if "-file" in sys.argv or "-f" in sys.argv:
            to_file = True
        else:
            to_file = False
        
        if "-t" in sys.argv:
            t_index = sys.argv.index("-t")
            try:
                max_runtime = int(sys.argv[t_index + 1])
            except (IndexError, ValueError):
                print("Error: You must provide a valid integer after '-t'")
                sys.exit(1)
        else:
            max_runtime = 5

        try:
            logging_setup(raport_flag, to_file)
            run_file(input_file, max_runtime)       # run the Agentar script
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found")
            return 1
        

    elif command == 'tree':
        if len(sys.argv) < 3:
            print("Error: No file specified for 'run'.\n")
            show_help()
            return 1    
        elif len(sys.argv) > 3:
            print("Error: Too many arguments for 'tree' command.\n")
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
