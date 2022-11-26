from core.db_manager import base,Column, Integer, String,engine,relationship


class Tables(base):
    __tablename__ = 'tables'
    _id = Column('table_id', Integer, unique=True, primary_key=True)
    position = Column('position', String(255))
    number = Column('number', Integer)
    order=relationship('Orders',backref='for order id')
#
base.metadata.create_all(engine)

