# db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db.sqlite3", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

"""
Schema:  Data Center -> Router -> Switch -> Computer -> Process -> BESClient
"""

def init_db():
    from models import DataCenter, Router, Switch, Computer, Process
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)

    # create records
    # db_session.commit()
    # db_session.flush()
