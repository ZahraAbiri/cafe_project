import app
import json
from urllib import response

from flask import render_template, flash, Flask, request

from models.Comments import Comments, save_comment

#
from models.Menu_items import add_menu_items, get_menu_item, delete_menu_items, update_menu_items


@app.route('/add_menu_item', methods=['POST', 'GET'])
def add_menu_item():
    if request.method == 'POST':
        result = request.form
        add_menu_items(result)
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return render_template('result.html')
    else:
        return render_template('menu_item.html', menu_item=get_menu_item())


@app.route('/delete_menu_item', methods=['POST', 'GET'])
def delete_menu_item():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        delete_menu_items(result.get('id'))
        return render_template('result.html')


@app.route('/update_menu_item', methods=['POST', 'GET'])
def update_menu_item():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        id=result.get('id')
        name=result.get('name')
        price=result.get('price')
        description=result.get('description')

        update_menu_items(id,name,price,description)
        return render_template('result.html')
