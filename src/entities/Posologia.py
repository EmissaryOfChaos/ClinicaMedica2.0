from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from entities.Base import Base

class posologia(Base):
    __tablename__ = 'posologia'

    id = Column(Integer, primary_key=True)
    medicamento_id = Column(Integer, ForeignKey('medicamento.id'), nullable=False)
    tratamento_id = Column(Integer, ForeignKey('tratamento.id'), nullable=False)
    receita = Column(String(100), nullable=False)
    qtd_utilizada = Column(Integer, nullable=True)

    medicamento = relationship("medicamento")

    def __init__(self, medicamento_id, tratamento_id, receita, qtd_utilizada):
        self.medicamento_id = medicamento_id
        self.tratamento_id = tratamento_id
        self.receita = receita
        self.qtd_utilizada = qtd_utilizada

    def to_dict(self):
        return {
            'id': self.id,
            'medicamento_id': self.medicamento_id,
            'tratamento_id': self.tratamento_id,
            'receita': self.receita,
            'qtd_utilizada': self.qtd_utilizada
        }
