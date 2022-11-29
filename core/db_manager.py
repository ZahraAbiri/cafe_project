from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/resturant')
# base = declarative_base()
# session = session.sessionmaker(bind=engine)()
# base.metadata.create_all(engine)