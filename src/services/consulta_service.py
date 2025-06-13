from repositories.consulta_repository import ConsultaRepository
from repositories.paciente_repository import PacienteRepository
from repositories.medico_repository import MedicoRepository
from entities.Consulta import Consulta
from services.base_service import BaseService
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime


class ConsultaService(BaseService[Consulta, ConsultaRepository]):
    def __init__(self, session: Session):
        super().__init__(ConsultaRepository(session))
        self.paciente_repo = PacienteRepository(session)
        self.medico_repo = MedicoRepository(session)

    def listar_por_paciente(self, paciente_id: int):
        return self.repository.get_by_paciente_id(paciente_id)

    def listar_por_medico(self, medico_id: int):
        return self.repository.get_by_medico_id(medico_id)

    def criar_consulta(self, data: dict):

         # Converta a string para date, se necessário
        if isinstance(data["data_consulta"], str):
            data["data_consulta"] = datetime.strptime(data["data_consulta"], "%Y-%m-%d").date()

        # Converta a string para date, se necessário
        if isinstance(data["horario"], str):
            data["horario"] = datetime.strptime(data["horario"], "%H:%M").time()

        if data["data_consulta"] < date.today():
            raise ValueError("Não é possível marcar consultas para datas anteriores ao dia atual.")

        consultas_no_dia = self.repository.get_all()
        for consulta in consultas_no_dia:
            if consulta.data_consulta == data["data_consulta"] and consulta.horario == data["horario"]:
                raise ValueError("Já existe uma consulta marcada para este horário.")
            
        if not self.paciente_repo.get_by_id(data["paciente_id"]):
            raise ValueError("Paciente não encontrado.")

        if not self.medico_repo.get_by_id(data["medico_id"]):
            raise ValueError("Médico não encontrado.")

        consulta = Consulta(
            paciente_id=data["paciente_id"],
            medico_id=data["medico_id"],
            data_consulta=data["data_consulta"],
            horario=data["horario"]
        )
        return self.repository.create(consulta)
    
    criar = criar_consulta