from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from entities.Pessoa import Pessoa

class Medico(Pessoa):
    __tablename__ = "medico"
    __table_args__ = {'extend_existing': True}

    crm = Column("CRM", String(10), nullable=False)
    
    especialidade_id = Column(Integer, ForeignKey("especialidade.id", ondelete='SET NULL'), nullable=True)
    
    especialidade = relationship("Especialidade", back_populates="medicos")

    def __init__(self, nome, data_nascimento, cpf, telefone, crm, especialidade_id):
        super().__init__(nome, data_nascimento, cpf, telefone)
        self.crm = crm
        self.especialidade_id = especialidade_id

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            'crm': self.crm,
            'especialidade_id': self.especialidade_id,
            'tipo': 'medico'
        })
        return dados