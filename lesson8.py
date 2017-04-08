from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)          # QtGui for images
from PyQt5.QtCore import Qt
import sys


'''
Lesson 7: Slider
Slider
'''

class Window(QWidget):

    def __init__(self):
        super().__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically

        self.init_ui()

    def init_ui(self):
        print(self)
        self.lineEdit = QLineEdit()         # allows you to type in text???
        self.button = QPushButton('Clear')
        self.button2 = QPushButton('Print')
        self.s1 = QSlider(Qt.Horizontal) # slider can be vert or hor #Qt.Core contains Qt object properties
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)             # slider won't show unless you add it to the window/widget
        self.s1.setTickInterval(10)      # puts marks along the slider
        self.s1.setTickPosition(QSlider.TicksBelow) # set location of ticks

        v_box = QVBoxLayout()
        v_box.addWidget(self.lineEdit)
        v_box.addWidget(self.button)

        v_box.addWidget(self.button2)

        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 6')

        # the methods below send the sender without using self.sender()
        # used lambda in order to send arguments
        self.button.clicked.connect(lambda: self.btn_clk(self.button, 'Hello from Clear'))
        self.button2.clicked.connect(lambda: self.btn_clk(self.button2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.v_change)     # no need for lambda because the function only takes self as arg
        # valueChanged = slider moves

        self.show()

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.lineEdit.text())

        #else:
        elif b.text() == 'Clear': # my edit:, makes sure the sender is from clear
            self.lineEdit.clear()

        print(string)   # output to console, not program

    def v_change(self):
        my_val = str(self.s1.value())
        self.lineEdit.setText(my_val)


app = QApplication([])
a_window = Window()
sys.exit(app.exec_())