from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="Per audacia ad astra."

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/add_two')
def add_two():
    session['count'] += 2
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)