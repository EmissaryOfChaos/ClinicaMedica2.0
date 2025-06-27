from entities.Medico import Medico
from repositories.base_repository import BaseRepository
from typing import Optional

class MedicoRepository(BaseRepository[Medico]):
    def __init__(self, session):
        super().__init__(Medico, session)
    
    def get_by_crm(self, crm: str) -> Optional[Medico]:
        return self.session.query(Medico).filter(Medico.crm == crm).first()
    
    def get_by_cpf(self, cpf: str):
        return self.session.query(Medico).filter(Medico.cpf == cpf).first()