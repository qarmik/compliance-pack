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

