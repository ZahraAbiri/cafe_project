from flask import render_template, request

from app import app
from models.Reciept import save_orders


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


@app.route("/tab", methods=['POST', 'GET'])
def tables_or():
    if request.method == 'POST':
        result = str(request.form.keys())
        s = str(request.form.keys()).split(":")
        str(request.form.keys()).split(":")[1].replace("\"", "").replace(",t", "")
        a = s[1].replace("\"", "").replace(",t", "")
        b = s[2].replace("\"", "").replace(",p", "")
        c = s[3].replace("}\'])", "").replace("\"", "")
        print(a, b, c)
        save_orders(a, b, c)
    return "ff"

