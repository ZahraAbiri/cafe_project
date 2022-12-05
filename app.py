from flask import Flask

from models.Comments import Comments, save_comment

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


from flask import render_template, request

from view.commentsView import home
from view.menuItemView import add_menu_items,delete_menu_item,update_menu_items
from  view.signinView import user_sign_in
from  view.loginView import user_log_in
from  view.getOrdersView import tables_order,tables_or
from  view.recieptView import read_recipt,recipt

app.run(debug=True)