from controllers.base_controller import BaseController
from services.tratamento_service import TratamentoService
from core.database import SessionLocal

class TratamentoController(BaseController):
    service_class = TratamentoService

    @classmethod
    def listar_por_consulta(cls, consulta_id: int):
        session = SessionLocal()
        tratamentos = cls.service_class(session).listar_por_consulta(consulta_id)
        session.close()
        return [t.to_dict() for t in tratamentos]