from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s, %(last_name)s , %(email)s);"

        #comes back as the new id
        result = connectToMySQL('users_schema').query_db( query, data )
        return result

    @classmethod
    def read_one(cls, selected_id):
        query = (f"SELECT * FROM USERS WHERE id = {selected_id};")
        selection_one = connectToMySQL('users_schema').query_db(query)
        return selection_one

    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id_from)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete(cls, id_from):
        query = (f"DELETE FROM users WHERE id = {id_from};")
        return connectToMySQL('users_schema').query_db(query)

    @classmethod
    def read_one_new(cls):
        query = "SELECT MAX(id) FROM users;"
        return connectToMySQL('users_schema').query_db(query)