from entities.Medicamento import Medicamento
from repositories.base_repository import BaseRepository
from typing import List

class MedicamentoRepository(BaseRepository[Medicamento]):
    def __init__(self, session):
        super().__init__(Medicamento, session)

    def get_by_nome(self, nome: str) -> List[Medicamento]:
        return self.session.query(Medicamento).filter(Medicamento.nome.like(f"%{nome}%")).all()