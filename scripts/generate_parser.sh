PROJECT_ROOT=$(dirname "$(dirname "$(realpath "$0")")")
GRAMMAR_FILE="$PROJECT_ROOT/grammar/Agentar.g4"
OUTPUT_DIR="$PROJECT_ROOT/src/antlr"

# Install antlr4-tools if missing
if ! command -v antlr4 &> /dev/null; then
    echo "Installing antlr4-tools..."
    pip install antlr4-tools
fi

# Create output directory if missing
mkdir -p "$OUTPUT_DIR"

# Generate Parser using antlr4-tools (no Java required)
echo "Regenerating parser from grammar..."
antlr4 -Dlanguage=Python3 \
       -visitor \
       -o "$OUTPUT_DIR" \
       -Xexact-output-dir \
       "$GRAMMAR_FILE"

# Ensure Python package marker
touch "$OUTPUT_DIR/__init__.py"

echo "Successfully generated parser in $OUTPUT_DIR"