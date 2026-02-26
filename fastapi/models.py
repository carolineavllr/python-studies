from sqlalchemy import \
    Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    perfil = relationship("Perfil", back_populates="estudante", uselist=False,cascade="all, delete-orphan")

class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String(200))
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    estudante = relationship("Estudante", back_populates="perfil")

class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    curso = Column(String(100), nullable=False)
