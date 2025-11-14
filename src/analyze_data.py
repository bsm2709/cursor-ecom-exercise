import sqlite3
from pathlib import Path


QUERY = """
SELECT
    u.first_name || ' ' || u.last_name AS user_name,
    ROUND(SUM(oi.total_price), 2) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY u.user_id
ORDER BY total_spent DESC
LIMIT 5;
"""


def main():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    db_path = data_dir / "ecommerce.db"
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found at {db_path}")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(QUERY)
        rows = cursor.fetchall()

    print("Top 5 Users by Total Spending:")
    for name, total in rows:
        print(f"{name}: ${total:.2f}")


if __name__ == "__main__":
    main()

