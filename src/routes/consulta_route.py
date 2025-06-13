from flask import Blueprint, jsonify, request
from services.consulta_service import ConsultaService

consulta_bp = Blueprint("Consulta", __name__, url_prefix="/consultas")

@consulta_bp.route("/", methods=["GET"])
def listar_consultas():
    return jsonify(ConsultaService.listar())

@consulta_bp.route("/paciente/<int:paciente_id>", methods=["GET"])
def listar_consultas_por_paciente(paciente_id):
    return jsonify(ConsultaService.listar_por_paciente(paciente_id))

@consulta_bp.route("/", methods=["POST"])
def criar_consulta():
    data = request.get_json()
    resultado = ConsultaService.criar(data)
    return resultado

@consulta_bp.route("/<int:consulta_id>", methods=["DELETE"])
def deletar_consulta(consulta_id):
    return ConsultaService.deletar(consulta_id)