import sys
import csv
import os
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, qApp, QAction

'''
Lesson 19 (4/4)
Write csv Spreadsheet
menu bar copied from notepad program (14 or 15?)
'''

class MyTable(QTableWidget):

    def __init__(self, rows, columns):
        super(MyTable, self).__init__(rows, columns)
        # this was added because whenever the csv writer changes the
        # value of a row,col, it calls c_current but no cell is selected
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)

        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()      # current row of the table instance
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print('The current cell is ', row, ', ', col)
            print('In this cell we have: ', value)

    def open_sheet(self):
        self.check_change = False       # since this is false, c_current will not run
        # last argument is a filter so that it will only show CSV files
        path = QFileDialog.getOpenFileName(self, 'Open csv', os.getenv('HOME'), 'CSV(*.csv')

        # path[0] = filename
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.columnCount(10)
                # my_file = csv.reader(csv_file, delimeter=',', quotechar='|')
                my_file = csv.reader(csv_file, dialect='excel')

                for row_data in my_file:

                    # 0 = counted, so value would be one more
                    row = self.rowCount()
                    # so no need to add one, because you'll be automatically at next row
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True

    def save_sheet(self):

        path = QFileDialog.getSaveFileName(self, 'Save csv', os.getenv('HOME'), 'CSV(*.csv')

        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for col in range(self.columnCount()):
                        item = self.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')

                    writer.writerow(row_data)


class Sheet(QMainWindow):
    #form_widget = MyTable(10, 10)

    def __init__(self):
        super(Sheet, self).__init__()

        form_widget = MyTable(10,10)        # used self in the original tuts

        self.setCentralWidget(form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        form_widget.setHorizontalHeaderLabels(col_headers)

        # not needed for lesson 19, we'll do this from the file menu
        # form_widget.open_sheet()    # super method

        # set up menu
        bar = self.menuBar()
        file = bar.addMenu('File')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_aciton = QAction('&Open', self)

        quit_aciton = QAction('&Quit', self)

        file.addAction(save_action)
        file.addAction(open_aciton)
        file.addAction(quit_aciton)

        quit_aciton.triggered.connect(self.quit_app)
        save_action.triggered.connect(form_widget.save_sheet)
        open_aciton.triggered.connect(form_widget.open_sheet)

        self.show()

    @staticmethod
    def quit_app():
        qApp.quit()

app = QApplication([])
sheet = Sheet()
#sys.exit(app.exec_())
app.exec_()