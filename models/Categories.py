from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine



class Categories(base):
    __tablename__ = 'categories'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))


base.metadata.create_all(engine)