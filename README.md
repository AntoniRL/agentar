# Agentar

Język programowania agentowego do modelowania inteligentnych zachowań.  
**Status:** Wczesna faza rozwoju.

## Instalacja
1. Wymagania:
   - Python 3.8+
   - ANTLR4
   ```bash
    pip install antlr4-tools
    pip install antlr4-python3-runtime

2. Aktywacja venv-agentar:
    ```bash
    source venv-agentar/bin/activate

    deactivate
    ```

3. Po zamianie struktury plików aktualizacja pakietu agentar.
    (wewnątrz folderu agentar i w venv-agentar)
    ```bash
    pip install -e .
    ```

3. Użycie:

Python
- Generowanie parsera i lexera
```bash
./scripts/generate_parser.sh
```

- uruchomienie interpretera
```bash
agentar run examples/hello.agar
```

Java (testowanie, łatwiejsza analiza drzewa parsowego)

- generuj parser
```bash
antlr4 -Dlanguage=Java -o java_tree grammar/Agentar.g4
find java_tree/grammar -name "*.java" | xargs javac -cp ".:../antlr-4.13.1-complete.jar"
java -cp ".:../antlr-4.13.1-complete.jar:java_tree/grammar" org.antlr.v4.gui.TestRig Agentar program -gui examples/test.agar
```

4. Budowanie drzewa AST testowo:

```bash
python ./src/ast_tree/print_ast.py examples/test.agar 
```
