from src.entities.Medico import medico
from src.repositories.base_repository import BaseRepository
from typing import Optional

class MedicoRepository(BaseRepository[medico]):
    def __init__(self, session):
        super().__init__(medico, session)

    def get_by_crm(self, crm: str) -> Optional[medico]:
        return self.session.query(medico).filter(medico.crm == crm).first()