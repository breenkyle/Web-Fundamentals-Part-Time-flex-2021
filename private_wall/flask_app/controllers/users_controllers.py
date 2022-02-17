from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.message_model import Message
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/register', methods=['POST'])
def register():
    if User.validate(request.form) == False:
        return redirect('/')
    pw_hash=bcrypt.generate_password_hash(request.form['password'])
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id=User.save(data)
    #Logging them in action
    session['user_id']=user_id
    return redirect('/user_wall')

# @app.route('/success')
# def success():
#     return render_template('success.html')

@app.route('/user_wall')
def user_wall():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    messages = Message.get_user_messages(data)
    sent_messages = Message.sent_messages(data)
    users = User.get_all()
    return render_template("user_wall.html", user = user, users = users, messages = messages, sent_messages = sent_messages)


@app.route('/user/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/user_wall")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')




# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/dashboard')
# def dashboard():
#     print("******** in dashboard *******************")
#     if not 'lu_id' in session:
#         print("User is not logged in, redirect to root login")
#         return redirect("/")                                                # If not logged in, redirect to root login
#     data = {
#         'id': session['lu_id']
#     }
#     print("data:")
#     print(data)
#     user = login_model.LoginUsers.get_one(data)                             # Retrive user's info from db and make a user instance
#     print("User:")
#     print(user)
#     return render_template("dashboard.html", user=user) 