from repositories.especialidade_repository import EspecialidadeRepository
from entities.Especialidade import especialidade
from services.base_service import BaseService
from sqlalchemy.orm import Session


class EspecialidadeService(BaseService[especialidade, EspecialidadeRepository]):
    def __init__(self, session: Session):
        super().__init__(EspecialidadeRepository(session))

    def buscar_por_nome(self, nome: str):
        return self.repository.get_by_nome(nome)

    def criar_especialidade(self, data: dict):
        especialidade = especialidade(
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