
#     This is a sample Python script.
#
#     Press Shift+F10 to execute it or replace it with your code.
#     Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox, QDesktopWidget
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import QCoreApplication
#
#
# class Eхample(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         # шрифт
#         QToolTip.setFont(QFont('Santserif', 10))
#
#         bt = QPushButton('выход', self)
#         bt.setToolTip('Тише,Тина спит!')
#         bt.clicked.connect(QCoreApplication.instance().quit)
#         bt.resize(100, 100)
#         bt.move(150, 50)
#         bt1 = QPushButton('вход', self)
#         bt1.setToolTip('Тише,папа спит!')
#         bt1.clicked.connect(QCoreApplication.instance().quit)
#         bt1.resize(100, 100)
#         bt1.move(20, 50)
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('программка')
#         self.center()
#
#         self.show()
#
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, 'сообщение', 'выйти или нет?', QMessageBox.Yes | QMessageBox.No,
#                                      QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#
# # Press the green button in the gutter to run the script.
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Eхample()
#     sys.exit(app.exec_())
#
#
#
# #
# #
# #
# #
# #
#
#
#
