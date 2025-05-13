import sys
from antlr4 import *

from antlr.AgentarLexer import AgentarLexer
from antlr.AgentarParser import AgentarParser
from antlr.AgentarVisitor import AgentarVisitor
from interpreter.interpreter import AgentarInterpreter

def run_agentar(file_path):
    input_stream = FileStream(file_path)
    lexer = AgentarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AgentarParser(stream)
    tree = parser.program()
    
    builder = ASTBuilder()
    ast = builder.visit(tree)

    interpreter = AgentarInterpreter()
    interpreter.interpret(ast)

def main():
    if len(sys.argv) < 2:
        print("No command provided.")
        print("For more information, use 'agentar --help'")
        sys.exit(1)
    elif sys.argv[1] == '--help':
        print("Usage: agentar run <file.agar>")
        print("\nExamples:")
        print("  agentar run examples/hello.agar")
        print("\nCommands:")
        print("  --help    Show this help message and exit")
        print("  run       Execute the specified .agar file")
        sys.exit(0)
    elif sys.argv[1] not in ['--help','run']:
        print(f"Error: Unknown command '{sys.argv[1]}'")
        print("For more information, use 'agentar --help'")
        sys.exit(1)
    elif len(sys.argv) < 3 and sys.argv[1] == 'run':
        print("Error: No file specified.")
        print("For more information, use 'agentar --help'")
        sys.exit(1)

    # run the agentar file
    input_file = sys.argv[2]
    try:        
        if sys.argv[1] == 'run':
            run_agentar(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
