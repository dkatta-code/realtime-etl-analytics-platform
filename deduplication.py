import redis

from config import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True
)

CACHE_EXPIRATION = 86400

def is_duplicate(transaction_id):

    existing_transaction = redis_client.get(transaction_id)

    if existing_transaction:
        return True

    redis_client.set(
        transaction_id,
        "processed",
        ex=CACHE_EXPIRATION
    )

    return False
