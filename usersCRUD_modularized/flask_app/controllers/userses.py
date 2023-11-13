from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import UsersCR

@app.route("/")
def index():
    users = UsersCR.get_all()
    print(users)
    return render_template("table.html", users = users)

@app.route("/form")
def form():
    users = UsersCR.get_all()
    print(users)
    return render_template("form.html", users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
    }
    UsersCR.save(data)
    #print("Route routing!")
    return redirect('/')

@app.route('/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    user=UsersCR.get_one(data)
    return render_template("show_user.html",user=user)

@app.route('/edit/<int:id>')
def update(id):
    data = {
        'id' : id
        }
    users = UsersCR.get_one(data)
    return render_template('update.html', users = users)

@app.route('/update_user/<int:id>', methods=["POST"])
def edit(id):
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    UsersCR.edit(data)
    return redirect(f"/show/{id}")

@app.route('/delete/<int:id>')
def delete(id):
    UsersCR.delete(id)
    return redirect('/')
