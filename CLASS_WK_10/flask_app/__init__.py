#(INITIALIZE)not in templates folder, goes in flask_app folder
# we are going to be breaking up the server.py file, it has too much going on. 


from flask import Flask 
app = Flask(__name__)

app.secret_key = "Py is goodness"    
# sessions and protection ^

