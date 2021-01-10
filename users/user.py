import tools.sqlite as sql
import hashlib

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        database = sql.DataBase()
        self.password = self.encryptPass(self.password)
        database.insert('users',self)
        return True

    def login(self):
        database = sql.DataBase()
        self.password = self.encryptPass(self.password)
        result = database.select('users','name,email,password','email="'+self.email+'" AND password="'+self.password+'"')
        try:
            if result[1] == self.email:
                self.name = result[0]
                return True
        except:
            return False
    
    def encryptPass(self,password):
        encrypt = hashlib.sha256()
        encrypt.update(password.encode('utf8'))
        return encrypt.hexdigest()

        