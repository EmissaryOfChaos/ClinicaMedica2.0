from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from entities.Base import Base

class Consulta(Base):
    __tablename__ = 'consulta'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    paciente_id = Column(Integer, ForeignKey('paciente.id'), nullable=False)
    medico_id = Column(Integer, ForeignKey('medico.id'), nullable=False)
    data_consulta = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)

    paciente = relationship("Paciente", backref="consultas", passive_deletes=True)
    medico = relationship("Medico", backref="consultas", passive_deletes=True)
    tratamentos = relationship("Tratamento", back_populates="consulta", cascade="all, delete-orphan")

    def __init__(self, paciente_id, medico_id, data_consulta, horario):
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.data_consulta = data_consulta
        self.horario = horario

    def to_dict(self):
        return {
            'id': self.id,
            'paciente_id': self.paciente_id,
            'medico_id': self.medico_id,
            'data_consulta': self.data_consulta.isoformat() if self.data_consulta else None,
            'horario': self.horario.strftime('%H:%M') if self.horario else None
        }



    