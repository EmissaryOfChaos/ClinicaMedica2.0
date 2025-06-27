from entities.Paciente import Paciente
from repositories.base_repository import BaseRepository
from typing import Optional

class PacienteRepository(BaseRepository[Paciente]):
    def __init__(self, session):
        super().__init__(Paciente, session)