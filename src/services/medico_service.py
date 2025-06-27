from repositories.medico_repository import MedicoRepository
from entities.Medico import Medico
from datetime import datetime
from services.base_service import BaseService
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime


class MedicoService(BaseService[Medico, MedicoRepository]):
    def __init__(self, session: Session):
        super().__init__(MedicoRepository(session))

    def criar_medico(self, data: dict):
        # Validação 5: CPF obrigatório
        if not data.get("cpf"):
            raise ValueError("CPF é obrigatório.")

        # Validação 6: Data de nascimento obrigatória
        if not data.get("data_nascimento"):
            raise ValueError("Data de nascimento é obrigatória.")
        
        # Converta a string para date, se necessário
        if isinstance(data["data_nascimento"], str):
            data["data_nascimento"] = datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date()

        # Validação 7: CRM obrigatório
        if not data.get("crm"):
            raise ValueError("CRM é obrigatório.")

        # Validação nome não pode conter números
        if any(char.isdigit() for char in data["nome"]):
            raise ValueError("Nome não pode conter números.")

        # Validação 2: Médico não pode ter mais de 110 anos
        idade = self.calcular_idade(data["data_nascimento"])
        if idade > 110:
            raise ValueError("Idade não pode ser superior a 110 anos.")

        # Validação 11: CRM não pode ser duplicado
        if self.repository.get_by_crm(data["crm"]):
            raise ValueError("CRM já cadastrado.")

        # Validação CPF não pode ser duplicado
        if self.repository.get_by_cpf(data["cpf"]):
            raise ValueError("CPF já cadastrado.")

        medico = Medico(
            nome=data["nome"],
            data_nascimento=data["data_nascimento"],
            cpf=data["cpf"],
            telefone=data["telefone"],
            crm=data["crm"],
            especialidade_id=data["especialidade_id"]
        )
        return self.repository.create(medico)

    def atualizar_medico(self, medico_id: int, data: dict):
        medico = self.repository.get_by_id(medico_id)
        if not medico:
            return None

        for key, value in data.items():
            if hasattr(medico, key):
                setattr(medico, key, value)

        return self.repository.update(medico)
    
    criar = criar_medico

    @staticmethod
    def calcular_idade(data_nascimento):
        hoje = date.today()
        return hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )