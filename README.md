# E-Commerce Data Exercise

This repo implements the Cursor IDE assessment:

1. Generate multiple synthetic e-commerce CSV files.
2. Ingest them into SQLite.
3. Run an analytical SQL query joining several tables.

## Project Layout

- `src/generate_data.py` – creates `users`, `products`, `orders`, `order_items`, `reviews` CSVs (50 rows each) inside `data/`.
- `src/ingest_db.py` – loads those CSVs into `data/ecommerce.db` using `pandas.to_sql` with `replace`.
- `src/analyze_data.py` – connects to the SQLite DB and prints the top 5 spenders via joins.
- `data/` – generated CSVs + `ecommerce.db` (ignored if you prefer clean repo).
- `requirements.txt` – Python dependencies (`pandas`, `Faker`, etc.).
- `.gitignore` – standard Python ignores.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows PowerShell
pip install -r requirements.txt
```

## Usage

```bash
# Generate synthetic data into data/
python src/generate_data.py

# Load CSVs into data/ecommerce.db
python src/ingest_db.py

# Run analysis showing top spenders
python src/analyze_data.py
```

Example output:

```
Top 5 Users by Total Spending:
Tracy Harris: $3868.28
...
```

## Tips

- Scripts set deterministic seeds for repeatable datasets.
- Regenerate data (`generate_data.py`) before re-ingesting (`ingest_db.py`) to keep DB in sync.
- Feel free to delete or git-ignore files under `data/` if you want a source-only repo.

Good luck demonstrating this in the interview!

