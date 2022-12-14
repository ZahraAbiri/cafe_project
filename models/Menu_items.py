from psycopg2 import Date
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, relationship

from core.db_manager import engine

from models.Category import Categories


base = declarative_base()
session = session.sessionmaker(bind=engine)()



class Menu_item(base):
    __tablename__ = 'menu_item'
    _id = Column('menu_item_id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    price = Column('price', Integer)
    category = Column('category_id', Integer, ForeignKey(Categories._id), nullable=True)
    description = Column('description', String(255))

    def __str__(self):
        return f'name:{self.name},price:{self.price},description:{self.description}'

    @property
    def id(self):
        return self._id


base.metadata.create_all(engine)


def select_dinner():
    dinner = session.query(Menu_item).filter(Menu_item.category == 1).all()
    return dinner


def select_lunch():
    lunch = session.query(Menu_item).filter(Menu_item.category == 4).all()
    return lunch


def select_deserts():
    desert = session.query(Menu_item).filter(Menu_item.category == 3).all()
    return desert


def select_drink():
    drink = session.query(Menu_item).filter(Menu_item.category == 2).all()
    return drink


def select_breakfast():
    breakfast = session.query(Menu_item).filter(Menu_item.category == 6).all()
    return breakfast


def select_salad():
    salad = session.query(Menu_item).filter(Menu_item.category == 5).all()
    return salad


def delete_menu_items(id):
    session.query(Menu_item).filter(Menu_item._id == id).delete()
    session.commit()


def update_menu_items(id, name, price, description):
    updateMenuItem = session.query(Menu_item).filter(Menu_item._id == id).first()
    updateMenuItem.name = name
    updateMenuItem.price = price
    updateMenuItem.description = description
    session.commit()


def get_menu_item():
    menu_item = session.query(Menu_item).all()
    return menu_item

def add_menu_items(result):
    category = session.query(Categories).filter(Categories.name == result.get('categories')).first()
    menu_item = Menu_item(name=result.get('newname'), price=result.get('price'),
                          description=result.get('description'),
                          category=category._id)
    session.add(menu_item)
    session.commit()
