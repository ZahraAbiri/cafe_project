from flask import render_template, request

from app import app
from models.Comments import Comments, save_comment
from models.Menu_items import select_lunch, select_breakfast,\
    select_salad, select_drink, select_deserts, select_dinner


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        result = request.form
        comments = Comments(name=result.get('name'), family=result.get('surname'), phone_number=result.get('phone'),
                            description=result.get('Description'))
        save_comment(comments)
        # flash('You were successfully logged in')

        return render_template('result.html')
    # breakefast,lunch,dinner,desserts,salads,drinks
    else:
        return render_template('home.html',dinner=select_dinner())
