import sys, json
from pathlib import Path
import fitz  # PyMuPDF

def extract_text(pdf_path, mode="text", sort=True):
    with fitz.open(pdf_path) as doc:
        parts = []
        for page in doc:
            if mode == "blocks":
                blocks = page.get_text("blocks")
                parts.extend(b[4] for b in blocks if len(b) >= 5)
            else:
                parts.append(page.get_text("text", sort=sort))
        return "".join(parts)

if len(sys.argv) < 2:
    print("Usage: python parser_v01.py <pdf_path> [mode]")
    sys.exit(1)

pdf_path = Path(sys.argv[1])
mode = sys.argv[2] if len(sys.argv) > 2 else "text"

out_dir = Path("output"); out_dir.mkdir(exist_ok=True)
text_out = out_dir / (pdf_path.stem + ".txt")
meta_out = out_dir / (pdf_path.stem + ".meta.json")

text = extract_text(pdf_path, mode)
text_out.write_text(text, encoding="utf-8")

with fitz.open(pdf_path) as doc:
    meta = {"file": str(pdf_path), "pages": doc.page_count,
            "chars": len(text), "mode": mode, "sort": True}
meta_out.write_text(json.dumps(meta, indent=2), encoding="utf-8")

print((text[:200] or "").replace("\n"," "))
print(f"[OK] Wrote {text_out} and {meta_out}")
