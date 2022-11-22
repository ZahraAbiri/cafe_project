import psycopg2
from models.mdels import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

user='postgres'
#passwd=
host='localhost'
port=5432
db='resturant'

url = f"postgresql://{user}:123456@{host}:{port}/{db}"
#engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/resturant')
engine = create_engine(url)
base = declarative_base()
session = session.sessionmaker(bind=engine)()




def read_test(id):
    return  session.query(Recipt).get(id)

def read_recipt():
    recipt1 = session.query(Recipt).all()
    return recipt1


