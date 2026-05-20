from faker import Faker
from confluent_kafka import Producer
from datetime import datetime
from config import config

import random
import json
import uuid
import time

fake = Faker()

producer = Producer({
    "bootstrap.servers": config.KAFKA_BOOTSTRAP_SERVERS
})

PAYMENT_STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]

ORDER_STATUS = [
    "CREATED",
    "PROCESSING",
    "SHIPPED",
    "DELIVERED",
    "RETURNED"
]

REGIONS = [
    "US",
    "EU",
    "APAC",
    "LATAM",
    "MIDDLE_EAST"
]

PRODUCT_CATALOG = [
    "LAPTOP",
    "HEADPHONES",
    "MOBILE",
    "MONITOR",
    "TABLET",
    "KEYBOARD",
    "MOUSE",
    "CAMERA"
]

def generate_transaction():

    quantity = random.randint(1, 10)

    amount = round(
        random.uniform(25, 5000),
        2
    )

    return {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": str(uuid.uuid4()),
        "product_id": random.choice(PRODUCT_CATALOG),
        "quantity": quantity,
        "amount": amount,
        "payment_status": random.choice(PAYMENT_STATUS),
        "order_status": random.choice(ORDER_STATUS),
        "region": random.choice(REGIONS),
        "created_at": datetime.utcnow().isoformat()
    }

def delivery_report(err, msg):

    if err:
        print(f"Delivery failed: {err}")

def stream_transactions(batch_size=10000):

    for _ in range(batch_size):

        record = generate_transaction()

        producer.produce(
            "transactions_topic",
            json.dumps(record).encode("utf-8"),
            callback=delivery_report
        )

    producer.flush()

if __name__ == "__main__":

    while True:
        stream_transactions()
        time.sleep(1)
