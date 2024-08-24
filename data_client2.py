import sqlite3


class Sqlite2():

    __CONNECTION = sqlite3.connect('sqlite2.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS zaprosprognoz 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        index_ob TEXT,
        index_smr TEXT,
        index_obor TEXT,
        index_proch TEXT);'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with (self.__CONNECTION as self.sql):
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM zaprosprognoz ''')
            return self.cursor.fetchall()

    # def select2(self, list_id):
    #     result_list = list()
    #     with (self.__CONNECTION as self.sql):
    #         self.cursor = self.sql.cursor()
    #         for one_id in list_id.split(','):
    #             self.cursor.execute('''SELECT * FROM zapros1 WHERE id = ?''', (int(one_id),))
    #             result_list.append(self.cursor.fetchone())
    #         return result_list

    def select2(self, list_id):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            placeholders = ', '.join(['?'] * len(list_id))
            query = f"SELECT * FROM zaprosprognoz WHERE id IN ({placeholders})"
            self.cursor.execute(query, list_id)
            return self.cursor.fetchall()

    def update(self,id,data,index_ob,index_smr,index_obor,index_proch):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE zaprosprognoz SET data=?,index_ob= ?,index_smr=?,index_obor=?,index_proch=? WHERE id = ?''',(data,index_ob,index_smr,index_obor,index_proch,id))

    def insert(self, **param):
        with self.__CONNECTION as self.sql:
            self.sql.execute(
                '''INSERT INTO zaprosprognoz
                (data,index_ob,index_smr,index_obor,index_proch) 
                VALUES(?,?,?,?,?)''',
                (param['data'], param['index_ob'], param['index_smr'], param['index_obor'],param['index_proch']))

    def delete(self, id):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM zapros1 WHERE id = ?''', (id,))




