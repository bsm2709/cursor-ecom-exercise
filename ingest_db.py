from pathlib import Path
import sqlite3

import pandas as pd


CSV_TABLE_MAP = {
    "users.csv": "users",
    "products.csv": "products",
    "orders.csv": "orders",
    "order_items.csv": "order_items",
    "reviews.csv": "reviews",
}


def main():
    base_dir = Path(__file__).parent
    db_path = base_dir / "ecommerce.db"

    with sqlite3.connect(db_path) as conn:
        for file_name, table_name in CSV_TABLE_MAP.items():
            csv_path = base_dir / file_name
            if not csv_path.exists():
                raise FileNotFoundError(f"Missing CSV file: {csv_path}")

            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)

    print("Database ingestion completed successfully")


if __name__ == "__main__":
    main()

