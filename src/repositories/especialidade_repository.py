from src.entities.Especialidade import especialidade
from src.repositories.base_repository import BaseRepository
from typing import List

class EspecialidadeRepository(BaseRepository[especialidade]):
    def __init__(self, session):
        super().__init__(especialidade, session)

    def get_by_nome(self, nome: str) -> List[especialidade]:
        return self.session.query(especialidade).filter(especialidade.nome.like(f"%{nome}%")).all()