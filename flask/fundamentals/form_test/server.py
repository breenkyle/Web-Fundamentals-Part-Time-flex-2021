# from flask import Flask, render_template
# app = Flask(__name__)
# # our index route will handle rendering our form
# @app.route('/')
# def index():
#     return render_template("index.html")


# from flask import Flask, render_template, request, redirect # added request

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#         # Never render a template on a POST request.
#         # Instead we will redirect to our index route.
#     return redirect('/')


# from flask import Flask, render_template, request, redirect # don't forget to import redirect!

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name = request.form['name']
#     email = request.form['email']
#     return redirect("/show")

# # adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html")


from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

@app.route('/show')
def show_user():
    return render_template('show.html')





if __name__ == "__main__":
    app.run(debug=True)

