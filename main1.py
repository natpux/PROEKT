import sys
from PyQt5.QtWidgets import QApplication, QWidget

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Eample1 (QWidget):

    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('наташа')
        self.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Eample1()
    sys.exit(app.exec_())




