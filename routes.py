from flask import render_template, url_for, flash, redirect, Flask, request
from models.mdels import *
from core.db_manager import *

app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template('home.html')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.route('/',methods=['POST', 'GET'])
def student():
    if request.method == 'POST':
        result = request.form
        student = Student(name=result.get('Name'), family=result.get('family'))
        add(student)
        flash('You were successfully logged in')

        return render_template('student.html')

    else:
        return render_template('student.html')

@app.route('/cashier_panel')
def cashier():
    number_of_items = item_count(Menu_item)
    total = total_price(Menu_item.price)
    data = bring_data(Menu_item)
    return render_template('cashier panel.html',
                           item_number = number_of_items ,
                           price = total,
                           data = data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/home")
def get():
    return render_template("home.html")

@app.route("/hover")
def show_order():
    data = load_order(1)
    return render_template("hover.html" , data = data )