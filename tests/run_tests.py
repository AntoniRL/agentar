import subprocess
import re
from pathlib import Path

def extract_expected_output(source: str):
    # Find /* EXPECT: ... */
    match = re.search(r'/\*\s*EXPECT:\s*(.*?)\s*\*/', source, re.DOTALL)
    return match.group(1).strip() if match else None

def run_single_test(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    expected_output = extract_expected_output(code)
    if expected_output is None:
        print(f"[SKIP] {filepath.name} (no EXPECT)")
        return True

    try:
        result = subprocess.run(
            ["agentar", "run", str(filepath), "-r"], 
            capture_output=True,
            text=True,
            timeout=5
        )
    except FileNotFoundError:
        print("❌ No 'agentar' executable found. Please ensure it is installed and in your PATH.")
        return False

    print(result)

    output = result.stdout.strip()
    if output == expected_output:
        print(f"[PASS] {filepath.name}")
        return True
    else:
        print(f"[FAIL] {filepath.name}")
        print(f"  Expected  : {expected_output}")
        print(f"  Got       : {output}")
        return False

def main():
    test_dir = Path("tests/agentar_files")
    agar_files = list(test_dir.glob("*.agar"))

    passed = 0
    for file in agar_files:
        if run_single_test(file):
            passed += 1

    total = len(agar_files)
    print(f"\n{passed}/{total} tests passed.")

if __name__ == "__main__":
    main()