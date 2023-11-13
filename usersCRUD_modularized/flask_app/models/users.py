from flask_app.config.mysqlconnection import connectToMySQL

class UsersCR:
    DB="mydb"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = """INSERT INTO userscr (first_name,last_name,email) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM userscr;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query  = """SELECT * FROM userscr WHERE id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
        #The update method for modifying existing friend data.
    @classmethod
    def edit(cls,data):
        query = """UPDATE userscr 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)

    # the delete method will be used when we need to delete a friend from our database
    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM userscr WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data)