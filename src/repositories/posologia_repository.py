from src.entities.Posologia import posologia
from src.repositories.base_repository import BaseRepository

class PosologiaRepository(BaseRepository[posologia]):
    def __init__(self, session):
        super().__init__(posologia, session)

    def get_by_tratamento_id(self, tratamento_id: int):
        return self.session.query(posologia).filter(posologia.tratamento_id == tratamento_id).all()
