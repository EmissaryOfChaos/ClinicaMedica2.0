from entities.Medico import Medico
from repositories.base_repository import BaseRepository
from typing import Optional

class MedicoRepository(BaseRepository[Medico]):
    def __init__(self, session):
        super().__init__(Medico, session)