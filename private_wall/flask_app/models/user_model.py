from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

db_name='private_wall_schema'

class User():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['first_name']) < 2:
            flash('First name must be at least 2 characters')
            is_valid=False
        if len(data['last_name']) < 2:
            flash('Last name must be at least 2 characters')
        if not EMAIL_REGEX.match(data['email']):
            flash('Email is invalid')
            is_valid=False
        if  User.get_by_email({'email': data['email']}):
            flash('Email is already in use')
            is_valid=False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters')
            is_valid=False
        if not any(char.isdigit() for char in data['password']):
            flash('Password should have at least one number')
            is_valid = False
        if not any(char.isupper() for char in data['password']):
            flash('Password should have at least one uppercase letter')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash('Passwords do not match')
            is_valid=False
        return is_valid

    @classmethod
    def save(cls, data):
        query='INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL(db_name).query_db(query, data)


    @classmethod
    def get_by_email(cls, data):
        query='Select * from users where email = %(email)s'
        data=connectToMySQL(db_name).query_db(query, data)
        if data == ():
            return False
        else:
            return cls(data[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db_name).query_db(query,data)
        return cls(results[0])