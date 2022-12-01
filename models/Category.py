from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

from core.db_manager import engine

base = declarative_base()
session = session.sessionmaker(bind=engine)()



class Categories(base):
    __tablename__ = 'categories'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))


base.metadata.create_all(engine)
