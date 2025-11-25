#  -*- coding: utf-8 -*-
# src/cli.py
# Command Line Interface (CLI) for running Agentar scripts (.agar files)

import os
import sys
import time
import logging
import argparse

from interpreter.agentar_interpreter import AgentarInterpreter
from ast_tree.print_ast import main as print_ast
from runtime.agentar_system import AgentarSystem
from resource_monitor import ResourceMonitor


def run_file(file_path: str, max_runtime: float, collect_cpu_data: bool = False) -> None:
    """
    Run a single Agentar program from a .agar file.
    """
    interpreter = AgentarInterpreter()
    mother, agents, messages = interpreter.runAgentar(file_path)
    system = AgentarSystem(mother, agents, messages)

    if collect_cpu_data:
        resource_monitor = ResourceMonitor(system=system, time_interval=0.5)
        resource_monitor.start()
    else:
        resource_monitor = None

    system.start()
    start_wall = time.time()
    start_cpu = time.process_time()

    # Main loop – waits until system finishes or timeout occurs
    while not system.terminated.is_set():
        if time.time() - start_wall > max_runtime:
            logging.warning("Timeout reached. Stopping system.")
            system.terminated.set()
            break
        time.sleep(0.1)

    system.stop()
    wall_time = time.time() - start_wall
    cpu_time = time.process_time() - start_cpu

    if resource_monitor is not None:
        resource_monitor.join()

    cpu_usage_ratio = (cpu_time / wall_time) * 100 if wall_time > 0 else 0.0
    print(f"Wall: {wall_time:.10f}s | CPU: {cpu_time:.10f}s | CPU utilization: {cpu_usage_ratio:.1f}%")


def ast_tree(file_path: str) -> None:
    """
    Print the AST of an Agentar file.
    Delegates to ast_tree.print_ast.main.
    """
    print_ast(file_path)


def logging_setup(report_flag: bool = False, to_file: bool = False) -> None:
    """
    Configure logging for the CLI.
    """
    if to_file:
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if not os.path.exists('logs/agentar.log'):
            open('logs/agentar.log', 'w').close()
        logging.basicConfig(
            filename='logs/agentar.log',
            filemode='w',  # 'a' = append, 'w' = overwrite
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%H:%M:%S',
        )
    else:
        logging.basicConfig(
            level=logging.INFO if report_flag else logging.ERROR,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%H:%M:%S',
        )



def handle_run(args: argparse.Namespace) -> int:
    """
    Handler for `agentar run`.
    """
    timeout_arg = args.timeout
    if isinstance(timeout_arg, str) and timeout_arg.lower() == "inf":
        max_runtime = float("inf")
    else:
        try:
            max_runtime = int(timeout_arg)
        except (TypeError, ValueError):
            print("Error: You must provide a valid integer for '--timeout' or 'inf' for infinite runtime.")
            return 1

    logging_setup(report_flag=args.report, to_file=args.file_log)

    try:
        run_file(args.file, max_runtime, collect_cpu_data=args.cpu_data)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found")
        return 1

    return 0


def handle_tree(args: argparse.Namespace) -> int:
    """
    Handler for `agentar tree`.
    """
    try:
        with open(args.file, "r") as f:
            source = f.read()
        ast_tree(source)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found")
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentar",
        description="Command Line Interface for running Agentar scripts (.agar files).",
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        required=True,
    )

    # ----- `run` -----
    run_parser = subparsers.add_parser(
        "run",
        help="Execute a .agar file",
        description="Execute an Agentar (.agar) script.",
    )
    run_parser.add_argument(
        "file",
        help="Path to the .agar file to execute.",
    )
    run_parser.add_argument(
        "-r", "--report",
        action="store_true",
        help="Log output to console (INFO level).",
    )
    run_parser.add_argument(
        "-f", "--file-log",
        action="store_true",
        help="Log output to logs/agentar.log.",
    )
    run_parser.add_argument(
        "-t", "--timeout",
        default="inf",
        help="Set maximum runtime for the script in seconds (default: 'inf' = no limit).",
    )
    run_parser.add_argument(
        "--cpu-data",
        action="store_true",
        help="Collect periodic CPU usage data for the Agentar system.",
    )
    run_parser.set_defaults(func=handle_run)

    # ----- `tree` -----
    tree_parser = subparsers.add_parser(
        "tree",
        help="Print the AST of a .agar file",
        description="Print the AST of an Agentar (.agar) script.",
    )
    tree_parser.add_argument(
        "file",
        help="Path to the .agar file.",
    )
    tree_parser.set_defaults(func=handle_tree)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        return args.func(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())