from src.entities.Tratamento import tratamento
from src.repositories.base_repository import BaseRepository

class TratamentoRepository(BaseRepository[tratamento]):
    def __init__(self, session):
        super().__init__(tratamento, session)