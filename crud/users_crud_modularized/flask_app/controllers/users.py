from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import Users


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/new')
def new():
    return render_template("new.html")

@app.route("/read_one_new")
def read_one_new():
    id_show = User.read_one_new()
    return redirect((f"/read_one/{id_show[0]['MAX(id)']}"))


@app.route("/read_one/<id_from>", methods=["GET"])
def read_one(id_from):
    selected = User.read_one(id_from)
    return render_template("/read_one.html", selected = selected)

@app.route("/edit/<id_from>")
def edit_template(id_from):
    id_from = id_from
    selected = User.read_one(id_from)
    return render_template("edit.html", id_from = id_from, selected = selected)

@app.route("/edit_request/<id_from>", methods=["POST"])
def edit(id_from):
    data = {
        "id_from":id_from,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    print(f"Last Updated on {data}")
    User.edit(data)
    return redirect(f"/read_one/{data['id_from']}")

@app.route("/delete/<id_from>")
def delete(id_from):
    User.delete(id_from)
    return redirect("/users")
