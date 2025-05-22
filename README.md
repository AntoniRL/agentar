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
    - Generowanie parsera i lexera
    ```bash
    ./scripts/generate_parser.sh
    ```
    - uruchomienie interpretera
    ```bash
    agentar run examples/hello.agar
    ```
