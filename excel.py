import sys
import pandas as pd
# import openpyxl
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_table(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1000, 684)
#         MainWindow.setMinimumSize(QtCore.QSize(1000, 684))
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(15, 342, 131, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
#         self.tableWidget.setGeometry(QtCore.QRect(170, 10, 811, 631))
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(15, 220, 131, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(15, 279, 131, 31))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(15, 400, 131, 31))
#         self.pushButton_4.setObjectName("pushButton_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
#         self.menubar.setObjectName("menubar")
#         self.menu = QtWidgets.QMenu(self.menubar)
#         self.menu.setObjectName("menu")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.action = QtWidgets.QAction(MainWindow)
#         self.action.setObjectName("action")
#         self.menu.addAction(self.action)
#         self.menubar.addAction(self.menu.menuAction())
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "обновить"))
#         self.pushButton_2.setText(_translate("MainWindow", "добавить"))
#         self.pushButton_3.setText(_translate("MainWindow", "удалить"))
#         self.pushButton_4.setText(_translate("MainWindow", "сохранить"))
#         self.menu.setTitle(_translate("MainWindow", "открыть"))
#         self.action.setText(_translate("MainWindow", "открыть файл"))
#
#
# class StartMenuMain(QMainWindow, Ui_table):
#     def __init__(self, parent=None):
#         super(StartMenuMain, self).__init__(parent)
#         self.setupUi(self)
#
#         self.fname = None
#         self.initUI()
#
#         self.pushButton_2.clicked.connect(self.addRow)
#         self.pushButton_3.clicked.connect(self.delRow)
#         self.pushButton_4.clicked.connect(self.exportToExcel)  # +++
#
#     def initUI(self):
#         self.pushButton.clicked.connect(self.update)
#         self.action.triggered.connect(self.open_file)
#
#     def update(self):
#         if not self.fname:
#             QMessageBox.critical(self, 'Ошибка!', "Выберите Exсel файл")
#             return
#         excel_file_path = self.fname
#         worksheet_name = 'Лист1'
#         self.loadExcelData(excel_file_path, worksheet_name)
#
#     def open_file(self):
#         self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', '.',
#                                                               "Файлы Exсel (*.xlsx)")
#         print(f'fname = {self.fname}')
#
#     def loadExcelData(self, excel_file_path, worksheet_name):
#         df = pd.read_excel(excel_file_path, worksheet_name)
#         if df.size == 0:
#             return
#
#         df.fillna('', inplace=True)
#         self.tableWidget.setRowCount(df.shape[0])
#         self.tableWidget.setColumnCount(df.shape[1])
#         self.tableWidget.setHorizontalHeaderLabels(df.columns)
#
#         # returns pandas array object
#         for row in df.iterrows():
#             values = row[1]
#             for col_index, value in enumerate(values):
#                 if isinstance(value, (float, int)):
#                     value = '{0:0,.0f}'.format(value)
#                 tableItem = QtWidgets.QTableWidgetItem(str(value))
#                 self.tableWidget.setItem(row[0], col_index, tableItem)
#         self.tableWidget.setColumnWidth(2, 300)
#
#     def addRow(self):
#         rowPosition = self.tableWidget.rowCount()
#         if not rowPosition:
#             msg = QMessageBox.information(self, 'Внимание', 'Выберите Exсel файл для добавления строки.')
#             return
#         self.tableWidget.insertRow(rowPosition)
#
#     def delRow(self):
#         row = self.tableWidget.currentRow()
#         if row == -1:
#             msg = QMessageBox.information(self, 'Внимание', 'Выберите строку для удаления')
#             return
#         self.tableWidget.removeRow(row)
#
#     # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#     def exportToExcel(self):
#         rows = self.tableWidget.rowCount()
#         if not rows:
#             msg = QMessageBox.information(self, 'Внимание', 'Нечего сохранять.')
#             return
#
#         path, _ = QFileDialog.getSaveFileName(self, 'Save Excel', '.', 'Excel(*.xlsx)')
#         if not path:
#             msg = QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
#             return
#
#         columnHeaders = []
#         # создать список заголовков столбцов
#         for j in range(self.tableWidget.model().columnCount()):
#             columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
#
#         df = pd.DataFrame(columns=columnHeaders)
#
#         # создать набор записей объекта dataframe
#         for row in range(self.tableWidget.rowCount()):
#             for col in range(self.tableWidget.columnCount()):
#                 df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()
#
#         df.to_excel(path, index=False)
#         msg = QMessageBox.information(self, 'Ok', 'Excel file exported.')
#     # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     startmenu_window = StartMenuMain()
#     windows = QStackedWidget()
#
#     windows.addWidget(startmenu_window)
#     windows.setWindowTitle("")
#     windows.show()
#     sys.exit(app.exec_())