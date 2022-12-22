# from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,relationship,backref
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, scoped_session, sessionmaker
from sqlalchemy.testing import db

from core.db_manager import engine
from models.Menu_items import Menu_item
from models.Order_menu_item import Order_menu_items

base = declarative_base()
session = session.sessionmaker(bind=engine)()
from models.Orders import Orders

from sqlalchemy import text


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
        b = ord._id
        menu_item = session.query(Menu_item).filter(Menu_item.name == x).first()
        Ord_men = Order_menu_items(order_id=b, menu_item_id=menu_item._id, table_id=int(table))
        session.add(Ord_men)

    session.commit()

def read_test():
    rec = session.query(Recipt).all()
    return rec

def read_recipt(data):
    recipt1 = session.query(Recipt).filter(Recipt._id == data).first()
    return recipt1

def get_order_item(id):

    que = f'SELECT m.name,m.price,r.total_price from  Menu_item m left join Order_menu_items om on m.menu_item_id=om.menu_item_id left join Orders o on o.order_id=om.order_id left join Recipt r on r.order_id=o.order_id where r.id={id}'
    sql = text(que)
    result = engine.execute(sql).all()
    return result
