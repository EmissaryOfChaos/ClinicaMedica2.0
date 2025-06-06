from controllers.base_controller import BaseController
from services.posologia_service import PosologiaService
from core.database import SessionLocal

class PosologiaController(BaseController):
    service_class = PosologiaService

    @classmethod
    def listar_por_tratamento(cls, tratamento_id: int):
        session = SessionLocal()
        posologias = cls.service_class(session).listar_por_tratamento(tratamento_id)
        session.close()
        return [p.to_dict() for p in posologias]