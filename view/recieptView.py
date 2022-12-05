from flask import render_template, request, make_response

from app import app
from models.Reciept import read_test, read_recipt


@app.route('/recipt/<r_id>', methods=['GET'])
def recipt(r_id):
    return render_template('recipt.HTML', data=read_recipt(r_id))


@app.route('/reciptlist', methods=['GET'])
def recipt_list():
    return render_template('recipt_list.html', data=read_test())


