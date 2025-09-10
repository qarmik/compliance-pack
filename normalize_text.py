# normalize_text.py
# PURPOSE: Clean raw .txt files (collapse newlines, strip spaces) into output/normalized/

from pathlib import Path

def normalize(text: str) -> str:
    # collapse multiple newlines into one
    import re
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    # strip leading/trailing spaces on each line
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(lines)

def main():
    in_dir = Path("output")
    out_dir = Path("output/normalized"); out_dir.mkdir(exist_ok=True)
    
    for txt_file in in_dir.glob("*.txt"):
        raw = txt_file.read_text(encoding="utf-8", errors="ignore")
        cleaned = normalize(raw)
        out_file = out_dir / txt_file.name
        out_file.write_text(cleaned, encoding="utf-8")
        print(f"[OK] Normalized {txt_file} -> {out_file}")

if __name__ == "__main__":
    main()
