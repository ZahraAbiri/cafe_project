import psycopg2
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session , relationship

engine = create_engine('postgresql://postgres:Mahboube.1@127.0.0.1:5432/resturant')
base = declarative_base()
session = session.sessionmaker(bind=engine)()


class Comments(base):
    __tablename__ = 'comments'
    _id = Column('id', Integer, unique=True, primary_key=True)
    description = Column('description', String(255))
    date = Column('date', Date)
    cus_id = Column('customer_id', Integer, ForeignKey('customer.customer_id'), nullable=True)


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
    # pic_adrs = Column('pic_address' ,String(50) )
    category = Column('category_id', Integer, ForeignKey('categories.id'), nullable=True)

    def __repr__(self):
        return f'name: {self.name} , price : {self.price}'


class Orders(base):
    __tablename__ = 'orders'
    _id = Column('order_id', Integer, unique=True, primary_key=True)
    number = Column('number', Integer)
    status = Column('status', String(50))
    date = Column('date', Date)
    tbl_id = Column('table_id', Integer, ForeignKey('tables.table_id'), nullable=True)

# order1 = Orders(number = 20, status = 'pending', tbl_id = )

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
    categories = relationship('Menu_item' , backref = 'item category')


base.metadata.create_all(engine)

# item = Menu_item(_id = 2, name = 'pizza', price = 5000 , category = 2)
# item2 = Menu_item(_id = 3, name = 'cake', price = 1000 , category = 3)
# session.add(item2)
# session.commit()

# all = session.query(Menu_item).all()
# for i in all:
#     print(i)


