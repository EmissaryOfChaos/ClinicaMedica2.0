from sqlalchemy import Column, Integer, String
from entities.Base import Base

class especialidade(Base):
    __tablename__ = 'especialidade'

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }


    