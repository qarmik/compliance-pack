# checklist_extractor.py
# PURPOSE: From tagged clauses, extract simple pass/fail checklist items.
# Input: output/tagged/*_tagged.txt
# Output: output/checklists/<name>_checklist.txt

from pathlib import Path

def clause_to_checklist(clause: str) -> str:
    # Remove tag header
    body = clause.split("] ", 1)[-1]
    # Heuristic: shorten long lines
    if len(body) > 150:
        body = body[:150] + "..."
    return f"- [ ] {body}"

def main():
    in_dir = Path("output/tagged")
    out_dir = Path("output/checklists"); out_dir.mkdir(exist_ok=True)

    for txt_file in in_dir.glob("*_tagged.txt"):
        raw = txt_file.read_text(encoding="utf-8", errors="ignore")
        clauses = [c.strip() for c in raw.split("\n\n---\n\n") if c.strip()]
        checklist = [clause_to_checklist(c) for c in clauses]
        out_file = out_dir / txt_file.name.replace("_tagged", "_checklist")
        out_file.write_text("\n".join(checklist), encoding="utf-8")
        print(f"[OK] {len(checklist)} checklist items -> {out_file}")

if __name__ == "__main__":
    main()
