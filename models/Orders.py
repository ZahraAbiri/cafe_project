from core.db_manager import base, Column, Integer, String, Date, ForeignKey, engine, relationship, backref


class Orders(base):
    __tablename__ = 'orders'
    _id = Column('order_id', Integer, unique=True, primary_key=True)
    number = Column('number', Integer)
    status = Column('status', String(50))
    date = Column('date', Date)
    # category = Column('category_id', Integer, ForeignKey('categories.id'), nullable=True)
    table_parent = relationship("Tables", backref=backref("orders", uselist=False))
    tbl_id = Column('table_id', Integer, ForeignKey('tables.table_id'), nullable=True)


base.metadata.create_all(engine)
