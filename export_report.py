# export_report.py
# PURPOSE: Generate a simple human-readable audit report from reviewed JSONs.
# Input: output/audits/*_audit_reviewed.json
# Output: reports/<name>_report.txt

import json
from pathlib import Path
from datetime import datetime

def make_report(data, out_file: Path):
    lines = []
    lines.append("Indus V-ai Compliance Pack")
    lines.append(f"Report Source: {data['source']}")
    lines.append(f"Generated: {datetime.now().isoformat()}")
    lines.append("")
    lines.append(f"Total items: {data['count']}")
    passed = sum(1 for it in data['items'] if it['status']=="pass")
    failed = sum(1 for it in data['items'] if it['status']=="fail")
    pending = sum(1 for it in data['items'] if it['status']=="pending")
    lines.append(f"Pass: {passed} | Fail: {failed} | Pending: {pending}")
    lines.append("\n---\n")

    for i, item in enumerate(data["items"], 1):
        lines.append(f"{i}. [{item['status'].upper()}] {item['item']}")

    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] Report written -> {out_file}")

def main():
    in_dir = Path("output/audits")
    out_dir = Path("reports"); out_dir.mkdir(exist_ok=True)

    for jf in in_dir.glob("*_audit_reviewed.json"):
        data = json.loads(jf.read_text(encoding="utf-8"))
        out_file = out_dir / jf.name.replace("_audit_reviewed.json", "_report.txt")
        make_report(data, out_file)

if __name__ == "__main__":
    main()
