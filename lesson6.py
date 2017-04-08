from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

'''
Lesson 6: Linedit (3/3 of series of buttons that do somehting)
LineEdit - takes text
(1/2) (this) - display screen with push button
(2/2) - properties and controls
'''

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lineEdit = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Clear')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lineEdit)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle('PyQt5 Lesson 6')

        self.show()

app = QtWidgets.QApplication([])
a_window = Window()
sys.exit(app.exec_())