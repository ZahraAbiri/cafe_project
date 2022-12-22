# from core.db_manager import base, Column, Integer, String, Date, ForeignKey, engine, relationship, backref
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

from core.db_manager import engine

base = declarative_base()
session = session.sessionmaker(bind=engine)()


class Orders(base):
    __tablename__ = 'orders'
    _id = Column('order_id', Integer, unique=True, primary_key=True)
    number = Column('number', Integer)
    status = Column('status', String(50))
    date = Column('date', Date)


base.metadata.create_all(engine)


def get_orders():
    que = f'SELECT m.name,o.order_id,o.status from  Menu_item m left join Order_menu_items om on m.menu_item_id=om.menu_item_id left join Orders o on o.order_id=om.order_id where m.menu_item_id=om.menu_item_id'
    sql = text(que)
    result = engine.execute(sql).all()

    return result


def update_order_status(id, status):
    updateStatus = session.query(Orders).filter(Orders._id == id).first()
    updateStatus.status = status
    session.commit()
