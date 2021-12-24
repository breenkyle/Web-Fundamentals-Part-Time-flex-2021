from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:anything>')
def say_name(anything):
    return f"Hi {anything.capitalize()}!"


@app.route('/repeat/<int:num>/<string:anything>')
def repeat_anything(num,anything):
    output = ''

    for i in range(0,num):
        output += f"<p>{anything}</p>"
    
    return output
#this repeats on seperate lines now

if __name__=="__main__":
    app.run(debug=True)
