from flask import render_template, request

from app import app
from models.Orders import Orders



@app.route("/tables", methods=['POST', 'GET'])
def tables_order():
    if request.method == 'POST':
        # result = request.form
        # comments = Comments(name=result.get('name'), family=result.get('surname'), phone_number=result.get('phone'),
        #                     description=result.get('Description'))
        # save_comment(comments)
        # flash('You were successfully logged in')

        return "uu"
    # breakefast,lunch,dinner,desserts,salads,drinks
    else:
        return render_template('lunchTable.html')
