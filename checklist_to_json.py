# checklist_to_json.py
# PURPOSE: Convert checklist .txt into structured JSON for audits.
# Input: output/checklists/*_checklist.txt
# Output: output/audits/<name>_audit.json

import json
from pathlib import Path

def parse_checklist_line(line: str):
    # "- [ ] text" → {"item": "text", "status": "pending"}
    text = line.replace("- [ ]", "").strip()
    return {"item": text, "status": "pending"}

def main():
    in_dir = Path("output/checklists")
    out_dir = Path("output/audits"); out_dir.mkdir(exist_ok=True)

    for txt_file in in_dir.glob("*_checklist.txt"):
        lines = [l.strip() for l in txt_file.read_text(encoding="utf-8").splitlines() if l.strip()]
        items = [parse_checklist_line(l) for l in lines if l.startswith("- [ ]")]
        data = {
            "source": txt_file.name,
            "count": len(items),
            "items": items,
        }
        out_file = out_dir / txt_file.name.replace("_checklist.txt", "_audit.json")
        out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[OK] {len(items)} items -> {out_file}")

if __name__ == "__main__":
    main()
