from repositories.consulta_repository import ConsultaRepository
from entities.Consulta import Consulta
from services.base_service import BaseService
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime


class ConsultaService(BaseService[Consulta, ConsultaRepository]):
    def __init__(self, session: Session):
        super().__init__(ConsultaRepository(session))

    def listar_por_paciente(self, paciente_id: int):
        return self.repository.get_by_paciente_id(paciente_id)

    def criar_consulta(self, data: dict):

         # Converta a string para date, se necessário
        if isinstance(data["data_consulta"], str):
            data["data_consulta"] = datetime.strptime(data["data_consulta"], "%Y-%m-%d").date()

        # Converta a string para time, se necessário
        if isinstance(data["horario"], str):
            data["horario"] = datetime.strptime(data["horario"], "%H:%M").time()

        if data["data_consulta"] < date.today():
            raise ValueError("Não é possível marcar consultas para datas anteriores ao dia atual.")

        consultas_no_dia = self.repository.get_all()
        for consulta in consultas_no_dia:
            if consulta.data_consulta == data["data_consulta"] and consulta.horario == data["horario"]:
                raise ValueError("Já existe uma consulta marcada para este horário.")

        consulta = Consulta(
            paciente_id=data["paciente_id"],
            medico_id=data["medico_id"],
            data_consulta=data["data_consulta"],
            horario=data["horario"]
        )
        return self.repository.create(consulta)
    
    def atualizar_consulta(self, consulta_id: int, data: dict):
        consulta = self.repository.get_by_id(consulta_id)
        if not consulta:
            return None

        for key, value in data.items():
            if hasattr(consulta, key):
                setattr(consulta, key, value)

        return self.repository.update(consulta)
    
    criar = criar_consulta