from controllers.base_controller import BaseController
from services.medicamento_service import MedicamentoService
from core.database import SessionLocal

class MedicamentoController(BaseController):
    service_class = MedicamentoService

    @classmethod
    def buscar_por_nome(cls, nome: str):
        session = SessionLocal()
        medicamentos = cls.service_class(session).buscar_por_nome(nome)
        session.close()
        return [m.to_dict() for m in medicamentos]