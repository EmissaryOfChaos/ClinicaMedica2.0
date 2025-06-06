from controllers.base_controller import BaseController
from services.especialidade_service import EspecialidadeService
from core.database import SessionLocal

class EspecialidadeController(BaseController):
    service_class = EspecialidadeService

    @classmethod
    def buscar_por_nome(cls, nome: str):
        session = SessionLocal()
        especialidades = cls.service_class(session).buscar_por_nome(nome)
        session.close()
        return [e.to_dict() for e in especialidades]