from repositories.tratamento_repository import TratamentoRepository
from repositories.consulta_repository import ConsultaRepository
from entities.Tratamento import tratamento
from services.base_service import BaseService
from sqlalchemy.orm import Session


class TratamentoService(BaseService[tratamento, TratamentoRepository]):
    def __init__(self, session: Session):
        super().__init__(TratamentoRepository(session))
        self.consulta_repo = ConsultaRepository(session)

    def listar_por_consulta(self, consulta_id: int):
        return self.repository.get_by_consulta_id(consulta_id)

    def criar_tratamento(self, data: dict):
        if not self.consulta_repo.get_by_id(data["consulta_id"]):
            raise ValueError("Consulta não encontrada.")

        tratamento = tratamento(
            descricao=data["descricao"],
            data_inicio=data["data_inicio"],
            data_fim=data.get("data_fim"),
            consulta_id=data["consulta_id"]
        )
        return self.repository.create(tratamento)