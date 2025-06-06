from routes.base_route import BaseRoute
from services.medicamento_service import MedicamentoService

medicamento_route = BaseRoute("Medicamento", "/medicamentos", MedicamentoService)
medicamento_bp = medicamento_route.blueprint