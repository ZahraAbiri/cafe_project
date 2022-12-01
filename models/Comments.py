# from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,session
import psycopg2
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

from core.db_manager import engine

base = declarative_base()
session = session.sessionmaker(bind=engine)()

class Comments(base):
    __tablename__ = 'comments'
    _id = Column('id', Integer, unique=True, primary_key=True)
    description = Column('description', String(255))
    date = Column('date', Date)
    name = Column('name', String(100))
    family = Column('family', String(100))
    phone_number = Column('phone_number', String(10))
base.metadata.create_all(engine)
def select_comment():
    comment = session.query(Comments).all()
    return comment



def save_comment(comment):
    session.add(comment)
    session.commit()

