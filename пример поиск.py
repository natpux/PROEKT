from PyQt5.Qt import *


def on_find():
    s = edit.text()
    rows = t.rowCount()
    cols = t.columnCount()
    first = None
    for i in range(rows):
        for j in range(cols):
            txt = t.item(i, j).text()
            if txt.contains(s):
                t.item(i, j).setTextColor(QColor(0, 0, 0))
                if not first: first = t.item(i, j)
            else:
                t.item(i, j).setTextColor(QColor(222, 222, 222))
    t.setCurrentItem(first)  # я о чем спрашивал?


app = QApplication([])
w = QWidget()
t = QTableWidget(w)
t.setRowCount(3)
t.setColumnCount(4)
for i in range(3):
    for j in range(4):
        s = 'blabla' + str(i) + str(j)
        item = QTableWidgetItem()
        item.setText(s)
        t.setItem(i, j, item)
t.setSortingEnabled(True)
edit = QLineEdit(w)
edit.returnPressed.connect(on_find)
lbl = QLabel(u'Filter:')
grid = QGridLayout(w)
grid.setMargin(0)
grid.addWidget(t, 0, 0, 1, 2)
grid.addWidget(lbl, 1, 0)
grid.addWidget(edit, 1, 1)
w.resize(500, 300)
w.move(0, 0)
w.show()
app.exec_()