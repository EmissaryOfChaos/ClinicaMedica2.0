from sqlalchemy import Column, Integer, String, Date
from entities.Base import Base

class Pessoa(Base):
    __abstract__ = True  # Não cria tabela no banco

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    telefone = Column(String(11), nullable=False)

    def __init__(self, nome, data_nascimento, cpf, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone = telefone

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'cpf': self.cpf,
            'telefone': self.telefone,
        }
