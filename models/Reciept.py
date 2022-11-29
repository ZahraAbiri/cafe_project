# from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,relationship,backref
import psycopg2
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref

from core.db_manager import engine

base = declarative_base()
session = session.sessionmaker(bind=engine)()
base.metadata.create_all(engine)

class Recipt(base):
    __tablename__ = 'recipt'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    total_price = Column('total_price', Integer)
    # total_price_discount = Column('total_price', Integer) todo
    date = Column('date', Date)
    order_id = Column('order_id', Integer, ForeignKey('orders.order_id'), nullable=True)


base.metadata.create_all(engine)