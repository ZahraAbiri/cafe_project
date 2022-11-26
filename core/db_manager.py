import psycopg2
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/resturant2')
base = declarative_base()
session = session.sessionmaker(bind=engine)()
base.metadata.create_all(engine)