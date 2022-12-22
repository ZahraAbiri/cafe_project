import json

from flask import render_template, request, redirect

from app import app
from models.Orders import get_orders, update_order_status
from models.user import signIn


@app.route("/user_sign_in", methods=['POST', 'GET'])
def user_sign_in():
    if request.method == 'POST':
        result = request.form
        signIn(result)
        return redirect('/login')
    else:
        return render_template('signIn.html')


@app.route("/casher")
def casher_login():
    return render_template('chashierPanel.html', data=get_orders())



@app.route("/testing", methods=['POST', 'GET'])
def c_login():
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        # {'statusOrder': 'kitchen', 'id': '12'}
        orderId = result.get('id')
        status = result.get('statusOrder')
        update_order_status(int(orderId), status)
        return redirect('/')
