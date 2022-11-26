from core.db_manager import base, Column, Integer, String, engine


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
