from entities.Posologia import Posologia
from repositories.posologia_repository import PosologiaRepository
from repositories.tratamento_repository import TratamentoRepository
from repositories.medicamento_repository import MedicamentoRepository
from services.base_service import BaseService
from sqlalchemy.orm import Session

class PosologiaService(BaseService[Posologia, PosologiaRepository]):
    def __init__(self, session: Session):
        super().__init__(PosologiaRepository(session))
        self.tratamento_repo = TratamentoRepository(session)
        self.medicamento_repo = MedicamentoRepository(session)
    
    def listar_por_id(self, posologia_id: int):
        return self.repository.get_by_id(posologia_id)

    def criar_posologia(self, data: dict):
        tratamento = self.tratamento_repo.get_by_id(data["tratamento_id"])
        if not tratamento:
            raise ValueError("Tratamento não encontrado.")

        medicamento = self.medicamento_repo.get_by_id(data["medicamento_id"])
        if not medicamento:
            raise ValueError("Medicamento não encontrado.")

        qtd_utilizada = int(data.get("qtd_utilizada", 0))
        if medicamento.qtd_estoque is not None and medicamento.qtd_estoque < qtd_utilizada:
            raise ValueError("Estoque insuficiente para retirada.")

        medicamento.qtd_estoque -= qtd_utilizada
        self.medicamento_repo.update(medicamento)

        posologia = Posologia(
            medicamento_id=data["medicamento_id"],
            tratamento_id=data["tratamento_id"],
            receita=data["receita"],
            qtd_utilizada=qtd_utilizada
        )
        return self.repository.create(posologia)
    
    def atualizar_posologia(self, posologia_id: int, data: dict):
        posologia = self.repository.get_by_id(posologia_id)
        if not posologia:
            return None
        for key, value in data.items():
            if hasattr(posologia, key):
                setattr(posologia, key, value)
        return self.repository.update(posologia)

    criar = criar_posologia