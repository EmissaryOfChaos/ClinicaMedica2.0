from core.database import SessionLocal
from typing import Type

class BaseController:
    service_class: Type

    @classmethod
    def listar(cls):
        session = SessionLocal()
        result = cls.service_class(session).listar()
        session.close()
        return [item.to_dict() for item in result]

    @classmethod
    def buscar(cls, entity_id: int):
        session = SessionLocal()
        entity = cls.service_class(session).buscar_por_id(entity_id)
        session.close()
        return entity.to_dict() if entity else None

    @classmethod
    def criar(cls, data: dict):
        session = SessionLocal()
        try:
            obj = cls.service_class(session).criar(data)
            return obj.to_dict(), 201
        except ValueError as e:
            return {"erro": str(e)}, 400
        finally:
            session.close()

    @classmethod
    def deletar(cls, entity_id: int):
        session = SessionLocal()
        entity = cls.service_class(session).deletar(entity_id)
        session.close()
        if entity:
            return {"mensagem": "Deletado com sucesso"}
        return {"erro": "Não encontrado"}, 404