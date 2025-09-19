# Indus V-ai Compliance Pack  
Parser stub + RBI KYC/Fraud text dumps.  
Timestamp: 2025-09-07
## Usage

python parser_v01.py input/kyc_master_direction.pdf
python parser_v01.py input/frauds_classification_reporting.pdf

# Alternate mode
python parser_v01.py input/kyc_master_direction.pdf blocks

## Normalization

```bash
python normalize_text.py

# Cleans raw outputs in output/ -> saves normalized files in output/normalized/
```

## Clause Segmentation
```bash
python clause_splitter.py
Takes normalized text in output/normalized/ and creates clause-level splits in output/clauses/.
```

## Clause Tagging
```bash
python tag_clauses.py
Adds rough [TAGS] (e.g., KYC, FRAUD, PENALTY) to each clause in output/tagged/.
```
## Checklist Extraction
```bash
python checklist_extractor.py
Creates pass/fail checklist items from tagged clauses into output/checklists/.
```
## Audit JSON Export
```bash
python checklist_to_json.py
Converts checklist text files into structured JSON in output/audits/.
```
## CLI Auditor
```bash
python cli_auditor.py
Interactive review of audit JSON items. Marks pass/fail and saves *_reviewed.json.
```

## Audit Report Export

```bash
python export_report.py
# Creates human-readable reports in reports/ with counts and itemized results.
```

