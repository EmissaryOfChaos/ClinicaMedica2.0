from repositories.paciente_repository import PacienteRepository
from entities.Paciente import Paciente
from services.base_service import BaseService
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime


class PacienteService(BaseService[Paciente, PacienteRepository]):
    def __init__(self, session: Session):
        super().__init__(PacienteRepository(session))

    def buscar_por_cpf(self, cpf: str):
        return self.repository.get_by_cpf(cpf)

    def criar_paciente(self, data: dict):
        if not data.get("cpf"):
            raise ValueError("CPF é obrigatório.")

        if not data.get("data_nascimento"):
            raise ValueError("Data de nascimento é obrigatória.")

        # Converta a string para date, se necessário
        if isinstance(data["data_nascimento"], str):
            data["data_nascimento"] = datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date()

        if any(char.isdigit() for char in data["nome"]):
            raise ValueError("Nome não pode conter números.")

        idade = self.calcular_idade(data["data_nascimento"])
        if idade > 110:
            raise ValueError("Idade não pode ser superior a 110 anos.")

        if self.repository.get_by_cpf(data["cpf"]):
            raise ValueError("CPF já cadastrado.")

        paciente = Paciente(
            nome=data["nome"],
            data_nascimento=data["data_nascimento"],
            cpf=data["cpf"],
            telefone=data["telefone"],
            prontuario=data["prontuario"]
        )
        return self.repository.create(paciente)

    criar = criar_paciente

    @staticmethod
    def calcular_idade(data_nascimento):
        hoje = date.today()
        return hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )


    
    
