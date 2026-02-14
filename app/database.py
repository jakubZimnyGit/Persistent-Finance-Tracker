from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import SQLALCHEMY_DATABASE_URL
import contextlib

Base = declarative_base()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)

@contextlib.contextmanager
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
