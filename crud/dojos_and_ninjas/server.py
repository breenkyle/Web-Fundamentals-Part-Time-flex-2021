from flask_app import app                                               # Import flask app
from flask_app.controllers import dojos_controller                      # Import Controllers

if __name__=="__main__":   
    app.run(debug=True)    