from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from core.database import get_session
from typing import Type

class BaseRoute:
    def __init__(self, name: str, url_prefix: str, service_class: Type):
        self.blueprint = Blueprint(name, __name__, url_prefix=url_prefix)
        self.service_class = service_class

        self.blueprint.add_url_rule("/", view_func=self.listar, methods=["GET"])
        self.blueprint.add_url_rule("/<int:entity_id>", view_func=self.buscar_por_id, methods=["GET"])
        self.blueprint.add_url_rule("/", view_func=self.criar, methods=["POST"])
        self.blueprint.add_url_rule("/<int:entity_id>", view_func=self.deletar, methods=["DELETE"])

    def get_service(self) -> Session:
        session = get_session()
        service = self.service_class(session)
        return session, service

    def listar(self):
        session, service = self.get_service()
        try:
            entidades = service.listar()
            return jsonify([e.to_dict() for e in entidades])
        finally:
            session.close()

    def buscar_por_id(self, entity_id: int):
        session, service = self.get_service()
        try:
            entidade = service.buscar_por_id(entity_id)
            if entidade:
                return jsonify(entidade.to_dict())
            return jsonify({"erro": "Não encontrado"}), 404
        finally:
            session.close()

    def criar(self):
        session, service = self.get_service()
        data = request.get_json()
        try:
            entidade = service.criar(data)
            return jsonify(entidade.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400
        finally:
            session.close()

    def deletar(self, entity_id: int):
        session, service = self.get_service()
        try:
            entidade = service.deletar(entity_id)
            if entidade:
                return jsonify({"mensagem": "Deletado com sucesso"})
            return jsonify({"erro": "Não encontrado"}), 404
        finally:
            session.close()
    