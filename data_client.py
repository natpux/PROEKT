import sqlite3

class Sqlite():
    __CONNECTION = sqlite3.connect('db.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS Zapros(id INTEGER PRIMARY KEY AUTOINCREMENT,Normativ TEXT,Kod KKM TEXT, Naimenovanie materiala(KKM) TEXT, Naimenovanie materiala(smeta) TEXT,Edinica izmerenia ТEXT,PTM(ПТМ) ТEХТ,Haracteristica materiala ТEХТ)'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.executescript(self.__CREATE_SCRIPTS)

    def select(self):
        with (self.__CONNECTION as self.sql):
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT Kod KKM FROM Zapros''')
            return self.cursor.fetchall()
a=Sqlite()
a.select()

