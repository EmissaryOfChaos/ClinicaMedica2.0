from sqlalchemy import Column, Integer, String, Float
from entities.Base import Base

class Medicamento(Base):
    __tablename__ = 'medicamento'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nome = Column(String(45), nullable=False)
    dosagem = Column(Float, nullable=False)
    forma_apresentacao = Column(String(20), nullable=False, default="Comprimido/Xarope")
    qtd_estoque = Column(Integer, nullable=True)

    def __init__(self, nome, dosagem, forma_apresentacao, qtd_estoque):
        self.nome = nome
        self.dosagem = dosagem
        self.forma_apresentacao = forma_apresentacao
        self.qtd_estoque = qtd_estoque

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'dosagem': self.dosagem,
            'forma_apresentacao': self.forma_apresentacao,
            'qtd_estoque': self.qtd_estoque
        }





    