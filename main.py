
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QLineEdit,QRadioButton,QLabel,QPushButton, QToolTip,QMessageBox, QDesktopWidget,QTableWidget
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QCoreApplication
from data_client1 import Sqlite
from PyQt5 import uic, QtWidgets
###ИМПОРТ ДЛЯ EXCEL
import pandas as pd
# import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets




class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.initUi()
        self.db = Sqlite()





    def initUi(self):
        #создать поле

        self.setMinimumWidth(930)
        self.setMinimumHeight(600)
        # self.setFixedSize(1000,900)
        self.setWindowTitle('ЗАПРОС РАЗРАБОТЧИКА СМЕТНОЙ ДОКУМЕНТАЦИИ ОПЕРАТОРУ ГОССТРОЙПОРТАЛА')

        # кнопка с пустым полем для того чтобы писать
        self.sth1 =QPushButton('ДОБАВИТЬ МАТЕРИАЛ В БАЗУ ДАННЫХ', self)
        self.sth1.clicked.connect(self.func1)
        self.sth1.setGeometry(100,360, 500,80 )
        self.sth1.setStyleSheet("background-image: url(7.jpg);")
        self.sth2=QPushButton('БАЗA ДАННЫХ  МАТЕРИАЛОВ',self)
        self.sth2.setGeometry(100,100,500,80)
        self.sth2.setStyleSheet("background-image: url(7.jpg);")
        self.sth2.clicked.connect(self.func3)
        self.sth3 = QPushButton('СФОРМИРОВАТЬ ЗАПРОС НА "ГОССТРОЙПОРТАЛ"', self)
        self.sth3.clicked.connect(self.func4)
        self.sth3.setGeometry(100, 230, 500, 80)
        self.sth3.setStyleSheet("background-image: url(7.jpg);")
        self.setStyleSheet("background-image: url(1000.jpg);")

        # self.sth5 = QPushButton('Цена за единицу измерения', self)
        # self.sth5.setGeometry(50, 500, 200, 75)
        # self.sth5.setStyleSheet('background-color:pink')
        # self.sth6 = QPushButton('Вид работ (ПТМ)', self)
        # self.sth6.setGeometry(50, 600, 200, 75)
        # self.sth6.setStyleSheet('background-color:white')
        # self.sth7 = QPushButton('Основные характеристики матерала по проекту', self)
        # self.sth7.setGeometry(50, 700, 500, 75)
        # self.sth7.setStyleSheet("background-сolor:pink;")
        # self.rb1 = QRadioButton('без НДС', self)
        # self.rb1.move(500,50)
        # self.rb2 = QRadioButton('с НДС', self)
        # self.rb2.move(600, 50)


        # self.gl=QLabel('форма создана по инструкции №39',self)
        # self.style='border: 1px solid; background-color:pink'
        # self.gl.setGeometry(700,50,230,80)
        # self.gl.setStyleSheet(self.style)
        # self.gl1 = QLabel(self)
        # self.gl1.setPixmap(QPixmap("999.jpg"))
        # self.gl1.setGeometry(650, 150, 700, 230)
        # self.gl2 = QLabel(self)
        # self.gl2.setPixmap(QPixmap("555.png"))
        # self.gl2.setGeometry(660,280,300,700)

      #  self.ins = QPushButton('ВСТАВИТЬ', self)
      #  self.ins.clicked.connect(self.insert)
      #  self.ins.setGeometry(50, 100, 100, 100)
       # self.ins.setStyleSheet('background-color:red')
        #self.ins1 = QPushButton('ОБНОВИТЬ', self)
       # self.ins1.clicked.connect(self.update())
       # self.ins1.setGeometry(50, 100, 100, 100)
       # self.ins1.setStyleSheet('background-color:red')
       # self.ins2 = QPushButton('УДАЛИТЬ', self)
      #  self.ins2.clicked.connect(self.delete)
       # self.ins2.setGeometry(50, 100, 100, 100)
       # self.ins2.setStyleSheet('background-color:red')
       # self.ins3 = QPushButton('УДАЛИТЬ', self)
      #  self.ins3.clicked.connect(self.select())
      #  self.ins3.setGeometry(50, 100, 100, 100)
     #   self.ins3.setStyleSheet('background-color:red')


      # self.pushButton.clicked.connect(self.insert)
      #self.pushButton_2.clicked.connect(self.update)
      # self.pushButton_3.clicked.connect(self.delete)





    def update(self):
        self.id = QLineEdit(self)
        self.Normativ = QLineEdit(self)
        self.Kod_KKM = QLineEdit(self)
        self.Naimenovanie_materiala = QLineEdit(self)
        self.PRICE = QLineEdit(self)
        self.db.update(self.id, self.Normativ, self.Kod_KKM, self.Naimenovanie_materiala, self.PRICE)
        self.select()
    # def update(self):
    #     self.id = self.lineEdit.text()
    #     self.login = self.lineEdit_2.text()
    #     self.password = self.lineEdit_3.text()
    #     self.db.update(self.id, self.login, self.password)
    #     self.select()

    # def delete1(self):
    #     self.id = self.pole201.text()
    #     self.db.delete(self.id)
    #     self.db.select()

    def func1(self):
        print('привет медведь')
        self.w1 = Window1()
        self.w1.button.clicked.connect(self.func2)
        self.w1.show()

    def func2(self):
        print('привет заяц')
        self.w2 = Window2()
        self.w2.show()
    def func3(self):
        print('ПРИВЕТ КОТЯРА')
        self.w4 = Window3()
        self.w4.show()

    def func4(self):
        print('ПРИВЕТ КОТЯРА')
        self.w4 = Window4()
        self.w4.show()




    #def select(self):
     #   self.data = self.db.select()
    #    self.tableWidget.setRowCount(len(self.data))
     #   self.tableWidget.setColumnCount(len(self.data[0]))

        # добавляет данные
       # for row, row_item in enumerate(self.data):
            #insert(self, Normativ, Kod_KKM,Naimenovanie_materiala,PRICE,Naimenovanie_smeta,Edinica_izmer,PTM,Haracteristica_mat,Naimenovanie_stroika):
        #    print(row,row_item)
        #    for column, value in enumerate(row_item):
         #       self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))

    # self.Naimenovanie_smeta,self.Edinica_izmer,self.PTM,self.Haracteristica_mat,self.Naimenovanie_stroik)


    # def insert(self):
    #     self.login = self.lineEdit_2.text()
    #     self.password = self.lineEdit_3.text()
    #     self.db.insert(self.login, self.password)
    #     self.select()




