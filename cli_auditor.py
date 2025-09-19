# cli_auditor.py
# PURPOSE: Review audit JSON files and allow user to mark items pass/fail from CLI.
# Input: output/audits/*_audit.json
# Output: output/audits/<name>_audit_reviewed.json

import json
from pathlib import Path

def review_audit(json_path: Path):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    print(f"\n[REVIEW] {json_path.name} — {data['count']} items")

    for i, item in enumerate(data["items"], start=1):
        print(f"\n{i}. {item['item']}")
        ans = input("Pass (p) / Fail (f) / Skip (Enter): ").strip().lower()
        if ans == "p":
            item["status"] = "pass"
        elif ans == "f":
            item["status"] = "fail"
        else:
            item["status"] = "pending"

    out_file = json_path.with_name(json_path.stem + "_reviewed.json")
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] Reviewed audit saved -> {out_file}")

def main():
    in_dir = Path("output/audits")
    audits = list(in_dir.glob("*_audit.json"))
    if not audits:
        print("No audit JSON files found.")
        return

    for file in audits:
        review_audit(file)

if __name__ == "__main__":
    main()
