from routes.base_route import BaseRoute
from src.services.medico_service import MedicoService

medico_route = BaseRoute("medico", "/medicos", MedicoService)
medico_bp = medico_route.blueprint