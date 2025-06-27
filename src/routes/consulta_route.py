from flask import Blueprint, jsonify, request
from services.consulta_service import ConsultaService
from core.database import get_session

consulta_bp = Blueprint("Consulta", __name__, url_prefix="/consultas")

@consulta_bp.route("/", methods=["GET"])
def listar_consultas():
    session = get_session()
    try:
        service = ConsultaService(session)
        consultas = service.listar()
        return jsonify([c.to_dict() for c in consultas])
    finally:
        session.close()

@consulta_bp.route("/<int:consulta_id>", methods=["GET"])
def buscar_por_id(consulta_id):
    session = get_session()
    try:
        service = ConsultaService(session)
        consulta = service.buscar_por_id(consulta_id)
        if consulta:
            return jsonify(consulta.to_dict())
        return jsonify({"erro": "Consulta não encontrada"}), 404
    finally:
        session.close()

@consulta_bp.route("/", methods=["POST"])
def criar_consulta():
    session = get_session()
    try:
        service = ConsultaService(session)
        resultado = service.criar(data=request.get_json())
        return jsonify(resultado.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        session.close()

@consulta_bp.route('/<int:consulta_id>', methods=['PUT'])
def atualizar_consulta(consulta_id):
    session = get_session()
    try:
        service = ConsultaService(session)
        data = request.get_json()
        consulta = service.atualizar_consulta(consulta_id, data)
        if consulta:
            return jsonify(consulta.to_dict()), 200
        else:
            return jsonify({"erro": "Consulta não encontrada"}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        session.close()

@consulta_bp.route('/<int:id>', methods=['DELETE'])
def deletar_consulta(id):
    session = get_session()
    try:
        service = ConsultaService(session)
        service.deletar(id)  # Aqui estava faltando o 'id'
        return jsonify({"mensagem": "Paciente deletado com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400