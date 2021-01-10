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
        'data TEXT,'+
        'date_creation DATE)')
        connection.commit()

        return [connection,cursor]

    def insert(self,table,data):
        database = self.connection()
        connection = database[0]
        cursor = database[1]
        # KEYS
        keys = ''
        for key in data.keys():
            keys += f'"{key}",'
        keys = keys[:-1]
        # VALUES
        values = ''
        for value in data.values():
            values += f'"{value}",'
        values = values[:-1]

        # QUERY
        cursor.execute('INSERT INTO '+table+' ('+keys+') VALUES ('+values+')')
        connection.commit()
        connection.close()

        return cursor.lastrowid

    def select(self,table,select,where):
        database = self.connection()
        connection = database[0]
        cursor = database[1]
        cursor.execute('SELECT '+select+' FROM '+table+' WHERE '+where+'')
        result=cursor.fetchone()
        connection.close()

        return result

    def update(self,table,update,where):
        database = self.connection()
        connection = database[0]
        cursor = database[1]
        cursor.execute('UPDATE '+table+' SET '+update+' WHERE '+where+'')
        connection.commit()
        connection.close()

        return cursor.rowcount
