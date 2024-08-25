import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QMainWindow)




class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI6()

    def initUI6(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)
        grid = QGridLayout(widget)
        self.setLayout(grid)


        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=',
                 '+']
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(1300,190)
        self.setWindowTitle('Calculator')



