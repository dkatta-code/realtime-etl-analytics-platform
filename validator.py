from datetime import datetime

REQUIRED_FIELDS = [
    "transaction_id",
    "customer_id",
    "product_id",
    "quantity",
    "amount",
    "payment_status",
    "order_status",
    "region",
    "created_at"
]

VALID_PAYMENT_STATUS = [
    "SUCCESS",
    "FAILED",
    "PENDING"
]

VALID_ORDER_STATUS = [
    "CREATED",
    "PROCESSING",
    "SHIPPED",
    "DELIVERED",
    "RETURNED"
]

def validate_schema(record):

    for field in REQUIRED_FIELDS:

        if field not in record:
            return False

        if record[field] is None:
            return False

    if not isinstance(record["quantity"], int):
        return False

    if record["quantity"] <= 0:
        return False

    if not isinstance(record["amount"], (float, int)):
        return False

    if record["amount"] <= 0:
        return False

    if record["payment_status"] not in VALID_PAYMENT_STATUS:
        return False

    if record["order_status"] not in VALID_ORDER_STATUS:
        return False

    try:
        datetime.fromisoformat(record["created_at"])
    except Exception:
        return False

    return True
