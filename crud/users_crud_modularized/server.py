from flask_app import app
# ...server.py
from flask_app.controllers import users


from user import User





if __name__ == "__main__":
    app.run(debug=True)
