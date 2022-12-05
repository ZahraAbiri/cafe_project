#from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,relationship,backref
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

from core.db_manager import engine
from models.Menu_items import Menu_item
from models.Order_menu_item import Order_menu_items

base = declarative_base()
session = session.sessionmaker(bind=engine)()
from models.Orders import Orders


class Recipt(base):
    __tablename__ = 'recipt'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50), nullable=True)
    total_price = Column('total_price', String(50))
    # total_price_discount = Column('total_price', Integer) todo
    date = Column('date', Date)
    order_id = Column('order_id', Integer, ForeignKey(Orders._id), nullable=True)


base.metadata.create_all(engine)



def save_orders(order, table, price):
    ord = Orders(number=123, status="ordered")
    session.add(ord)
    session.commit()
    res = Recipt(total_price=price, order_id=ord._id)
    session.add(res)
    for x in str(order).split(","):
        menu_item = session.query(Menu_item).filter(Menu_item.name == x).first()
        Ord_men = Order_menu_items(order_id=ord._id, menu_item_id=menu_item._id, table_id=int(table))
        session.add(Ord_men)
        session.commit()


def read_test(id):
    return  session.query(Recipt).get(id)

def read_recipt():
    recipts = session.query(Recipt).all()
    return recipts

