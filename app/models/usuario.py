from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from config.connection import db

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    email = Column(String(250))
    senha = Column(String(250))

    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

class PontosDeColeta(Base):
    __tablename__ = "pontosdecoleta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250))
    endereco = Column(String(250))
    horarioFuncionamento = Column(String(250))

    def __init__(self, nome: str, endereco: str, hoarioFuncionamento: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.horarioFuncionamento = hoarioFuncionamento

class MaterialReciclavel(Base):
    __tablename__ = "materialreciclavel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(250))
    descricao = Column(String(250))

    def __init__(self, tipo: str, descricao: str) -> None:
        self.tipo = tipo
        self.descricao = descricao

Base.metadata.create_all(bind=db)