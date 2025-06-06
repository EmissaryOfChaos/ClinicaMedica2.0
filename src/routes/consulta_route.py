from flask import Blueprint, jsonify, request
from controllers.consulta_controller import ConsultaController

consulta_bp = Blueprint("consulta", __name__, url_prefix="/consultas")

@consulta_bp.route("/", methods=["GET"])
def listar_consultas():
    return jsonify(ConsultaController.listar())

@consulta_bp.route("/paciente/<int:paciente_id>", methods=["GET"])
def listar_consultas_por_paciente(paciente_id):
    return jsonify(ConsultaController.listar_por_paciente(paciente_id))

@consulta_bp.route("/", methods=["POST"])
def criar_consulta():
    data = request.get_json()
    resultado = ConsultaController.criar(data)
    return resultado

@consulta_bp.route("/<int:consulta_id>", methods=["DELETE"])
def deletar_consulta(consulta_id):
    return ConsultaController.deletar(consulta_id)