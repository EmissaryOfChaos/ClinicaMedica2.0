
#Os serviços são responsáveis por implementar a lógica de negócios da aplicação. 
#Eles coordenam as operações entre os modelos e os repositórios, aplicando regras de negócios e garantindo a consistência dos dados. 
#Os serviços geralmente contêm a lógica para manipular os dados, realizar validações, executar cálculos e realizar outras tarefas
#relacionadas à funcionalidade específica da aplicação.

from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from repositories.base_repository import BaseRepository

T = TypeVar("T")  # Tipo da entidade
R = TypeVar("R", bound=BaseRepository)  # Tipo do repositório

class BaseService(Generic[T, R]):
    def __init__(self, repository: R):
        self.repository = repository

    def listar(self) -> List[T]:
        return self.repository.get_all()

    def buscar_por_id(self, entity_id: int) -> Optional[T]:
        return self.repository.get_by_id(entity_id)
    
    def atualizar(self, entity_id: int, data: dict) -> Optional[T]:
        entity = self.repository.get_by_id(entity_id)
        if not entity:
            return None
        for key, value in data.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        self.repository.session.commit()
        return entity

    def deletar(self, entity_id: int) -> Optional[T]:
        entity = self.repository.get_by_id(entity_id)
        if not entity:
            return None
        self.repository.delete(entity)
        return entity
