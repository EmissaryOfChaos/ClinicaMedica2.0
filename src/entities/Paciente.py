from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from entities.Pessoa import Pessoa

class Paciente(Pessoa):
    __tablename__ = "paciente"
    __table_args__ = {'extend_existing': True}

    prontuario = Column("prontuario", String(100), nullable=False)

    consulta = relationship("Consulta", back_populates="paciente", cascade="all, delete-orphan", passive_deletes=True)

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


    