from routes.base_route import BaseRoute
from services.paciente_service import PacienteService

paciente_route = BaseRoute("paciente", "/pacientes", PacienteService)
paciente_bp = paciente_route.blueprint