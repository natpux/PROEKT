import sqlite3


class Sqlite():

    __CONNECTION = sqlite3.connect('sqlite.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS zapros1 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        Normativ TEXT,
        Kod_KKM TEXT,
        Naimenovanie_materiala TEXT,
        Naimenovanie_smeta TEXT,
        Ediniza_izm TEXT,
        PTM TEXT,Haracteristica TEXT,
        Primechanie TEXT,
        PRICE TEXT);'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with (self.__CONNECTION as self.sql):
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM zapros1''')
            return self.cursor.fetchall()

    # def select2(self, list_id):
    #     result_list = list()
    #     with (self.__CONNECTION as self.sql):
    #         self.cursor = self.sql.cursor()
    #         for one_id in list_id.split(','):
    #             self.cursor.execute('''SELECT * FROM zapros1 WHERE id = ?''', (int(one_id),))
    #             result_list.append(self.cursor.fetchone())
    #         return result_li                                                        st
    # def select2(self, list_id):
    #     with self.__CONNECTION as self.sql:
    #         self.cursor = self.sql.cursor()
    #         placeholders = ', '.join(['?'] * len(list_id))
    #         query = f"SELECT * FROM zapros1 WHERE id IN ({placeholders})"
    #         self.cursor.execute(query, list_id)
    #         return self.cursor.fetchall()

    def select2(self, list_id):
        list_id1 = list_id.split(',')
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            placeholders = ', '.join(['?'] * len(list_id1))
            query = f"SELECT * FROM zapros1 WHERE id IN ({placeholders})"
            self.cursor.execute(query, list_id1)
            return self.cursor.fetchall()


    def update(self,id,Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE zapros1 SET Normativ=?,Kod_KKM = ?,Naimenovanie_materiala=?,Naimenovanie_smeta=?,Ediniza_izm=?,PTM=?,Haracteristica=?,Primechanie=?,PRICE=? WHERE id = ?''',(Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE,id))

    def insert(self, **param):
        with self.__CONNECTION as self.sql:
            self.sql.execute(
                '''INSERT INTO zapros1 
                (Normativ,Kod_KKM,
                Naimenovanie_materiala,
                Naimenovanie_smeta,
                Ediniza_izm,
                PTM,
                Haracteristica,
                Primechanie,PRICE) 
                VALUES(?,?,?,?,?,?,?,?,?)''',
                (param['Normativ'], param['Kod_KKM'], param['Naimenovanie_materiala'], param['Naimenovanie_smeta'],
                 param['Ediniza_izm'], param['PTM'], param['Haracteristica'], param['Primechanie'], param['PRICE']))

    def delete(self, id):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM zapros1 WHERE id = ?''', (id,))










# a=Sqlite()
#
# a.insert('Е8-409-1','1/10-1/10','ТРУБЫ ПВХ 25ММ','2,05 БЕЛ.Р.')#,'ТРУБА 25 ММ','ШТ','Ж6-90-90','ПОЛИВИНИЛХЛОРИД',"Волс национ.аэопорт")
# a.insert('Е8-912-1','1/10-1/11','КАБЕЛЬ ПВХ ВВБГНГ 3Х1,5','3,4 БЕЛ.Р')#,'КАБЕЛЬ ВВГНБГ 3Х1,5 М','М','Ж6-90-90','БРОНИРОВАННЫЙ',"аэропорт")
# a.update(56,'ljkj','hkhjk','jhkh','ljlkj')
# a.select()

# a.insert('Е8-912-1','1/10-1/11','КАБЕЛЬ ПВХ ВВБГНГ 3Х1,5','3,4 БЕЛ.Р')
#
