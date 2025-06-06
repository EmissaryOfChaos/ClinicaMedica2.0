from repositories.medicamento_repository import MedicamentoRepository
from entities.Medicamento import Medicamento
from services.base_service import BaseService
from sqlalchemy.orm import Session


class MedicamentoService(BaseService[Medicamento, MedicamentoRepository]):
    def __init__(self, session: Session):
        super().__init__(MedicamentoRepository(session))

    def buscar_por_nome(self, nome: str):
        return self.repository.get_by_nome(nome)

    def criar_medicamento(self, data: dict):
        medicamento = Medicamento(
            nome=data["nome"],
            dosagem=data["dosagem"],
            forma_apresentacao=data.get("forma_apresentacao", "Comprimido"),
            qtd_estoque=data.get("qtd_estoque", 0)
        )
        return self.repository.create(medicamento)

    def atualizar_medicamento(self, medicamento_id: int, data: dict):
        medicamento = self.repository.get_by_id(medicamento_id)
        if not medicamento:
            return None

        for key, value in data.items():
            if hasattr(medicamento, key):
                setattr(medicamento, key, value)

        return self.repository.update(medicamento)