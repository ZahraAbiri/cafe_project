from flask import render_template, request, redirect

from app import app
from models.user import signIn


@app.route("/user_sign_in", methods=['POST', 'GET'])
def user_sign_in():
    if request.method == 'POST':
        result = request.form
        signIn(result)
        return redirect('/login')
    else:
        return render_template('signIn.html')
