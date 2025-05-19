# mostlyai-competition

## Overview
This repo generates and evaluates synthetic data for the FLAT and SEQUENTIAL challenges in the $100k MOSTLY AI Prize.

## Steps
1. Install dependencies:
```bash
pip install pandas numpy synthcity
cd mostlyai-qa
pip install -r requirements.txt
cd ..
```

2. Place training files into the `data/` folder.

3. Run:
```bash
python generate_flat.py
python generate_sequential.py
python evaluate_synthetic.py
```

4. Submit your generated `.csv` or `.csv.gz` file to the competition site.

---
This repo is MIT licensed. Fork, contribute, and compete! 🏆
