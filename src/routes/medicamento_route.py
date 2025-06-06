from routes.base_route import BaseRoute
from services.medicamento_service import MedicamentoService

medicamento_route = BaseRoute("medicamento", "/medicamentos", MedicamentoService)
medicamento_bp = medicamento_route.blueprint