from sqlalchemy import Column, Integer, String, Numeric, Date, TIMESTAMP, func
from database.connection import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    valor = Column(Numeric(10,2), nullable=False)
    categoria = Column(String, nullable=False)
    data = Column(Date, nullable=False)

    criado_em = Column(TIMESTAMP(timezone=True), server_default=func.now())
