from entities.Tratamento import Tratamento
from repositories.base_repository import BaseRepository

class TratamentoRepository(BaseRepository[Tratamento]):
    def __init__(self, session):
        super().__init__(Tratamento, session)