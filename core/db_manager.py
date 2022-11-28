import psycopg2
from models.mdels import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from sqlalchemy.sql import func


engine = create_engine('postgresql://postgres:Mahboube.1@127.0.0.1:5432/resturant')
base = declarative_base()
session = session.sessionmaker(bind=engine)()


def add(student):
    session.add(student)
    session.commit()

def item_count(table_name):
    return session.query(table_name).count()

def total_price(column):
    total = session.query(func.sum(column)).scalar()
    return f'{total} tomans'

# print(total_price(Menu_item.price))
def bring_data(table_name):
    return session.query(table_name).all()

# def pic_adrs_chooser(name):
#     if name == 'pizza':
#         return '01.png'

def load_order(restaurant_table_number):
    data = session.query(Orders).filter(Orders.tbl_id == restaurant_table_number).first()
    return data
# print(bring_data(Menu_item))

x = load_order(1)
print(x.status)