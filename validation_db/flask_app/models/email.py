from flask_app import app
from flask import flash
import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

db_name='email_val_schema'

class Email():
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query='INSERT INTO emails ( email ) VALUES ( %(email)s );'
        return connectToMySQL(db_name).query_db(query, data)


    @classmethod
    def get_all(cls):
        query= "SELECT * FROM emails;"
        results = connectToMySQL(db_name).query_db(query)
        emails = []
        for row in results:
            emails.append( cls(row) )
        return emails


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(db_name).query_db(query,data)


    # @staticmethod
    # def validate(data):
    #     is_valid=True
    #     if not EMAIL_REGEX.match(data['email']):
    #         flash('Email is invalid!', "error")
    #         is_valid=False
    #     return is_valid


    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(db_name).query_db(query,email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid