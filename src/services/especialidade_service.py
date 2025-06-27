from repositories.especialidade_repository import EspecialidadeRepository
from entities.Especialidade import Especialidade
from services.base_service import BaseService
from sqlalchemy.orm import Session


class EspecialidadeService(BaseService[Especialidade, EspecialidadeRepository]):
    def __init__(self, session: Session):
        super().__init__(EspecialidadeRepository(session))

    def criar_especialidade(self, data: dict):
        especialidade = Especialidade(
            nome=data["nome"]
        )
        return self.repository.create(especialidade)

    def atualizar_especialidade(self, especialidade_id: int, data: dict):
        especialidade = self.repository.get_by_id(especialidade_id)
        if not especialidade:
            return None

        for key, value in data.items():
            if hasattr(especialidade, key):
                setattr(especialidade, key, value)

        return self.repository.update(especialidade)
    
    criar = criar_especialidade