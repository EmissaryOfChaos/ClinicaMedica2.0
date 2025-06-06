from controllers.base_controller import BaseController
from services.medico_service import MedicoService

class MedicoController(BaseController):
    service_class = MedicoService