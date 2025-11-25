# Agentar

Agentar is an agent-oriented programming language (AOP) for modeling intelligent behavior.  
**Status:** Early development stage 

---

## Installation

### 1️. Requirements
- Python **3.8+**
- (Optional) Java **11+** – required only if you want to generate parsers directly using ANTLR

---

### 2️. Recommended: Virtual Environment (e.g. `venv-agentar`)

Create a virtual environment (Linux):
```bash
python3 -m venv venv-agentar
```

Activate and deactivate (Linux):
```basj
source venv-agentar/bin/activate

deactivate
```

### 3. Initialize the Agentar package.
Clone the repository

```bash
git clone https://github.com/AntoniRL/agentar.git
```
Run these commands inside the agentar folder (where setup.py is located) and with the virtual environment activated.

Before installation, make sure pip and setuptools are up to date:
```bash
pip install --upgrade pip setuptools wheel
```
Then install Agentar in editable (development) mode:
```bash
pip install -e .
```
*Re-run this command every time you change the project’s structure.

### 4. Usage.

- Generate the parser and lexer (only after modifying the .g4 grammar file)
```bash
./scripts/generate_parser.sh
```

- Run the interpreter
```bash
agentar run examples/helloAgentar.agar
agentar --help 
```

- Run the visualization (GUI)
All programs located in GUI folder, for example:
```bash
python GUI/exampleGui.py
```

- Generate the parser in Java (useful for testing and visualizing the parse tree)

    Requires:
    - Java (version 11 or higher)
    - plik antlr-4.13.1-complete.jar (```curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar```)

    Then run:
    ```bash
    antlr4 -Dlanguage=Java -o java_tree grammar/Agentar.g4
    find java_tree/grammar -name "*.java" | xargs javac -cp ".:antlr-4.13.1-complete.jar"
    java -cp ".:../antlr-4.13.1-complete.jar:java_tree/grammar" org.antlr.v4.gui.TestRig Agentar program -gui examples/test.agar
    ```