class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.db = Sqlite()
        self.initUi1()
        self.sth20.clicked.connect(self.insert)
        self.sth20.clicked.connect(self.close)



    def initUi1(self):
        self.setWindowTitle('ВВЕДИТЕ НОВЫЕ ДАННЫЕ В БАЗУ')
        self.setMinimumWidth(1700)
        self.setMinimumHeight(960)
        self.gl100 = QLabel('НОРМАТИВ РАСХОДА РЕСУРСОВ',self)
        self.gl100.setStyleSheet('border:3px solid pink')
        self.gl100.setGeometry(30,20, 200, 30)
        self.pole1=QLineEdit(self)
        self.pole1.setGeometry(30, 60,200, 70)
        self.gl101 = QLabel('            КОД ККМ', self)
        self.gl101.setStyleSheet('border:3px solid pink')
        self.gl101.setGeometry(270, 20, 200, 30)
        self.pole2 = QLineEdit(self)
        self.pole2.setGeometry(270, 60, 200, 70)
        self.pole3 = QLineEdit(self)
        self.pole3.setGeometry(510, 60, 200, 70)
        self.gl102 = QLabel('НАИМЕНОВАНИЕ МАТЕРИЛА КОД ККМ', self)
        self.gl102.setStyleSheet('border:3px solid pink')
        self.gl102.setGeometry(510, 20, 200, 30)
        #
        self.pole4 = QLineEdit(self)
        self.pole4.setGeometry(180, 210, 200, 70)
        self.gl103 = QLabel('  ЦЕНУ ЗА ЕД.ИЗМЕРЕНИЯ', self)
        self.gl103.setStyleSheet('border:3px solid pink')
        self.gl103.setGeometry(180,170, 200, 30)
        #
        self.pole5 = QLabel(self)
        self.pole5.setPixmap(QPixmap("321.jpg"))
        self.pole5.setGeometry(110, 440,400,400)
        self.sth20 = QPushButton('ОК', self)
        self.sth20.setGeometry(180, 325, 200, 75)
        self.sth20.setStyleSheet("background-image: url(7.jpg);")
        self.pole6 = QLabel(self)
        self.pole6.setPixmap(QPixmap("img_1.png"))
        self.pole6.setGeometry(520,153, 875, 776)
        # НОВОЕ
        self.pole110 = QLineEdit(self)
        self.pole110.setGeometry(750, 60, 200, 70)
        self.gl110 = QLabel(' НАИМЕНОВАНИЕ МАТЕРИАЛА '
                            'ДЛЯ ВКЛЮЧЕНИЯ В СМЕТНУЮ СТОИМОСТЬ', self)
        self.gl110.setStyleSheet('border:3px solid pink')
        self.gl110.setGeometry(750, 20, 200, 30)
        self.pole111 = QLineEdit(self)
        self.pole111.setGeometry(990, 60, 200, 70)
        self.gl111 = QLabel('   ЕДИНИЦА ИЗМЕРЕНИЯ', self)
        self.gl111.setStyleSheet('border:3px solid pink')
        self.gl111.setGeometry(990, 20, 200, 30)
        self.pole111 = QLineEdit(self)
        self.pole111.setGeometry(1230, 60, 200, 70)
        self.gl111 = QLabel('   ВИД РАБОТЫ (ПТМ)', self)
        self.gl111.setStyleSheet('border:3px solid pink')
        self.gl111.setGeometry(1230, 20, 200, 30)
        self.pole112 = QLineEdit(self)
        self.pole112.setGeometry(1470, 60, 200, 400)
        self.gl112 = QLabel('ОСНОВНЫЕ ХАРАКТЕРИСТИКИ', self)
        self.gl112.setStyleSheet('border:3px solid pink')
        self.gl112.setGeometry(1470, 20, 200, 30)
        self.pole113 = QLineEdit(self)
        self.pole113.setGeometry(1470, 540, 200,390)
        self.gl113 = QLabel('ПРИМЕЧАНИЕ', self)
        self.gl113.setStyleSheet('border:3px solid pink')
        self.gl113.setGeometry(1470, 490, 200, 30)

    def insert(self):
        self.Normativ = self.pole1.text()
        self.Kod_KKM = self.pole2.text()
        self.Naimenovanie_materiala = self.pole3.text()
        self.PRICE = self.pole4.text()
        self.db.insert( self.Normativ, self.Kod_KKM, self.Naimenovanie_materiala, self.PRICE)
        self.db.select()


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.db = Sqlite()
        self.initUi2()


    def initUi2(self):
        self.setWindowTitle('Выберите  Сборник')
        self.setMinimumWidth(600)
        self.setMinimumHeight(500)
        self.button = QPushButton(self)
        self.button.setStyleSheet("background-image: url(7.jpg);")
        self.button.setText('ВВЕДИТЕ ДАННЫЕ')
        self.button.setGeometry(400,200, 190, 100)
        self.button.colorCount()
        self.button.show()
        text1 = "Cборник № 1- Земляные работы"
        text=QLabel(text1,self)
        text.setGeometry(5,10,300,80)
        text6 = "Cборник № 6- Бетонные монолитные конструкции"
        text = QLabel(text6,self)
        text.setGeometry(5, 40, 300, 80)
        text7 = "Cборник № 7- Сборные железобетонные конструкции"
        text = QLabel(text7, self)
        text.setGeometry(5, 70, 300, 80)
        text9 = "Cборник № 9- Металлические конструкции"
        text = QLabel(text9, self)
        text.setGeometry(5,100, 300, 80)
        text10 = "Cборник № 10- Деревянные конструкции"
        text = QLabel(text10, self)
        text.setGeometry(5, 130, 300, 80)
        text11 = "Cборник № 11- Полы"
        text = QLabel(text11, self)
        text.setGeometry(5, 160, 300, 80)
        text12 = "Cборник № 12- Кровля"
        text = QLabel(text12, self)
        text.setGeometry(5, 190, 300, 80)
        text13 = "Cборник № 13- Антикорозионная защита"
        text = QLabel(text13, self)
        text.setGeometry(5, 220, 300, 80)
        text15 = "Cборник № 15- Отделочные работы"
        text = QLabel(text15, self)
        text.setGeometry(5, 250, 300, 80)
        text16 = "Cборник № 16- Сантехнические работы"
        text = QLabel(text16, self)
        text.setGeometry(5, 280, 300, 80)
        text26 = "Cборник № 26- Теплоизоляционные работы"
        text = QLabel(text26, self)
        text.setGeometry(5, 310, 300, 80)
        text27 = "Ц8 * Cборник № 8- Электромонтажные работы"
        text = QLabel(text27, self)
        text.setGeometry(5, 340, 300, 80)
        self.pole2 = QLabel(self)
        self.pole2.setPixmap(QPixmap("777.jpg"))
        self.pole2.setGeometry(400,300, 200, 200)
        self.pole3 = QLabel(self)
        self.pole3.setPixmap(QPixmap("333.jpg"))
        self.pole3.setGeometry(400,0, 200, 200)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '!!!', 'Хочешь выйти?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Window3(Main):

    def __init__(self):
        super(Window3, self).__init__()
        self.initUi3()
        self.select()
        self.sth300.clicked.connect(self.delete)
        # self.sth302.clicked.connect(self.open_file)
        self.sth303.clicked.connect(self.exportExcel)
        self.edit.returnPressed.connect(self.on_find)
        self.sth304.clicked.connect(self.update)
        # self.edit1.returnPressed.connect(self.save)
        # self.sth304.clicked.connect(self.select)
        #self.sth300.clicked.connect(self.close)

    def initUi3(self):
        self.setWindowTitle('ПРОСМОРТ БАЗЫ ДАННЫХ')
        self.setMinimumWidth(1910)
        self.setMinimumHeight(990)
        self.setStyleSheet("background-image: url(44444.jpg);")
        self.gl201 = QLabel('       УДАЛИТЬ НОМЕР', self)
        self.gl201.setStyleSheet('border:3px solid pink')
        self.gl201.setGeometry(1700, 20, 175, 70)
        self.pole201 = QLineEdit(self)
        self.pole201.setGeometry(1745, 112, 100, 70)
        self.pole201.setStyleSheet("background-image: url(44444-4.jpg);")
        self.sth300 = QPushButton('УДАЛИТЬ', self)
        self.sth300.setGeometry(1700, 220, 180, 70)
        self.sth300.setStyleSheet("background-image: url(7.jpg);")
        self.pig = QTableWidget(self)
        self.pig.setGeometry(5, 5, 1670, 700)
        # self.sth302 = QPushButton('ОТКРЫТЬ ФАЙЛ EXCEL', self)
        # self.sth302.setGeometry(1010, 325, 180, 100)
        # self.sth302.setStyleSheet("background-image: url(7.jpg);")

        self.sth303 = QPushButton('СОХРАНИТЬ ФАЙЛ В ЕХСЕЛ', self)
        self.sth303.setGeometry(1700, 530, 180, 70)
        self.sth303.setStyleSheet("background-image: url(7.jpg);")
        self.edit = QLineEdit(self)
        self.edit.setGeometry(1700, 430, 175, 70)
        self.edit.setStyleSheet("background-image: url(44444-4.jpg);")
        self.gl202 = QLabel('   ПОИСК ПО БАЗЕ', self)
        self.gl202.setStyleSheet('border:3px solid pink')
        self.gl202.setGeometry(1700,330, 175, 70)
        self.sth304 = QPushButton('ОБНОВИТЬ БАЗУ ДАННЫХ', self)
        self.sth304.setGeometry(1700, 760, 180, 100)
        self.sth304.setStyleSheet("background-image: url(7.jpg);")

        # --------------------------------------------НИЗЗ!!!!!



        self.gl100 = QLabel('№ПП ИЗ БАЗЫ                        (ДЛЯ ОБНОВЛЕНИЯ)', self)
        self.gl100.setStyleSheet('border:3px solid pink')
        self.gl100.setGeometry(30, 710, 200, 40)
        self.gl100.setWordWrap(True)
        self.pole1 = QLineEdit(self)
        self.pole1.setGeometry(30, 760, 200, 70)
        #######
        self.gl101 = QLabel('НОРМАТИВ РАСХОДА РЕСУРСОВ ', self)
        self.gl101.setStyleSheet('border:3px solid pink')
        self.gl101.setGeometry(270, 710, 200, 40)
        self.gl101.setWordWrap(True)
        self.pole2 = QLineEdit(self)
        self.pole2.setGeometry(270, 760, 200, 70)
        ##########
        self.gl102 = QLabel('КОД ККМ', self)
        self.gl102.setStyleSheet('border:3px solid pink')
        self.gl102.setGeometry(510,710, 200, 40)
        self.pole3 = QLineEdit(self)
        self.pole3.setGeometry(510, 760, 200, 70)

        # НОВОЕ
        self.gl110 = QLabel('НАИМЕНОВАНИЕ МАТЕРИЛА           (ПО КОДУ ККМ) ', self)
        self.gl110.setWordWrap(True)
        self.gl110.setStyleSheet('border:3px solid pink')
        self.gl110.setGeometry(990,710, 200, 40)
        self.pole110 = QLineEdit(self)
        self.pole110.setGeometry(990, 760, 200, 70)
        #########
        self.gl111 = QLabel('НАИМЕНОВАНИЕ МАТЕРИАЛА '
                            'ДЛЯ ВКЛЮЧЕНИЯ В СМЕТНУЮ СТОИМОСТЬ', self)
        ####перенос текста
        self.gl111.setWordWrap(True)
        self.gl111.setStyleSheet('border:3px solid pink')
        self.gl111.setGeometry(1230, 710, 200, 50)
        self.pole111 = QLineEdit(self)
        self.pole111.setGeometry(1230, 760, 200, 70)
        ########
        self.gl1111 = QLabel('ЕДИНИЦА ИЗМЕРЕНИЯ', self)
        self.gl1111.setStyleSheet('border:3px solid pink')
        self.gl1111.setGeometry(1470, 710, 200, 40)
        self.pole1111 = QLineEdit(self)
        self.pole1111.setGeometry(1470, 760, 200, 70)
        ########
        self.gl112 = QLabel('ВИД РАБОТЫ (ПТМ)', self)
        self.gl112.setStyleSheet('border:3px solid pink')
        self.gl112.setGeometry(30,840,200, 40)
        self.pole112 = QLineEdit(self)
        self.pole112.setGeometry(30,890, 200, 70)
        #######
        self.gl113 = QLabel('            ОСНОВНЫЕ ХАРАКТЕРИСТИКИ       ', self)
        self.gl113.setWordWrap(True)
        self.gl113.setStyleSheet('border:3px solid pink')
        self.gl113.setGeometry(270,840,440, 40)
        self.pole113 = QLineEdit(self)
        self.pole113.setGeometry(270,890,440, 70)
        # self.edit1 = QLineEdit(self)
        # self.edit1.setGeometry(1010,640, 175, 70)
        # self.edit1.setStyleSheet("background-image: url(44444-4.jpg);")
        ######
        self.gl103 = QLabel(' ПРИМЕЧАНИЕ ', self)
        self.gl103.setStyleSheet('border:3px solid pink')
        self.gl103.setGeometry(990, 840,440, 40)
        self.pole4 = QLineEdit(self)
        self.pole4.setGeometry(990, 890, 440, 70)
        #######
        self.gl103 = QLabel(' ЦЕНУ ЗА ЕД.ИЗМЕРЕНИЯ', self)
        self.gl103.setStyleSheet('border:3px solid pink')
        self.gl103.setGeometry(1470, 840, 200,40)
        self.pole4 = QLineEdit(self)
        self.pole4.setGeometry(1470, 890, 200, 70)
        ######
        self.pole2 = QLabel(self)
        self.pole2.setPixmap(QPixmap("999.jpg"))
        self.pole2.setGeometry(720,710,260,270)
        ######
        # self.pole2 = QLabel(self)
        # self.pole2.setPixmap(QPixmap("2222.jpg"))
        # self.pole2.setGeometry(1680, 710, 230, 270)


        # self.pole401 = QLineEdit(self)
        # self.pole401.setGeometry(1015, 600, 175, 70)
        # self.sth304 = QPushButton('ВЫБЕРИТЕ НОМЕР ПОЗИЦИИ', self)
        # self.sth304.setGeometry(1010, 700, 180, 100)
        # self.sth304.setStyleSheet("background-image: url(888.jpg);")

    # def save (self):
    #     __k__ = self.edit1.text().lower()
    #     print(k)



    def select(self):
        self.data = self.db.select()

        if len(self.data)!= 0:
            self.pig.setRowCount(len(self.data))
            self.pig.setColumnCount(len(self.data[0]))
            self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
            for row, row_item in enumerate(self.data):
                for column, value in enumerate(row_item):
                    self.pig.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))
                    self.pig.setColumnWidth(0, 110)
                    self.pig.setColumnWidth(1, 110)
                    self.pig.setColumnWidth(2, 200)
                    self.pig.setColumnWidth(3, 250)
                    self.pig.setColumnWidth(4, 200)

        else:
            print('дата 0')
            self.pig.setColumnCount(5)
            self.pig.setRowCount(100)
            self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
            self.pig.setColumnWidth(0, 110)
            self.pig.setColumnWidth(1, 110)
            self.pig.setColumnWidth(2, 200)
            self.pig.setColumnWidth(3, 250)
            self.pig.setColumnWidth(4, 200)
            self.pig.setItem(0, 0, QtWidgets.QTableWidgetItem(str('ДАННЫХ')))
            self.pig.setItem(0, 1, QtWidgets.QTableWidgetItem(str('НЕТ  !!!')))
            self.pig.setItem(0, 2, QtWidgets.QTableWidgetItem(str('                    ')))
            self.pig.setItem(0, 3, QtWidgets.QTableWidgetItem(str('ВВЕДИТЕ')))
            self.pig.setItem(0, 4, QtWidgets.QTableWidgetItem(str('ДАННЫЕ  !!!')))
            self.sth300.clicked.connect(self.close)

    # def select2(self):
    #     self.data = self.db.select2(self.id)
    #     self.id=self.pole401.text()
    #
    #     if len(self.data)!= 0:
    #         self.pig.setRowCount(len(self.data))
    #         self.pig.setColumnCount(len(self.data[0]))
    #         self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
    #         for row, row_item in enumerate(self.data):
    #             for column, value in enumerate(row_item):
    #                 self.pig.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))
    #                 self.pig.setColumnWidth(0, 110)
    #                 self.pig.setColumnWidth(1, 110)
    #                 self.pig.setColumnWidth(2, 200)
    #                 self.pig.setColumnWidth(3, 250)
    #                 self.pig.setColumnWidth(4, 200)
    #
    #     else:
    #         print('дата 0')
    #         self.pig.setColumnCount(5)
    #         self.pig.setRowCount(100)
    #         self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
    #         self.pig.setColumnWidth(0, 110)
    #         self.pig.setColumnWidth(1, 110)
    #         self.pig.setColumnWidth(2, 200)
    #         self.pig.setColumnWidth(3, 250)
    #         self.pig.setColumnWidth(4, 200)
    #         self.pig.setItem(0, 0, QtWidgets.QTableWidgetItem(str('ДАННЫХ')))
    #         self.pig.setItem(0, 1, QtWidgets.QTableWidgetItem(str('НЕТ  !!!')))
    #         self.pig.setItem(0, 2, QtWidgets.QTableWidgetItem(str('                    ')))
    #         self.pig.setItem(0, 3, QtWidgets.QTableWidgetItem(str('ВВЕДИТЕ')))
    #         self.pig.setItem(0, 4, QtWidgets.QTableWidgetItem(str('ДАННЫЕ  !!!')))
    #         self.sth300.clicked.connect(self.close)

    def update(self):
        self.id =self.pole1.text()
        self.Normativ = self.pole2.text()
        self.Kod_KKM = self.pole3.text()
        self.Naimenovanie_materiala = self.pole110.text()
        self.PRICE = self.pole4.text()
        self.db.update(self.id, self.Normativ, self.Kod_KKM, self.Naimenovanie_materiala, self.PRICE)
        self.select()
    def delete(self):
        self.id=self.pole201.text()
        self.db.delete(self.id)
        self.select()

    # def open_file(self):
    #     self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', '.',
    #                                                               "Файлы Exсel (*.xlsx)")
    #     print(f'fname = {self.fname}')

    def exportExcel(self):
        rows = self.pig.rowCount()
        if not rows:
            msg = QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
            return

        path, _ = QFileDialog.getSaveFileName(self, 'Save Excel', '.', 'Excel(*.xlsx)')
        if not path:
            msg = QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
            return

        columnHeaders = []
        # создать список заголовков столбцов
        for j in range(self.pig.model().columnCount()):
            columnHeaders.append(self.pig.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # создать набор записей объекта dataframe
        for row in range(self.pig.rowCount()):
            for col in range(self.pig.columnCount()):
                df.at[row, columnHeaders[col]] = self.pig.item(row, col).text()

        df.to_excel(path, index=False)
        msg = QMessageBox.information(self, 'Ok', 'Файл сохранен!')

    def on_find(self):
        s = self.edit.text().lower()
        rows =self.pig.rowCount()
        cols =self.pig.columnCount()
        first = None
        for i in range(rows):
            for j in range(cols):
                txt = self.pig.item(i, j).text()
                if s in txt.lower():
                    self.pig.item(i, j).setBackground(QtGui.QColor(0,0,0,0))
                    if not first: first = self.pig.item(i, j)
                # elif s in txt:
                #     self.pig.item(i, j).setBackground(QtGui.QColor(0,0,0,0))
                #     if not first: first = self.pig.item(i, j)
                # if s in txt.upper():
                #     self.pig.item(i, j).setBackground(QtGui.QColor(0, 0, 0, 0))
                #     if not first: first = self.pig.item(i, j)
                else:
                    self.pig.item(i, j).setBackground(QtGui.QColor(100,100,0,100))
        self.pig.setCurrentItem(first)




class Window4(Main):

    def __init__(self):
        super(Window4, self).__init__()
        self.initUi4()
        # self.sth300.clicked.connect(self.delete)
        # self.sth302.clicked.connect(self.open_file)
        self.sth303.clicked.connect(self.exportExcel)
        self.sth304.clicked.connect(self.select2)
        # self.sth304.clicked.connect(self.close)


    def initUi4(self):
        self.setWindowTitle('ПОЛЕ ДЛЯ ФОРМИРОВАНИЯ ЗАПРОСА')
        self.setMinimumWidth(1215)
        self.setMinimumHeight(965)
        self.move(300,20)
        self.setStyleSheet("background-image: url(11.jpg);")
        self.gl201 = QLabel('  ВВЕДИТЕ №П/П ИЗ БАЗЫ', self)
        self.gl201.setStyleSheet('border:3px solid pink')
        self.gl201.setGeometry(1020, 130, 180, 50)
        # self.gl202 = QLabel(__k__,self)
        # self.gl202.setStyleSheet('border:3px solid pink')
        # self.gl202.setGeometry(1020, 760, 180, 50)
        # # self.pole201 = QLineEdit(self)
        # self.pole201.setGeometry(1050, 112, 100, 70)
        # self.sth300 = QPushButton('УДАЛИТЬ', self)
        # self.sth300.setGeometry(1010, 200, 180, 100)
        # self.sth300.setStyleSheet("background-image: url(888.jpg);")
        self.pig = QTableWidget(self)
        self.pig.setGeometry(3, 3, 1000, 965)
        # self.sth302 = QPushButton('ОТКРЫТЬ ФАЙЛ EXCEL', self)
        # self.sth302.setGeometry(1010, 325, 180, 100)
        # self.sth302.setStyleSheet("background-image: url(888.jpg);")
        self.sth303 = QPushButton('СОХРАНИТЬ ФАЙЛ В ЕХСЕЛ', self)
        self.sth303.setGeometry(1020, 650, 180, 85)
        self.pole5 = QLabel(self)
        self.pole5.setPixmap(QPixmap("19.jpg"))
        self.pole5.setGeometry(1020, 740, 250, 250)
        self.sth303.setStyleSheet("background-image: url(7.jpg);")
        self.pole401 = QLineEdit(self)
        self.pole401.setGeometry(1020, 200, 70, 50)
        self.pole401.setStyleSheet("background-image: url(1000.jpg);")
        self.pole402 = QLineEdit(self)
        self.pole402.setGeometry(1020, 270, 70,50)
        self.pole402.setStyleSheet("background-image: url(1000.jpg);")
        self.pole403 = QLineEdit(self)
        self.pole403.setGeometry(1020, 340, 70, 50)
        self.pole403.setStyleSheet("background-image: url(1000.jpg);")
        self.sth304 = QPushButton('ПОКАЗАТЬ ДАННЫЕ', self)
        self.sth304.setGeometry(1020,20, 180, 85)
        self.sth304.setStyleSheet("background-image: url(7.jpg);")
        self.pole404 = QLineEdit(self)
        self.pole404.setGeometry(1020, 410, 70, 50)
        self.pole404.setStyleSheet("background-image: url(1000.jpg);")
        self.pole405 = QLineEdit(self)
        self.pole405.setGeometry(1020, 490, 70, 50)
        self.pole405.setStyleSheet("background-image: url(1000.jpg);")
        self.pole406 = QLineEdit(self)
        self.pole406.setGeometry(1120, 200, 70, 50)
        self.pole406.setStyleSheet("background-image: url(1000.jpg);")
        self.pole407 = QLineEdit(self)
        self.pole407.setGeometry(1120, 270, 70, 50)
        self.pole407.setStyleSheet("background-image: url(1000.jpg);")
        self.pole408 = QLineEdit(self)
        self.pole408.setGeometry(1120, 340, 70, 50)
        self.pole408.setStyleSheet("background-image: url(1000.jpg);")
        self.pole409 = QLineEdit(self)
        self.pole409.setGeometry(1120, 410, 70, 50)
        self.pole409.setStyleSheet("background-image: url(1000.jpg);")
        self.pole410 = QLineEdit(self)
        self.pole410.setGeometry(1120, 490, 70, 50)
        self.pole410.setStyleSheet("background-image: url(1000.jpg);")
        self.pole411 = QLineEdit(self)
        self.pole411.setGeometry(1020, 560, 70, 50)
        self.pole411.setStyleSheet("background-image: url(1000.jpg);")
        self.pole412 = QLineEdit(self)
        self.pole412.setGeometry(1120, 560, 70, 50)
        self.pole412.setStyleSheet("background-image: url(1000.jpg);")

    # def sav(self):
    #     super.__class__.
    # #     k=self.edit1.text().lower()
    #     print(k)
    # def select(self):
    #     self.data = self.db.select()
    #
    #     if len(self.data)!= 0:
    #         self.pig.setRowCount(len(self.data))
    #         self.pig.setColumnCount(len(self.data[0]))
    #         self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
    #         for row, row_item in enumerate(self.data):
    #             for column, value in enumerate(row_item):
    #                 self.pig.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))
    #                 self.pig.setColumnWidth(0, 110)
    #                 self.pig.setColumnWidth(1, 110)
    #                 self.pig.setColumnWidth(2, 200)
    #                 self.pig.setColumnWidth(3, 250)
    #                 self.pig.setColumnWidth(4, 200)
    #
    #     else:
    #         print('дата 0')
    #         self.pig.setColumnCount(5)
    #         self.pig.setRowCount(100)
    #         self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
    #         self.pig.setColumnWidth(0, 110)
    #         self.pig.setColumnWidth(1, 110)
    #         self.pig.setColumnWidth(2, 200)
    #         self.pig.setColumnWidth(3, 250)
    #         self.pig.setColumnWidth(4, 200)
    #         self.pig.setItem(0, 0, QtWidgets.QTableWidgetItem(str('ДАННЫХ')))
    #         self.pig.setItem(0, 1, QtWidgets.QTableWidgetItem(str('НЕТ  !!!')))
    #         self.pig.setItem(0, 2, QtWidgets.QTableWidgetItem(str('                    ')))
    #         self.pig.setItem(0, 3, QtWidgets.QTableWidgetItem(str('ВВЕДИТЕ')))
    #         self.pig.setItem(0, 4, QtWidgets.QTableWidgetItem(str('ДАННЫЕ  !!!')))
    #         self.sth300.clicked.connect(self.close)

    def select2(self):
        self.id = self.pole401.text()
        self.id2 = self.pole402.text()
        self.id3 = self.pole403.text()
        self.id4 = self.pole404.text()
        self.id5 = self.pole405.text()
        self.id6 = self.pole406.text()
        self.id7 = self.pole407.text()
        self.id8 = self.pole408.text()
        self.id9 = self.pole409.text()
        self.id10 = self.pole410.text()
        self.id11 = self.pole411.text()
        self.id12 = self.pole412.text()
        self.data = self.db.select2(self.id,self.id2, self.id3,self.id4,self.id5, self.id6,self.id7,self.id8, self.id9,self.id10,self.id11, self.id12)


        if len(self.data)!= 0:
            self.pig.setRowCount(len(self.data))
            self.pig.setColumnCount(len(self.data[0]))
            self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
            for row, row_item in enumerate(self.data):
                for column, value in enumerate(row_item):
                    self.pig.setItem(row, column, QtWidgets.QTableWidgetItem(str(value)))
                    self.pig.setColumnWidth(0, 110)
                    self.pig.setColumnWidth(1, 110)
                    self.pig.setColumnWidth(2, 200)
                    self.pig.setColumnWidth(3, 250)
                    self.pig.setColumnWidth(4, 200)

        else:
            print('дата 0')
            self.pig.setColumnCount(5)
            self.pig.setRowCount(100)
            self.pig.setHorizontalHeaderLabels(["№п/п", 'РАСЦЕНКА', "КОД ККМ", "НАИМЕНОВАНИЕ МАТЕРИАЛА", "ЦЕНА ЗА ЕД.ИЗМ."])
            self.pig.setColumnWidth(0, 110)
            self.pig.setColumnWidth(1, 110)
            self.pig.setColumnWidth(2, 200)
            self.pig.setColumnWidth(3, 250)
            self.pig.setColumnWidth(4, 200)
            self.pig.setItem(0, 0, QtWidgets.QTableWidgetItem(str('ДАННЫХ')))
            self.pig.setItem(0, 1, QtWidgets.QTableWidgetItem(str('НЕТ  !!!')))
            self.pig.setItem(0, 2, QtWidgets.QTableWidgetItem(str('                    ')))
            self.pig.setItem(0, 3, QtWidgets.QTableWidgetItem(str('ВВЕДИТЕ')))
            self.pig.setItem(0, 4, QtWidgets.QTableWidgetItem(str('ДАННЫЕ  !!!')))



    def delete(self):
        self.id=self.pole201.text()
        self.db.delete(self.id)
        self.select()

    # def open_file(self):
    #     self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', '.',
    #                                                               "Файлы Exсel (*.xlsx)")
    #     print(f'fname = {self.fname}')

    def exportExcel(self):
        rows = self.pig.rowCount()
        if not rows:
            msg = QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
            return

        path, _ = QFileDialog.getSaveFileName(self, 'Save Excel', '.', 'Excel(*.xlsx)')
        if not path:
            msg = QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
            return

        columnHeaders = []
        # создать список заголовков столбцов
        for j in range(self.pig.model().columnCount()):
            columnHeaders.append(self.pig.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # создать набор записей объекта dataframe
        for row in range(self.pig.rowCount()):
            for col in range(self.pig.columnCount()):
                df.at[row, columnHeaders[col]] = self.pig.item(row, col).text()

        df.to_excel(path, index=False)
        msg = QMessageBox.information(self, 'Ok', 'Файл сохранен!')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    ex=Main()
    ex.show()
    sys.exit(app.exec_())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
