from repositories.posologia_repository import PosologiaRepository
from repositories.tratamento_repository import TratamentoRepository
from repositories.medicamento_repository import MedicamentoRepository
from entities.Posologia import Posologia
from services.base_service import BaseService
from sqlalchemy.orm import Session


class PosologiaService(BaseService[Posologia, PosologiaRepository]):
    def __init__(self, session: Session):
        super().__init__(PosologiaRepository(session))
        self.tratamento_repo = TratamentoRepository(session)
        self.medicamento_repo = MedicamentoRepository(session)

    def listar_por_tratamento(self, tratamento_id: int):
        return self.repository.get_by_tratamento_id(tratamento_id)

    def criar_posologia(self, data: dict):
        tratamento = self.tratamento_repo.get_by_id(data["tratamento_id"])
        if not tratamento:
            raise ValueError("Tratamento não encontrado.")

        medicamento = self.medicamento_repo.get_by_id(data["medicamento_id"])
        if not medicamento:
            raise ValueError("Medicamento não encontrado.")

        qtd_utilizada = data.get("qtd_utilizada", 0)
        if medicamento.qtd_estoque is not None and medicamento.qtd_estoque < qtd_utilizada:
            raise ValueError("Estoque insuficiente para retirada.")

        # Atualiza estoque
        medicamento.qtd_estoque -= qtd_utilizada
        self.medicamento_repo.update(medicamento)

        posologia = Posologia(
            medicamento_id=data["medicamento_id"],
            tratamento_id=data["tratamento_id"],
            receita=data["receita"],
            qtd_utilizada=qtd_utilizada
        )
        return self.repository.create(posologia)
    
    criar = criar_posologia
