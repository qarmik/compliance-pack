# parser_stub.py
# PURPOSE: Read a PDF and write all text into a .txt file. Print first 200 chars.

import sys               # sys lets us read command-line arguments
from pathlib import Path  # Path helps with file paths (cross-platform)
import fitz               # 'fitz' is the PyMuPDF package

# If a path is given as first argument, use it; otherwise use the KYC default
pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("input/kyc_master_direction.pdf")
out_txt = pdf_path.with_suffix(".txt")  # change .pdf to .txt

with fitz.open(pdf_path) as doc:   # open the PDF
    parts = []
    for page in doc:
        # plain text first; 'sort=True' tries to keep reading order
        parts.append(page.get_text("text", sort=True))
    text = "".join(parts)

# Show first 200 characters (smoke test). Replace newlines with spaces for readability.
print((text[:200] or "").replace("\n", " "))

# Write the full text to a .txt file (UTF-8 encoding)
out_txt.write_text(text, encoding="utf-8")
print(f"[OK] Wrote {len(text)} chars -> {out_txt}")
