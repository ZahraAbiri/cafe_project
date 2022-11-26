from core.db_manager import base,Column, Integer, String, Date,ForeignKey,engine,session

class Comments(base):
    __tablename__ = 'comments'
    _id = Column('id', Integer, unique=True, primary_key=True)
    description = Column('description', String(255))
    date = Column('date', Date)
    cus_id = Column('user_id', Integer, ForeignKey('customer.customer_id'), nullable=True)
    name = Column('name', String(100))
    family = Column('family', String(100))
    phone_number = Column('phone_number', String(10))
base.metadata.create_all(engine)
def select_comment():
    comment = session.query(Comments).all()
    return comment



def save_comment(comment):
    session.add(comment)
    session.commit()

