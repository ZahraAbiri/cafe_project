import json

from flask import render_template, request, redirect

from app import app
#
from models.Menu_items import add_menu_items, get_menu_item, delete_menu_items, update_menu_items


@app.route('/add_menu_item', methods=['POST', 'GET'])
def add_menu_item():
    if request.method == 'POST':
        result = request.form
        add_menu_items(result)
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return redirect('/')
    else:
        return render_template('menu_item.html', menu_item=get_menu_item())


@app.route('/delete_menu_item', methods=['POST', 'GET'])
def delete_menu_item():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        delete_menu_items(result.get('id'))
        return redirect('/')


@app.route('/update_menu_item', methods=['POST', 'GET'])
def update_menu_item():
    if request.method == 'POST':
        result =request.form
        id=result.get('idu')
        name=result.get('nameu')
        price=result.get('priceu')
        description=result.get('descriptionu')

        update_menu_items(id,name,price,description)
        return redirect('/')
