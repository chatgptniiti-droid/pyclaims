from pathlib import Path
import sys

term = sys.argv[1]
docs_root = Path(__file__).resolve().parents[1] / "docs"

for path in sorted(docs_root.rglob("*")):
    if path.is_file():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if term in text:
            print(path.relative_to(docs_root))
