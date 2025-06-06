from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from entities.Base import Base

SessionLocal = None
engine = None

def get_session():
    if SessionLocal is None:
        raise Exception("SessionLocal não inicializado. Chame init_db(app) antes de usar o banco.")
    return SessionLocal()

def init_db(app):
    global SessionLocal, engine
    # Agora usa a configuração do app (que vem do config.py)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    @app.before_request
    def before_request():
        app.session = SessionLocal()

    @app.teardown_request
    def teardown_request(exception=None):
        SessionLocal.remove()

    Base.metadata.create_all(bind=engine)