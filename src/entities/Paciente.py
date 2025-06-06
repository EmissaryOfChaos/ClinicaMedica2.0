from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from entities.Base import Base

class paciente(Base):
    __tablename__ = "paciente"

    prontuario = Column("prontuario", String(100), nullable=False)

    consulta = relationship("consulta", back_populates="paciente")

    def __init__(self, nome, data_nascimento, cpf, telefone, prontuario):
        super().__init__(nome, data_nascimento, cpf, telefone)
        self.prontuario = prontuario

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            'prontuario': self.prontuario,
            'tipo': 'paciente'
        })
        return dados


    