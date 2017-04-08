from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

'''
Lesson 5: Lesson5 Signals and slot (2/3 of series of buttons that do somehting)
signal = calls a function which is a slot, to change the text of the label
'''

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        # it is defined outside of __init__, but it's not a problem
        # because __init__ will call this function everytime
        self.button = QtWidgets.QPushButton('Push Me')              #note: these were
                    # probably made as class attributes (hence self) so that they can be called from btn_clk
        self.label = QtWidgets.QLabel('I have not been clicked')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 5')

        # does whatever is in the parentheses when button is clicked
        self.button.clicked.connect(self.btn_click)

        self.show()


    def btn_click(self):
        self.button.setText('I have been clicked')

        self.label.setText('I have been clicked')

app = QtWidgets.QApplication([])
a_window = Window()
sys.exit(app.exec_())