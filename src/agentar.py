import sys
from antlr4 import *
# from src.antlr.gen.AgentarLexer import AgentarLexer

def main():
    if len(sys.argv) < 2:
        print("No command provided.")
        print("For more information, use 'agentar --help'")
        sys.exit(1)

    if sys.argv[1] == '--help':
        print("Usage: agentar run <file.agar>")
        print("\nExamples:")
        print("  agentar run examples/hello.agar")
        print("\nCommands:")
        print("  --help    Show this help message and exit")
        print("  run       Execute the specified .agar file")
        sys.exit(0)

    if sys.argv[1] not in ['--help','run']:
        print(f"Error: Unknown command '{sys.argv[1]}'")
        print("For more information, use 'agentar --help'")
        sys.exit(1)


    input_file = sys.argv[2]
    try:
        input_stream = FileStream(input_file)
        # lexer = AgentarLexer(input_stream)
        # Rest of your processing logic...
        
        if sys.argv[1] == 'run':
            print(f"Running {input_file}...")
            # Add your execution logic here
            
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
