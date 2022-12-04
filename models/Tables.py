# from core.db_manager import base,Column, Integer, String,engine,relationship
import psycopg2
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref

from core.db_manager import engine


base = declarative_base()
session = session.sessionmaker(bind=engine)()


class Tables(base):
    __tablename__ = 'tables'
    _id = Column('table_id', Integer, unique=True, primary_key=True)
    position = Column('position', String(255))
    number = Column('number', Integer)
    # order_id = Column('order_id', Integer, ForeignKey(Orders._id), nullable=True)

#
base.metadata.create_all(engine)

