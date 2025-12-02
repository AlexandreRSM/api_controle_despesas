from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.despesas_model import Despesa
from schemas.despesas_schema import DespesaCreate, DespesaResponse


router = APIRouter(prefix="/despesas", tags=["Despesas"])

@router.post("/", response_model=DespesaResponse)
def criar_despesa(despesa: DespesaCreate, db: Session = Depends(get_db)):
    nova = Despesa(**despesa.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/", response_model=list[DespesaResponse])
def listar_despesas(db: Session = Depends(get_db)):
    return db.query(Despesa).all()

@router.get("/{id}", response_model=DespesaResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    despesa = db.query(Despesa).filter(Despesa.id == id).first()
    if not despesa:
        raise HTTPException(404, "Despesa não encontrada")
    return despesa

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    despesa = db.query(Despesa).filter(Despesa.id == id).first()
    if not despesa:
        raise HTTPException(404, "Despesa não encontrada")
    db.delete(despesa)
    db.commit()
    return {"mensagem": "Despesa removida"}
