from pydantic import BaseModel
from typing import List, Optional

class Perfil(BaseModel):
    id: int
    idade: int
    endereco: str
    
    class Config:
        from_attribute = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class Estudante(BaseModel):
    id: int
    nome: str
    email: str
    perfil: Optional[Perfil] = None
    
    class Config:
      from_attribute = True

class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: Optional[PerfilCreate] = None
    

class MatriculaBase(BaseModel):
    estudante_id: int
    curso: str

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int

    class Config:
        from_attribute = True