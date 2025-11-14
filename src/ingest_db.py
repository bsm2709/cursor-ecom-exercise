from pathlib import Path
import sqlite3

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

CSV_TABLE_MAP = {
    "users.csv": "users",
    "products.csv": "products",
    "orders.csv": "orders",
    "order_items.csv": "order_items",
    "reviews.csv": "reviews",
}


def main():
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")

    db_path = DATA_DIR / "ecommerce.db"

    with sqlite3.connect(db_path) as conn:
        for file_name, table_name in CSV_TABLE_MAP.items():
            csv_path = DATA_DIR / file_name
            if not csv_path.exists():
                raise FileNotFoundError(f"Missing CSV file: {csv_path}")

            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)

    print("Database ingestion completed successfully")


if __name__ == "__main__":
    main()

