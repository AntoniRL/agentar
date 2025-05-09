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

2. Użycie:
    - Generowanie parsera i lexera
    ```bash
    cd src/antlr/
    antlr4 -Dlanguage=Python3 Agentar.g4 -o gen/
    ```
    - uruchomienie interpretera
    ```bash
    python3 -m src.agentar examples/hello.agar
    ```