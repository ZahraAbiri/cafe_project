# from core.db_manager import base, Column, Integer, ForeignKey, engine,relationship,backref
import psycopg2
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship, backref

from core.db_manager import engine


base = declarative_base()
session = session.sessionmaker(bind=engine)()
from models.Menu_items import Menu_item
from models.Orders import Orders
from models.Tables import Tables
#

class Order_menu_items(base):
    __tablename__ = 'order_menu_items'
    _id = Column('id', Integer, unique=True, primary_key=True)
    menu_item_id = Column('menu_item_id', Integer, ForeignKey(Menu_item._id), nullable=True)
    order_id = Column('order_id', Integer, ForeignKey(Orders._id), nullable=True)
    table_id = Column('table_id', Integer, ForeignKey(Tables._id), nullable=True)
    recipt_id = Column('recipt_id', Integer, nullable=True)
    number = Column('number', Integer)

base.metadata.create_all(engine)
