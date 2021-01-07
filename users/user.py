import users.sqlite as sql

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        database = sql.DataBase()
        database.insert('users',self)
        