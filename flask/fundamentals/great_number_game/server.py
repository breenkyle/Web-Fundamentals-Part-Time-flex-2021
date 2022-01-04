from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "per aspera ad astra"

@app.route('/')
def index():
    session.clear()
    bg = "bg-info"
    session['random_num'] = random.randint(1,100)
    print(session['random_num'])
    return render_template('index.html', bg=bg)

@app.route('/guess', methods=['POST'])
def guess():
    session['number'] = int(request.form['num'])
    print(session['number'])
    message = ""

    if 'atttempts' in session:
        print(f'This attempts exist{session["attempts"]}')
    else:
        session['attempts'] = 0

    if session['random_num'] > session['number']:
        message = "Too Low!"
        bg = "bg-warning"
        session['attempts'] += 1
        print(session['attempts'])
    elif session['random_num'] < session['number']:
        message = "Too High!"
        bg = "bg-danger"
        print(session['attempts'])
    else:
        return redirect('/winner')
    return render_template('guess.html', message = message, bg=bg)

@app.route('/winner')
def winner():
    message = (f'Congratulations {session["number"]} is correct!')
    bg = "bg-success"
    return render_template('winner.html', bg=bg, message=message)


if __name__ == "__main__":
    app.run(debug=True)