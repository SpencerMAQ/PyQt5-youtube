import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem

'''
Lesson 17 (2/4)
QTableWidget
Spreadsheet Project
'''

class MyTable(QTableWidget):

    def __init__(self, rows, columns):
        super(MyTable, self).__init__(rows, columns)

        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)

        self.show()

    def c_current(self):
        row = self.currentRow()      # current row of the table instance
        col = self.currentColumn()
        value = self.item(row, col)
        value = value.text()
        print('The current cell is ', row, ', ', col)
        print('In this cell we have: ', value)

class Sheet(QMainWindow):
    #form_widget = MyTable(10, 10)

    def __init__(self):
        super(Sheet, self).__init__()

        form_widget = MyTable(10,10)        # used self in the original tuts

        self.setCentralWidget(form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        form_widget.setHorizontalHeaderLabels(col_headers)

        number = QTableWidgetItem('10')       # special item for QTableWidget
        form_widget.setCurrentCell(1, 1)
        # if this line form_widget.setCurrentCell(1, 1) is not specified
        # no value will be passed to c_current

        form_widget.setItem(1, 1, number)
        # because val in this cell is changed, it calls c_current

        self.show()


app = QApplication([])
sheet = Sheet()
sys.exit(app.exec_())