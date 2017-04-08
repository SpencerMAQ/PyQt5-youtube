from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

'''
Lesson 7: Linedit
LineEdit - takes text
(1/2) ) - display screen with push button
(2/2)(this - properties and controls
'''

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lineEdit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Clear')

        self.button2 = QtWidgets.QPushButton('Print')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lineEdit)
        v_box.addWidget(self.button)

        v_box.addWidget(self.button2)

        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 Lesson 6')

        self.button.clicked.connect(self.btn_clicked)
        self.button.clicked.connect(self.btn_clicked)

        self.show()

    def btn_clicked(self):
        sender = self.sender()
        # sends info about where the action came from

        # from _init_ui self.button2 = QtWidgets.QPushButton('Print')
        if sender.text() == 'Print':
            print(self.lineEdit.text())

        if sender.text() == 'Clear':
            self.lineEdit.clear()

app = QtWidgets.QApplication([])
a_window = Window()
sys.exit(app.exec_())