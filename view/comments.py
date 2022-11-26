import app
import json
from urllib import response

from flask import render_template, flash, Flask, request

from models.Comments import Comments, save_comment


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
        return render_template('home.html')