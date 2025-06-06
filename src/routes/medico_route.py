from routes.base_route import BaseRoute
from services.medico_service import MedicoService

medico_route = BaseRoute("Medico", "/medicos", MedicoService)
medico_bp = medico_route.blueprint