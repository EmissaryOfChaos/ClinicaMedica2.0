from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from entities.Base import Base

class tratamento(Base):
    __tablename__ = 'tratamento'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(100), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=True)
    consulta_id = Column(Integer, ForeignKey('consulta.id'), nullable=False)

    posologias = relationship("posologia", backref="tratamento", cascade="all, delete-orphan")

    def __init__(self, descricao, data_inicio, data_fim, consulta_id):
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.consulta_id = consulta_id

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'data_inicio': self.data_inicio.isoformat() if self.data_inicio else None,
            'data_fim': self.data_fim.isoformat() if self.data_fim else None,
            'consulta_id': self.consulta_id
        }


    