from controllers.base_controller import BaseController
from services.paciente_service import PacienteService

class PacienteController(BaseController):
    service_class = PacienteService