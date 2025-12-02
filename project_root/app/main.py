#usuario pode registrar despesas com descrição, valor, categoria e data
#usuario pode listar todas as despesas
#usuario pode listar despesas por categoria
#usuario pode listar despesas por data 
#a API permite listar, filtrar por mês/categoria e obter resumo mensal

from fastapi import FastAPI

from routers.despesas_router import router as despesas_router
from database.connection import Base, engine

# Criar tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Controle de Gastos")

# Registrar rotas
app.include_router(despesas_router)
