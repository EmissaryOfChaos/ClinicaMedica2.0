from src.entities.Medicamento import medicamento
from src.repositories.base_repository import BaseRepository
from typing import List

class MedicamentoRepository(BaseRepository[medicamento]):
    def __init__(self, session):
        super().__init__(medicamento, session)

    def get_by_nome(self, nome: str) -> List[medicamento]:
        return self.session.query(medicamento).filter(medicamento.nome.like(f"%{nome}%")).all()