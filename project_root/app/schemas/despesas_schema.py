from pydantic import BaseModel
from datetime import date, datetime
from decimal import Decimal

class DespesaBase(BaseModel):
    descricao: str
    valor: Decimal
    categoria: str
    data: date

class DespesaCreate(DespesaBase):
    pass

class DespesaResponse(DespesaBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
