from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)          # QtGui for images
import sys


'''
Lesson 10: QRadioButton
Slider
'''

class Window(QWidget):

    def __init__(self):
        super().__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically

        self.init_ui()

    def init_ui(self):
        # note: I removed self from each of these
        label = QLabel('Which do you like best?')
        dog = QRadioButton('Dogs')
        cat = QRadioButton('Cats')
        btn = QPushButton('Select')

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(dog)
        layout.addWidget(cat)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setWindowTitle('Lesson 10: radio')

        btn.clicked.connect(lambda: self.btn_clk(dog.isChecked(), label))
        # dog.toggled.connect
        # call a function when dog is selected

        self.show()

    @staticmethod
    def btn_clk(dog_is_checked, lbl):
        if dog_is_checked:
            lbl.setText('I guess you like dogs')
        else:
            lbl.setText('I guess you like cats')


app = QApplication([])
a_window = Window()
sys.exit(app.exec_())