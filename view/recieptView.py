from flask import render_template, request, make_response

from app import app
from models.Reciept import read_test, read_recipt,get_order_item


@app.route('/recipt/<r_id>', methods=['GET'])
def recipt(r_id):
    item = get_order_item(r_id)
    return render_template('recipt.HTML', data=read_recipt(r_id),dt=item)


@app.route('/reciptlist', methods=['GET'])
def recipt_list():
    return render_template('recipt_list.html', data=read_test())

@app.route('/test', methods=['GET'])
def recipt_list_item():
    return render_template('test.html', data=get_order_item())

