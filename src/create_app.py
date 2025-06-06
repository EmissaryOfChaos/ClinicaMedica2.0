from flask import Flask
from flask_cors import CORS
from routes.paciente_route import paciente_bp
from routes.medico_route import medico_bp
from routes.consulta_route import consulta_bp
from routes.tratamento_route import tratamento_bp
from routes.posologia_route import posologia_bp
from routes.medicamento_route import medicamento_bp
from routes.especialidade_route import especialidade_bp
from core.database import init_db
from config import Config

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco
    init_db(app)

    # Libera o CORS para consumir a API
    CORS(app)

    # Registro de rotas (blueprints)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(medico_bp)
    app.register_blueprint(consulta_bp)
    app.register_blueprint(tratamento_bp)
    app.register_blueprint(posologia_bp)
    app.register_blueprint(medicamento_bp)
    app.register_blueprint(especialidade_bp)

    return app