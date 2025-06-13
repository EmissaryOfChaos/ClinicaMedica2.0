from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from entities.Base import Base

class Posologia(Base):
    __tablename__ = 'posologia'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    medicamento_id = Column(Integer, ForeignKey('medicamento.id', ondelete='SET NULL'), nullable=True)
    tratamento_id = Column(Integer, ForeignKey('tratamento.id', ondelete='CASCADE'), nullable=False)
    receita = Column(String(100), nullable=False)
    qtd_utilizada = Column(Integer, nullable=True)

    tratamento = relationship("Tratamento", back_populates="posologias", passive_deletes=True)
    medicamento = relationship("Medicamento", back_populates="posologias", passive_deletes=True)

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