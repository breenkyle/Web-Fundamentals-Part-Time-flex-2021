from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", num = 3)

@app.route('/play/<int:num>')
def play(num):
    return render_template("index.html", num = num)
# inputting '7' returns an error on the webpage


@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("index.html", num = num, color = color)

# @app.route('/play/<int:x>/<string:color>')
# def second(x, color):
#     return render_template('index.html', times=x, color=color)

if __name__=="__main__":
    app.run(debug=True)