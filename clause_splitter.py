# clause_splitter.py
# PURPOSE: Split normalized text into clauses/sections using regex.
# Input: output/normalized/*.txt
# Output: output/clauses/<name>_clauses.txt

import re
from pathlib import Path

def split_into_clauses(text: str):
    # Basic rule: split on numbered clauses (1., 2.), bullet points, or ALLCAPS headers
    pattern = r"(?m)(?=^\s*(?:\d+\.\s|[A-Z][A-Z ]{3,}:|•|- ))"
    parts = re.split(pattern, text)
    return [p.strip() for p in parts if p.strip()]

def main():
    in_dir = Path("output/normalized")
    out_dir = Path("output/clauses"); out_dir.mkdir(exist_ok=True)

    for txt_file in in_dir.glob("*.txt"):
        raw = txt_file.read_text(encoding="utf-8", errors="ignore")
        clauses = split_into_clauses(raw)
        out_file = out_dir / (txt_file.stem + "_clauses.txt")
        out_file.write_text("\n\n---\n\n".join(clauses), encoding="utf-8")
        print(f"[OK] {len(clauses)} clauses -> {out_file}")

if __name__ == "__main__":
    main()
