from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

DATABASE_URL = (
    f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@"
    f"{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=40,
    pool_recycle=3600,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
