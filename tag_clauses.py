# tag_clauses.py
# PURPOSE: Read clause-level text files and prepend simple [TAGS] to each clause.
# Input: output/clauses/*.txt
# Output: output/tagged/<name>_tagged.txt

from pathlib import Path

# crude keyword map for demo
KEYWORDS = {
    "kyc": ["customer", "identity", "verification", "kyc", "due diligence"],
    "fraud": ["fraud", "reporting", "classification", "npas", "timeline"],
    "penalty": ["penalty", "fine", "non-compliance"],
    "governance": ["board", "oversight", "responsibility", "audit committee"],
}

def tag_clause(clause: str) -> str:
    text = clause.lower()
    tags = []
    for tag, kws in KEYWORDS.items():
        if any(kw in text for kw in kws):
            tags.append(tag.upper())
    if not tags:
        tags.append("MISC")
    return f"[{'|'.join(tags)}] {clause}"

def main():
    in_dir = Path("output/clauses")
    out_dir = Path("output/tagged"); out_dir.mkdir(exist_ok=True)

    for txt_file in in_dir.glob("*_clauses.txt"):
        raw = txt_file.read_text(encoding="utf-8", errors="ignore")
        clauses = [c.strip() for c in raw.split("\n\n---\n\n") if c.strip()]
        tagged = [tag_clause(c) for c in clauses]
        out_file = out_dir / txt_file.name.replace("_clauses", "_tagged")
        out_file.write_text("\n\n---\n\n".join(tagged), encoding="utf-8")
        print(f"[OK] Tagged {len(tagged)} clauses -> {out_file}")

if __name__ == "__main__":
    main()
