from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.email import Email
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html',emails=Email.get_all())


@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/success')





#   @app.route('/user/register', methods=['POST'])
#   def register():
#     if User.validate(request.form) == False:
#         return redirect('/')

#     data={
#         'email': request.form['email']
#     }

#     user_id=User.save(data)

#     #Logging them in action
#     session['logged_in_user']=user_id

#     return redirect('/success')