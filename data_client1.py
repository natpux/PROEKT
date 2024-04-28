
import sqlite3
class Sqlite():


    __CONNECTION = sqlite3.connect('sqlite.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS zapros1 (id INTEGER PRIMARY KEY AUTOINCREMENT,Normativ TEXT,Kod_KKM TEXT,Naimenovanie_materiala TEXT,Naimenovanie_smeta TEXT,Ediniza_izm TEXT,PTM TEXT,Haracteristica TEXT,Primechanie TEXT,PRICE TEXT);'''
   # __CREATE_SCRIPTS2 = '''CREATE TABLE IF NOT EXISTS zapros2 (id INTEGER PRIMARY KEY AUTOINCREMENT,Naimenovanie_smeta TEXT,Edinica_izmer ТEXT,PTM ТEXT,Haracteristica_mat ТEXT,FOREIGN KEY(id) REFERENCES zapros1(id));'''
   # __CREATE_SCRIPTS3 = '''CREATE TABLE IF NOT EXISTS STROIKA (id INTEGER PRIMARY KEY AUTOINCREMENT,Naimenovanie_stroika TEX,FOREIGN KEY(id) REFERENCES zapros1(id));'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)
            #self.sql.execute(self.__CREATE_SCRIPTS2)
            #self.sql.execute(self.__CREATE_SCRIPTS3)

    #def select(self) -> object:
     #   with self.__CONNECTION as self.sql:
     #       [print(*data) for data in self.sql.cursor().execute('''SELECT * FROM zapros1''').fetchall()]

    def select(self):
        with (self.__CONNECTION as self.sql):
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM zapros1''')
            return self.cursor.fetchall()


            #[print(*data) for data in self.sql.cursor().execute('''SELECT * FROM zapros2''').fetchall()]
            #[print(*data) for data in self.sql.cursor().execute('''SELECT * FROM STROIKA''').fetchall()]

    def select2(self,id,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12):
        with (self.__CONNECTION as self.sql):
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM zapros1 WHERE id IN(?,?,?,?,?,?,?,?,?,?,?,?)''', (id,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12))
            return self.cursor.fetchall()

    # Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat,Naimenovanie_stroika):
    # def update(self, id, Normativ, Kod_KKM, Naimenovanie_materiala, PRICE, Naimenovanie_smeta, Edinica_izmer, PTM,Haracteristica_mat, Naimenovanie_stroika):
    def update(self,id,Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE):
        with self.__CONNECTION as self.sql:
           #  self.sql.execute('''UPDATE zapros1 SET Normativ = ?,Kod_KKM = ?,Naimenovanie_materiala=?,PRICE=? ,id = ?''', (id,Normativ,Kod_KKM,Naimenovanie_materiala,PRICE))
           # self.sql.execute('''UPDATE zapros2 SET Naimenovanie_smeta = ? Edinica_izmer= ? PTM=? Haracteristica_mat=? WHERE id = ?''', (Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat,id))
            self.sql.execute('''UPDATE zapros1 SET Normativ=?,Kod_KKM = ?,Naimenovanie_materiala=?,Naimenovanie_smeta=?,Ediniza_izm=?,PTM=?,Haracteristica=?,Primechanie=?,PRICE=? WHERE id = ?''',(Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE,id))

    # def update(self, id, login, password):
    #     with self.__CONNECTION as self.sql:
    #         self.sql.execute('''UPDATE person SET login = ?, password = ? WHERE id = ?''', (login, hash(password), id))

    def insert(self, Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE):#Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat,Naimenovanie_stroika):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO zapros1(Normativ,Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE) VALUES(?,?,?,?,?,?,?,?,?)''', (Normativ, Kod_KKM,Naimenovanie_materiala,Naimenovanie_smeta,Ediniza_izm,PTM,Haracteristica,Primechanie,PRICE))
            #self.sql.execute('''INSERT INTO zapros2(Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat) VALUES(?,?,?,?)''', (Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat))
            #self.sql.execute('''INSERT INTO STROIKA(Naimenovanie_stroika) VALUES(?)''', (Naimenovanie_stroika,))

    def delete(self, id):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM zapros1 WHERE id = ?''', (id,))
            #self.sql.execute('''DELETE FROM zapros2 WHERE id = ?''',(id,))










# a=Sqlite()
#
# a.insert('Е8-409-1','1/10-1/10','ТРУБЫ ПВХ 25ММ','2,05 БЕЛ.Р.')#,'ТРУБА 25 ММ','ШТ','Ж6-90-90','ПОЛИВИНИЛХЛОРИД',"Волс национ.аэопорт")
# a.insert('Е8-912-1','1/10-1/11','КАБЕЛЬ ПВХ ВВБГНГ 3Х1,5','3,4 БЕЛ.Р')#,'КАБЕЛЬ ВВГНБГ 3Х1,5 М','М','Ж6-90-90','БРОНИРОВАННЫЙ',"аэропорт")
# a.update(56,'ljkj','hkhjk','jhkh','ljlkj')
# a.select()

# a.insert('Е8-912-1','1/10-1/11','КАБЕЛЬ ПВХ ВВБГНГ 3Х1,5','3,4 БЕЛ.Р')
#
