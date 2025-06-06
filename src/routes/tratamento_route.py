from routes.base_route import BaseRoute
from services.tratamento_service import TratamentoService

tratamento_route = BaseRoute("tratamento", "/tratamentos", TratamentoService)
tratamento_bp = tratamento_route.blueprint