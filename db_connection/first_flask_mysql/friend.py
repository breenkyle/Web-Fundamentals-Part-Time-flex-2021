from mysqlconnection import connectToMySQL
class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # the get_all method will be used when we need to retrieve all the rows of the table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask').query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend) )
        return friends

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation, created_at, updated_at) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        result = connectToMySQL('first_flask').query_db( query, data )
        return result

    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls,id):
        query  = f"SELECT * FROM friends WHERE id = {id}";
        result = connectToMySQL('first_flask').query_db(query)
        return cls(result[0])

    @classmethod
    def update(cls,data, id):
        query = f"UPDATE friends SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = {id};"
        return connectToMySQL('first_flask').query_db(query,data)

    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM friends WHERE id = {id};"
        return connectToMySQL('first_flask').query_db(query)



# # import the function that will return an instance of a connection
# from mysqlconnection import connectToMySQL
# # model the class after the friend table from our database
# class Friend:
#     def __init__( self , data ):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.occupation = data['occupation']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
#     # Now we use class methods to query our database
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM friends;"
#         # make sure to call the connectToMySQL function with the schema you are targeting.
#         results = connectToMySQL('first_flask').query_db(query)
#         # Create an empty list to append our instances of friends
#         friends = []
#         # Iterate over the db results and create instances of friends with cls.
#         for friend in results:
#             friends.append( cls(friend) )
#         return friends


# # import the function that will return an instance of a connection
# from mysqlconnection import connectToMySQL
# # model the class after the friend table from our database
# class Friend:
#     # ... other class methods
#     # class method to save our friend to the database
#     @classmethod
#     def save(cls, data ):
#     # The value placeholders need to correspond with the names of each of your form inputs
#         query = "INSERT INTO friends ( first_name , last_name , occupation) VALUES ( %(fname)s , %(lname)s , %(occ)s);"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL('first_flask').query_db( query, data )

# # Note: We will need to call on the connectToMySQL function every time we want to execute a query because our connection closes as soon as the query finishes executing.