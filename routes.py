from flask import render_template, url_for, flash, redirect, Flask, request
from models.mdels import *
from core.db_manager import *

app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template('home.html')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#@app.route('/',methods=['POST', 'GET'])
#def student():
 #   if request.method == 'POST':
 #       result = request.form
 #       student = Student(name=result.get('Name'), family=result.get('family'))
  #      add(student)
'''
        flash('You were successfully logged in')

        return render_template('student.html')

    else:
        return render_template('student.html')
'''
# @app.route('/recipt',methods=['GET'])
# def recipt():
#     x = read_test(1)
#     return render_template('recipt.HTML', data=x)
#
# @app.route('/reciptlist',methods=['GET'])
# def recipt_list():
#     x = read_test(1)
#     return render_template('recipt_list.html', data=x)

@app.route('/recipt',methods=['GET'])
def recipt():
    return render_template('recipt.HTML', data=read_recipt())

@app.route('/reciptlist',methods=['GET'])
def recipt_list():
    return render_template('recipt_list.html', data=read_recipt())