import sqlite3

class DataBase:

    def connection(self):
        connection = sqlite3.connect('./data/sqlite.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users ('+
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '+
        'name varchar(255), '+
        'email varchar(255), '+
        'password varchar(255))')
        connection.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS quizzes ('+
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '+
        'user_id INTEGER, '+
        'title varchar(255), '+
        'type TINYINT,'+
        'date_creation DATE)')
        connection.commit()

        return [connection,cursor]

    def insert(self,table,data):
        database = self.connection()
        connection = database[0]
        cursor = database[1]
        cursor.execute('INSERT INTO '+table+' VALUES (null, "'+data.name+'", "'+data.email+'", "'+data.password+'")')
        connection.commit()
        connection.close()

    def select(self,table,select,where):
        database = self.connection()
        connection = database[0]
        cursor = database[1]
        cursor.execute('SELECT '+select+' FROM '+table+' WHERE '+where+'')
        result=cursor.fetchone()
        connection.close()

        return result

