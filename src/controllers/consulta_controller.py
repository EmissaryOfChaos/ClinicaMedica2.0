from controllers.base_controller import BaseController
from services.consulta_service import ConsultaService
from core.database import SessionLocal

class ConsultaController(BaseController):
    service_class = ConsultaService

    @classmethod
    def listar_por_paciente(cls, paciente_id: int):
        session = SessionLocal()
        consultas = cls.service_class(session).listar_por_paciente(paciente_id)
        session.close()
        return [c.to_dict() for c in consultas]