from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session


from models.mdels import Menu_item,Comments,Customer,Categories

engine = create_engine('postgresql://postgres:123456@127.0.0.1:5432/resturant')
base = declarative_base()
session = session.sessionmaker(bind=engine)()
base.metadata.create_all(engine)


def add(student):
    session.add(student)
    session.commit()


def select_comment():
    comment = session.query(Comments).all()
    return comment


def select_dinner():
    dinner = session.query(Menu_item).filter(Menu_item.category == 2).all()
    return dinner


def select_lunch():
    lunch = session.query(Menu_item).filter(Menu_item.category == 1).all()
    return lunch


def select_deserts():
    desert = session.query(Menu_item).filter(Menu_item.category == 3).all()
    return desert


def select_drink():
    drink = session.query(Menu_item).filter(Menu_item.category == 4).all()
    return drink


def select_breakfast():
    breakfast = session.query(Menu_item).filter(Menu_item.category == 6).all()
    return breakfast


def select_salad():
    salad = session.query(Menu_item).filter(Menu_item.category == 5).all()
    return salad


def save_comment(comment):
    session.add(comment)
    session.commit()


def delete_menu_items(id):
    session.query(Menu_item).filter(Menu_item._id == id).delete()
    session.commit()


def update_menu_items(id,name,price,description):
    updateMenuItem = session.query(Menu_item).filter(Menu_item._id == id).first()
    updateMenuItem.name=name
    updateMenuItem.name=price
    updateMenuItem.name=description
    session.commit()

def get_menu_item():
    menu_item = session.query(Menu_item).all()
    return menu_item

def add_menu_items(result):
    category = session.query(Categories).filter(Categories.name == result.get('categories')).first()
    menu_item = Menu_item(name=result.get('newname'), price=result.get('price'), description=result.get('description'),
                     category=category._id)
    session.add(menu_item)
    session.commit()
