from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from entities.Base import Base 

DATABASE_URL = "mysql+pymysql://usuario:senha@localhost:3306/ClinicaMedica"

# Engine e sessão
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Inicializador
def init_db(app):
    @app.before_request
    def before_request():
        app.session = SessionLocal()

    @app.teardown_request
    def teardown_request(exception=None):
        SessionLocal.remove()

    Base.metadata.create_all(bind=engine)