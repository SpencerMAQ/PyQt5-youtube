from PyQt5.QtWidgets import (QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget)          # QtGui for images
from PyQt5.QtCore import Qt
import sys


'''
Lesson 9: Checkbox
Slider
'''

class Window(QWidget):

    def __init__(self):
        super().__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.cbx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton('Push Me')


        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cbx)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        # what this does is changes the label when you click
        # 'Push Me', together with ticking (or not) the box
        self.btn.clicked.connect(lambda: self.btn_clk(self.cbx.isChecked(), self.lbl))
        # Note to self: you can omit the 'self' part of things you'd want to send
        # to slots if you'd use lambda functions, as in:
            # lbl = QLabel()
            # self.btn.clicked.connect(lambda: self.btn_clk(self.cbx.isChecked(), lbl))
            # where lbl is sent as an argument

        self.setWindowTitle('PyQt5 Lesson 9')

        self.show()

    @staticmethod
    def btn_clk(isChecked, label):
        if isChecked:                               # == True:
            label.setText('I see you like dogs')

        else:
            label.setText('Dog hater then')

app = QApplication([])
a_window = Window()
sys.exit(app.exec_())