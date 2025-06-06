from flask import Blueprint, jsonify, request
from services.posologia_service import PosologiaService
from core.database import SessionLocal

posologia_bp = Blueprint("posologia", __name__, url_prefix="/posologias")

@posologia_bp.route("/", methods=["GET"])
def listar_posologias():
    session = SessionLocal()
    service = PosologiaService(session)
    posologias = service.listar()
    session.close()
    return jsonify([p.to_dict() for p in posologias])

@posologia_bp.route("/<int:entity_id>", methods=["GET"])
def buscar_posologia(entity_id):
    session = SessionLocal()
    service = PosologiaService(session)
    posologia = service.buscar_por_id(entity_id)
    session.close()
    if posologia:
        return jsonify(posologia.to_dict())
    return jsonify({"erro": "Posologia não encontrada"}), 404

@posologia_bp.route("/", methods=["POST"])
def criar_posologia():
    session = SessionLocal()
    service = PosologiaService(session)
    data = request.get_json()
    try:
        posologia = service.criar(data)
        session.close()
        return jsonify(posologia.to_dict()), 201
    except ValueError as e:
        session.close()
        return jsonify({"erro": str(e)}), 400

@posologia_bp.route("/<int:entity_id>", methods=["DELETE"])
def deletar_posologia(entity_id):
    session = SessionLocal()
    service = PosologiaService(session)
    posologia = service.deletar(entity_id)
    session.close()
    if posologia:
        return jsonify({"mensagem": "Posologia deletada"})
    return jsonify({"erro": "Posologia não encontrada"}), 404