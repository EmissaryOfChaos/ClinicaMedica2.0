from src.entities.Consulta import consulta
from src.repositories.base_repository import BaseRepository

class ConsultaRepository(BaseRepository[consulta]):
    def __init__(self, session):
        super().__init__(consulta, session)

    def get_by_paciente_id(self, paciente_id: int):
        return self.session.query(consulta).filter(consulta.paciente_id == paciente_id).all()

    def get_by_medico_id(self, medico_id: int):
        return self.session.query(consulta).filter(consulta.medico_id == medico_id).all()