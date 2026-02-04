from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Format:
# mysql+pymysql://username:password@host:port/database_name
DATABASE_URL = "mysql+pymysql://root:Sbelhekar%4014@localhost:3306/todo_db"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
