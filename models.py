from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    BigInteger,
    Index
)

Base = declarative_base()

class TransactionRecord(Base):

    __tablename__ = "transactions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    transaction_id = Column(String(120), unique=True, nullable=False)
    customer_id = Column(String(120), nullable=False)
    product_id = Column(String(120), nullable=False)

    quantity = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)

    payment_status = Column(String(40), nullable=False)
    order_status = Column(String(40), nullable=False)

    region = Column(String(100), nullable=False)

    created_at = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("idx_transaction_id", "transaction_id"),
        Index("idx_customer_id", "customer_id"),
        Index("idx_region", "region"),
        Index("idx_created_at", "created_at"),
    )


class FailedRecord(Base):

    __tablename__ = "failed_records"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    transaction_id = Column(String(120))
    failure_reason = Column(String(255))

    payload = Column(String(5000))

    created_at = Column(DateTime, nullable=False)
