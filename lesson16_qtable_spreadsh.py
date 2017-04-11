import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow


'''
Lesson 16 (1/4)
QTableWidget
Spreadsheet Project
'''

class MyTable(QTableWidget):

    def __init__(self, rows, columns):
        super(MyTable, self).__init__(rows, columns)

        self.show()

class Sheet(QMainWindow):

    #form_widget = MyTable(10, 10)

    def __init__(self):
        super(Sheet, self).__init__()

        form_widget = MyTable(10,10)

        self.setCentralWidget(form_widget)
        self.show()


app = QApplication([])
sheet = Sheet()
sys.exit(app.exec_())