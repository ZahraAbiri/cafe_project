import json

from flask import render_template, flash, Flask, request

from core.db_manager import select_dinner, save_comment, select_lunch, select_comment, select_deserts, select_drink, \
    select_breakfast, select_salad, add_menu_items, get_menu_item, delete_menu_items, update_menu_items
from models.mdels import Comments

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        result = request.form
        comments = Comments(name=result.get('name'), family=result.get('surname'), phone_number=result.get('phone'),
                            description=result.get('Description'))
        save_comment(comments)
        flash('You were successfully logged in')

        return render_template('result.html')

    else:
        return render_template('home.html', dinner=select_dinner(),
                               lunch=select_lunch(), comments=select_comment()
                               , drinks=select_drink(), salads=select_salad(), desserts=select_deserts(),
                               breakefast=select_breakfast())


@app.route('/add_menu_item', methods=['POST', 'GET'])
def add_menu_item():
    if request.method == 'POST':
        result = request.form
        add_menu_items(result)
        return render_template('menu_item.html')
    else:
        return render_template('menu_item.html', menu_item=get_menu_item())


@app.route('/delete_menu_item', methods=['POST', 'GET'])
def delete_menu_item():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        delete_menu_items(result.get('id'))
        return render_template('menu_item.html')


@app.route('/update_menu_item', methods=['POST', 'GET'])
def update_menu_item():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        id=result.get('id')
        name=result.get('name')
        price=result.get('price')
        description=result.get('description')

        update_menu_items(id,name,price,description)
        return render_template('menu_item.html')
