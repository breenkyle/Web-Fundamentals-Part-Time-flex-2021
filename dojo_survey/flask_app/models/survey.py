# from multiprocessing.spawn import is_forking
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from validation.dojo_survey.server import result

# TARGETDATABASE = 'dojo_survey_schema'
# TABLENAME = "users"

class Survey:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Must choose a Dojo location.")
            is_valid = False
        if len(survey['language']) < 1:
            flash("Must choose a favorite language.")
            is_valid = False
        if len(survey['comments']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        # elif len(data['comment']) >255:
        #     flash("Comment must be less than 255 characters.")
        #     is_valid = False
        return is_valid

    @classmethod
    def save(data):
        query = "INSERT into dojos (name,location,language,comments) VALUES (( %(name)s , %(location)s , %(language)s , %(comment)s );"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def get_last_survey():
        query = "SELECT * FROM dojos ORDER BY surveys.id DESC LIMIT 1;"
        results - connectToMySQL('dojo_survey_schema').query_db(query)
        return Survey(results[0])



    # @classmethod
    # def create(cls, data ):
    #     query = "INSERT INTO " + TABLENAME +" (name, location, language, comment) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s );"
    #     return connectToMySQL(TARGETDATABASE).query_db( query, data)


    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM " + TABLENAME + ";"
    #     results = connectToMySQL(TARGETDATABASE).query_db(query)
    #     list_of_instances = []
    #     for class_instance in results:
    #         list_of_instances.append( cls(class_instance) )
    #     return list_of_instances

    # @classmethod
    # def get_one(cls, data:dict):
    #     query = "SELECT * FROM " + TABLENAME +"WHERE id = %(id)s;"
    #     results = connectToMySQL(TARGETDATABASE).query_db(query, data)

    #     return cls(results[0])

    # @classmethod
    # def update_one(cls, data:dict):
    #     query = "UPDATE " + TABLENAME +" SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
    #     return connectToMySQL(TARGETDATABASE).query_db(query, data)

