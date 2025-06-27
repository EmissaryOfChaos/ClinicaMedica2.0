from flask import Blueprint, jsonify, request
from services.posologia_service import PosologiaService
from core.database import SessionLocal, get_session

posologia_bp = Blueprint("Posologia", __name__, url_prefix="/posologias")

@posologia_bp.route("/", methods=["GET"])
def listar_posologias():
    session = get_session()
    try:
        service = PosologiaService(session)
        posologias = service.listar()
        return jsonify([p.to_dict() for p in posologias])
    finally:
        session.close()

@posologia_bp.route("/<int:posologia_id>", methods=["GET"])
def buscar_por_id(posologia_id):
    session = get_session()
    try:
        service = PosologiaService(session)
        posologia = service.buscar_por_id(posologia_id)
        if posologia:
            return jsonify(posologia.to_dict())
        return jsonify({"erro": "Posologia não encontrada"}), 404
    finally:
        session.close()

@posologia_bp.route("/", methods=["POST"])
def criar_posologia():
    session = get_session()
    try:
        service = PosologiaService(session)
        resultado = service.criar(data=request.get_json())
        return jsonify(resultado.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        session.close()

@posologia_bp.route('/<int:posologia_id>', methods=['PUT'])
def atualizar_posologia(posologia_id):
    session = get_session()
    try:
        service = PosologiaService(session)
        data = request.get_json()
        posologia = service.atualizar_posologia(posologia_id, data)
        if posologia:
            return jsonify(posologia.to_dict()), 200
        else:
            return jsonify({"erro": "Posologia não encontrada"}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        session.close()

@posologia_bp.route("/<int:entity_id>", methods=["DELETE"])
def deletar_posologia(entity_id):
    session = get_session()
    try:
        service = PosologiaService(session)
        service.deletar(entity_id)  # Aqui estava faltando o 'id'
        return jsonify({"mensagem": "Posologia deletada com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 400