from entities.Especialidade import Especialidade
from repositories.base_repository import BaseRepository
from typing import List

class EspecialidadeRepository(BaseRepository[Especialidade]):
    def __init__(self, session):
        super().__init__(Especialidade, session)

    def get_by_nome(self, nome: str) -> List[Especialidade]:
        return self.session.query(Especialidade).filter(Especialidade.nome.like(f"%{nome}%")).all()