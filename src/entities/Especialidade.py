from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from entities.Base import Base


class Especialidade(Base):
    __tablename__ = 'especialidade'
    __table_args__ = {'extend_existing': True}

    medicos = relationship("Medico", back_populates="especialidade")

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome
        }


    