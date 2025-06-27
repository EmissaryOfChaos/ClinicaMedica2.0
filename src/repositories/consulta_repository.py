from entities.Consulta import Consulta
from repositories.base_repository import BaseRepository

class ConsultaRepository(BaseRepository[Consulta]):
    def __init__(self, session):
        super().__init__(Consulta, session)
    
    def get_by_paciente_id(self, paciente_id: int):
        return self.session.query(Consulta).filter_by(paciente_id=paciente_id).all()
    
    