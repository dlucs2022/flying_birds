from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from database.config import SQLALCHEMY_DATABASE_URL, development

ENGINE = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    echo_pool=development,
)

SESSION_LOCAL = sessionmaker(
    bind=ENGINE,
    autocommit=False,
    autoflush=False,
)
BASE = declarative_base()
