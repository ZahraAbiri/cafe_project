# from core.db_manager import base, Column, Integer, String, engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

from core.db_manager import engine

base = declarative_base()
session = session.sessionmaker(bind=engine)()



class User(base):
    __tablename__ = 'user'
    _id = Column('user_id', Integer, unique=True, primary_key=True, nullable=False)
    name = Column('name', String(100))
    role = Column('role', String(100))
    family = Column('family', String(100))
    phone_number = Column('phone_number', String(10))
    username = Column('username', String(20))
    password = Column('password', String(8))


base.metadata.create_all(engine)


def signIn(result):
    users = User(name=result.get('name'), family=result.get('family'), phone_number=result.get('phone')
                 , password=result.get('password'), username=result.get('username'))
    session.add(users)
    session.commit()


def find_user(result):
    user = session.query(User).filter(User.username == result.get('userid') ,
                                      User.password == result.get('passw')).first()

    if user is not None and user.role=='cashier':
        return 1
    elif user is not None:
        return 0
    else:
        return -1
