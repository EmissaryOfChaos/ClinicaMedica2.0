from entities.Especialidade import Especialidade
from repositories.base_repository import BaseRepository
from typing import List

class EspecialidadeRepository(BaseRepository[Especialidade]):
    def __init__(self, session):
        super().__init__(Especialidade, session)