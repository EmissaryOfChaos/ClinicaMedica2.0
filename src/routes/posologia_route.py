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

@posologia_bp.route("/tratamento/<int:tratamento_id>", methods=["GET"])
def listar_por_tratamento(tratamento_id):
    session = get_session()
    try:
        service = PosologiaService(session)
        posologias = service.listar_por_tratamento(tratamento_id)
        return jsonify([p.to_dict() for p in posologias])
    finally:
        session.close()

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