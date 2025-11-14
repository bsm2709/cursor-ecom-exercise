import random
from pathlib import Path

import pandas as pd
from faker import Faker


RECORD_COUNT = 50
fake = Faker()
random.seed(2024)
Faker.seed(2024)


def format_address() -> str:
    return fake.address().replace("\n", ", ")


def generate_users(count: int):
    users = []
    for user_id in range(1, count + 1):
        profile = fake.simple_profile()
        users.append(
            {
                "user_id": user_id,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": profile["mail"],
                "address": fake.street_address(),
                "city": fake.city(),
                "state": fake.state(),
                "postal_code": fake.postcode(),
                "signup_date": fake.date_between(start_date="-2y", end_date="today").isoformat(),
            }
        )
    return users


def generate_products(count: int):
    categories = ["Electronics", "Books", "Home", "Beauty", "Sports", "Toys"]
    products = []
    for product_id in range(1, count + 1):
        price = round(random.uniform(5.0, 500.0), 2)
        products.append(
            {
                "product_id": product_id,
                "name": fake.catch_phrase(),
                "category": random.choice(categories),
                "price": price,
                "stock": random.randint(0, 500),
                "created_at": fake.date_between(start_date="-2y", end_date="today").isoformat(),
            }
        )
    return products


def generate_orders(count: int, user_ids):
    statuses = ["processing", "shipped", "delivered", "cancelled"]
    orders = []
    for order_id in range(1, count + 1):
        order = {
            "order_id": order_id,
            "user_id": random.choice(user_ids),
            "order_date": fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
            "status": random.choice(statuses),
            "shipping_address": format_address(),
            "total_amount": 0.0,
        }
        orders.append(order)
    return orders


def generate_order_items(orders, products):
    product_lookup = {product["product_id"]: product["price"] for product in products}
    order_items = []
    for idx, order in enumerate(orders, start=1):
        product = random.choice(products)
        quantity = random.randint(1, 5)
        unit_price = product_lookup[product["product_id"]]
        total_price = round(unit_price * quantity, 2)
        order["total_amount"] = total_price
        order_items.append(
            {
                "order_item_id": idx,
                "order_id": order["order_id"],
                "product_id": product["product_id"],
                "quantity": quantity,
                "unit_price": unit_price,
                "total_price": total_price,
            }
        )
    return order_items


def generate_reviews(count: int, user_ids, product_ids):
    reviews = []
    for review_id in range(1, count + 1):
        reviews.append(
            {
                "review_id": review_id,
                "user_id": random.choice(user_ids),
                "product_id": random.choice(product_ids),
                "rating": random.randint(1, 5),
                "title": fake.sentence(nb_words=6),
                "content": fake.paragraph(nb_sentences=3),
                "created_at": fake.date_time_between(start_date="-1y", end_date="now").isoformat(),
            }
        )
    return reviews


def main():
    output_dir = Path(__file__).parent

    users = generate_users(RECORD_COUNT)
    products = generate_products(RECORD_COUNT)
    orders = generate_orders(RECORD_COUNT, [user["user_id"] for user in users])
    order_items = generate_order_items(orders, products)
    reviews = generate_reviews(RECORD_COUNT, [user["user_id"] for user in users], [product["product_id"] for product in products])

    datasets = {
        "users.csv": users,
        "products.csv": products,
        "orders.csv": orders,
        "order_items.csv": order_items,
        "reviews.csv": reviews,
    }

    for file_name, rows in datasets.items():
        df = pd.DataFrame(rows)
        df.to_csv(output_dir / file_name, index=False)

    print("Data generated successfully")


if __name__ == "__main__":
    main()

