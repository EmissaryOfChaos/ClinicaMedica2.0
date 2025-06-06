from routes.base_route import BaseRoute
from services.paciente_service import PacienteService

paciente_route = BaseRoute("Paciente", "/pacientes", PacienteService)
paciente_bp = paciente_route.blueprint