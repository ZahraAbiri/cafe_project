import psycopg2
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/resturant')
base = declarative_base()
session = session.sessionmaker(bind=engine)()


class Comments(base):
    __tablename__ = 'comments'
    _id = Column('id', Integer, unique=True, primary_key=True)
    description = Column('description', String(255))
    date = Column('date', Date)
    cus_id = Column('customer_id', Integer, ForeignKey('customer.customer_id'), nullable=True)
    name = Column('name', String(100))
    family = Column('family', String(100))
    phone_number = Column('phone_number', String(10))

class Customer(base):
    __tablename__ = 'customer'
    _id = Column('customer_id', Integer, unique=True, primary_key=True, nullable=False)
    name = Column('name', String(100))
    family = Column('family', String(100))
    phone_number = Column('phone_number', String(10))
    username = Column('username', String(20))
    password = Column('password', String(8))

class Student(base):
    __tablename__ = 'student'
    _id = Column('customer_id', Integer, unique=True, primary_key=True, nullable=False)
    name = Column('name', String(100))
    family = Column('family', String(100))

class Tables(base):
    __tablename__ = 'tables'
    _id = Column('table_id', Integer, unique=True, primary_key=True)
    position = Column('position', String(255))
    number = Column('number', Integer)


class Menu_item(base):
    __tablename__ = 'menu_item'
    _id = Column('menu_item_id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    price = Column('price', Integer)
    category = Column('category_id', Integer, ForeignKey('categories.id'), nullable=True)
    description = Column('description', String(255))
    def __str__(self):
        return f'name:{self.name},price:{self.price},description:{self.description}'

class Orders(base):
    __tablename__ = 'orders'
    _id = Column('order_id', Integer, unique=True, primary_key=True)
    number = Column('number', Integer)
    status = Column('status', String(50))
    date = Column('date', Date)
    tbl_id = Column('table_id', Integer, ForeignKey('tables.table_id'), nullable=True)


class Recipt(base):
    __tablename__ = 'recipt'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    total_price = Column('total_price', Integer)
    # total_price_discount = Column('total_price', Integer) todo
    date = Column('date', Date)
    order_id = Column('order_id', Integer, ForeignKey('orders.order_id'), nullable=True)


class Order_menu_items(base):
    __tablename__ = 'order_menu_items'
    _id = Column('id', Integer, unique=True, primary_key=True)
    order_id = Column('order_id', Integer, ForeignKey('orders.order_id'), nullable=True)
    menu_item_id = Column('menu_item_id', Integer, ForeignKey('menu_item.menu_item_id'), nullable=True)
    number = Column('number', Integer)


class Categories(base):
    __tablename__ = 'categories'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))


base.metadata.create_all(engine)
