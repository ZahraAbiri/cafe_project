from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,relationship,backref
class Recipt(base):
    __tablename__ = 'recipt'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    total_price = Column('total_price', Integer)
    # total_price_discount = Column('total_price', Integer) todo
    date = Column('date', Date)
    table_parent = relationship("Orders", backref=backref("recipt", uselist=False))
    order_id = Column('order_id', Integer, ForeignKey('orders.order_id'), nullable=True)


base.metadata.create_all(engine)