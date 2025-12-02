from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com PostgreSQL
DATABASE_URL = "postgresql://postgres:1235@localhost:5432/controle_gastos"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência usada nos endpoints (abre e fecha conexão)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()