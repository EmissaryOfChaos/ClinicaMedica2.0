from repositories.tratamento_repository import TratamentoRepository
from repositories.consulta_repository import ConsultaRepository
from entities.Tratamento import Tratamento
from services.base_service import BaseService
from sqlalchemy.orm import Session
from datetime import datetime


class TratamentoService(BaseService[Tratamento, TratamentoRepository]):
    def __init__(self, session: Session):
        super().__init__(TratamentoRepository(session))
        self.consulta_repo = ConsultaRepository(session)

    def criar_tratamento(self, data: dict):
        if not self.consulta_repo.get_by_id(data["consulta_id"]):
            raise ValueError("Consulta não encontrada.")
        
        # Converta a string para date, se necessário
        if isinstance(data["data_inicio"], str):
            data["data_inicio"] = datetime.strptime(data["data_inicio"], "%Y-%m-%d").date()

        # Converta a string para date, se necessário
        if isinstance(data["data_fim"], str):
            data["data_fim"] = datetime.strptime(data["data_fim"], "%Y-%m-%d").date()

        tratamento = Tratamento(
            descricao=data["descricao"],
            data_inicio=data["data_inicio"],
            data_fim=data.get("data_fim"),
            consulta_id=data["consulta_id"]
        )
        return self.repository.create(tratamento)
    
    criar = criar_tratamento