from flask_app.models import burger
from flask_app.config.mysqlconnection import connectToMySQL



class Restaurant:
    def __init__( self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # we create a list so that later we can add in all the burgers that are associated with a restaurant
        self.burger = []

        @classmethod
        def save( cls, data ):
            query = "INSERT INTO restaurants ( name ,  created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
            return connectToMySQL('burgers').query_db(query,data)

        @classmethod
        def get_restaurant_with_burgers( cls, data ):
            query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
            results = connectToMySQL('burgers').query_db( query , data )
            restaurant = cls( results[0] )
            for row_from_db in results:
                # now we parse the burger data to make instances of burgers and add them into our list
                burger_data = {
                    "id" : row_from_db["burgers.id"],
                    "name" : row_from_db["burgers.name"],
                    "bun" : row_from_db["bun"],
                    "meat" : row_from_db["meat"],
                    "calories" : row_from_db["calories"],
                    "created_at" : row_from_db["created_at"],
                    "updated_at" : row_from_db["updated_at"]
                }
                restaurant.burgers.append( burger.Burger( burger_data ) )
            return restaurant


