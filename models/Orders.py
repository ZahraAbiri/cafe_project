# from core.db_manager import base, Column, Integer, String, Date, ForeignKey, engine, relationship, backref
import psycopg2
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref

from core.db_manager import engine
from models.Menu_items import Menu_item

base = declarative_base()
session = session.sessionmaker(bind=engine)()



class Orders(base):
    __tablename__ = 'orders'
    _id = Column('order_id', Integer, unique=True, primary_key=True)
    number = Column('number', Integer)
    status = Column('status', String(50))
    date = Column('date', Date)


base.metadata.create_all(engine)


