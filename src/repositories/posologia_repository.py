from entities.Posologia import Posologia
from repositories.base_repository import BaseRepository

class PosologiaRepository(BaseRepository[Posologia]):
    def __init__(self, session):
        super().__init__(Posologia, session)

    def get_by_id(self, posologia_id: int):
        return self.session.query(Posologia).filter(Posologia.id == posologia_id).first()
