from core.db_manager import base, Column, Integer, ForeignKey, engine,relationship,backref


class Order_menu_items(base):
    __tablename__ = 'order_menu_items'
    _id = Column('id', Integer, unique=True, primary_key=True)
    order_parent = relationship("Orders", backref=backref("order_menu_items", uselist=False))
    order_id = Column('order_id', Integer, ForeignKey('orders.order_id'), nullable=True)
    menuItem_parent = relationship("Menu_item", backref=backref("menuItem_parents", uselist=False))
    menu_item_id = Column('menu_item_id', Integer, ForeignKey('menu_item.menu_item_id'), nullable=True)
    number = Column('number', Integer)

base.metadata.create_all(engine)
