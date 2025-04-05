
import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime
import json
import os

fake = Faker()

def generate_orders(n=100):
    orders = []
    for _ in range(n):
        orders.append({
            "order_id": str(uuid.uuid4()),
            "order_date": fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "customer_id": random.randint(1000, 9999),
            "amount": round(random.uniform(20.0, 500.0), 2),
            "currency": "USD"
        })
    df = pd.DataFrame(orders)
    df.to_csv("orders.csv", index=False)

def generate_customers(n=100):
    customers = []
    for _ in range(n):
        customers.append({
            "customer_id": random.randint(1000, 9999),
            "name": fake.name(),
            "email": fake.email(),
            "signup_date": fake.date_this_decade().isoformat()
        })
    with open("customers.json", "w") as f:
        json.dump(customers, f, indent=2)

def generate_products(n=50):
    products = []
    for _ in range(n):
        products.append({
            "product_id": str(uuid.uuid4()),
            "product_name": fake.word().capitalize(),
            "price": round(random.uniform(10.0, 200.0), 2),
            "category": fake.random_element(elements=("Electronics", "Books", "Clothing", "Home"))
        })
    df = pd.DataFrame(products)
    df.to_parquet("products.parquet", index=False)

def generate_iot_data(n=100):
    with open("iot_data.jsonl", "w") as f:
        for _ in range(n):
            record = {
                "device_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "temperature": round(random.uniform(15.0, 30.0), 2),
                "humidity": round(random.uniform(30.0, 70.0), 2)
            }
            f.write(json.dumps(record) + "\n")

def generate_logs(n=100):
    with open("logs.txt", "w") as f:
        for _ in range(n):
            f.write(fake.sentence() + "\n")

def main():
    os.makedirs("data", exist_ok=True)
    os.chdir("data")
    generate_orders()
    generate_customers()
    generate_products()
    generate_iot_data()
    generate_logs()

if __name__ == "__main__":
    main()
