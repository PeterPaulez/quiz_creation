import tools.sqlite as sql
import hashlib

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        database = sql.DataBase()
        self.password = self.encryptPass(self.password)
        database.insert('users',self)
    
    def encryptPass(self,password):
        encrypt = hashlib.sha256()
        encrypt.update(password.encode('utf8'))
        return encrypt.hexdigest()

        