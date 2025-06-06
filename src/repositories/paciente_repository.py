from src.entities.Paciente import paciente
from src.repositories.base_repository import BaseRepository
from typing import Optional

class PacienteRepository(BaseRepository[paciente]):
    def __init__(self, session):
        super().__init__(paciente, session)

    def get_by_cpf(self, cpf: str) -> Optional[paciente]:
        return self.session.query(paciente).filter(paciente.cpf == cpf).first()