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
        self.id = database.insert('users',self.__dict__)
        return True

    def login(self):
        database = sql.DataBase()
        self.password = self.encryptPass(self.password)
        result = database.selectOne('users','id,name,email,password','email="'+self.email+'" AND password="'+self.password+'"')
        try:
            if result[2] == self.email:
                self.id = result[0]
                self.name = result[1]
                return True
        except:
            return False
    
    def encryptPass(self,password):
        encrypt = hashlib.sha256()
        encrypt.update(password.encode('utf8'))
        return encrypt.hexdigest()

        