from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import List
import models
import schemas
from database import SessionLocal, engine

# cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint para criar estudante
@app.post("/estudantes/", response_model=schemas.Estudante)
def criar_estudante(estudante: schemas.EstudanteCreate, db: Session = Depends(get_db)):
    db_estudante = models.Estudante(
      nome = estudante.nome, 
      email = estudante.email,
      perfil = models.Perfil(**estudante.perfil.model_dump())
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

# endpoint para listar estudantes
@app.get("/estudantes/", response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    # usando joinedload para evitar o problema de N+1 queries
    estudantes = db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return estudantes

# endpoint para ler um estudante específico
@app.get("/estudantes/{estudante_id}", response_model=schemas.Estudante)
def ler_estudante(estudante_id: int, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).filter(models.Estudante.id == estudante_id).first()
    if estudante is None:
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    return estudante