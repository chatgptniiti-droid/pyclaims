from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parents[1] / "pyclaims"

def list_functions(path: Path):
    tree = ast.parse(path.read_text())
    results = []
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
                    results.append(f"{node.name}.{item.name}")
                if isinstance(item, ast.AsyncFunctionDef) and not item.name.startswith("_"):
                    results.append(f"{node.name}.{item.name}")
    return results

if __name__ == "__main__":
    for file in sorted(ROOT.glob("*.py")):
        if file.name.startswith("_"):
            continue
        for symbol in list_functions(file):
            print(symbol)
