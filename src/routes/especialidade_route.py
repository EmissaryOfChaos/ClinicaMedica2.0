from routes.base_route import BaseRoute
from services.especialidade_service import EspecialidadeService

especialidade_route = BaseRoute("Especialidade", "/especialidades", EspecialidadeService)
especialidade_bp = especialidade_route.blueprint