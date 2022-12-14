from flask import render_template, request, redirect

from app import app
from models.user import find_user


@app.route("/login", methods=['POST', 'GET'])
def user_log_in():
    if request.method == 'POST':
        result = request.form
        isExsist = find_user(result)
        if isExsist == 0:
            return redirect('/tables')
        elif isExsist == 1:
            return redirect('/casher')
        else:
            return redirect('/user_sign_in')
    else:
        return render_template('loginPage.html')


