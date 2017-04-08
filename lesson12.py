from PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout)          # QtGui for images
import sys


'''
Lesson 12: (1/5) TextEdit
(2/5) Save Files
File Dialog, SOrted Dialog
Menu Bar
Put all together for Notepad program
'''

class Notepad(QWidget):

    def __init__(self):

        super(Notepad, self).__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Save')

        self.init_ui()
        # return self, text, clr_btn

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.clr_btn)

        self.clr_btn.clicked.connect(self.save_text)

        self.setLayout(layout)
        self.setWindowTitle('Lesson11: QTextEdit')

        self.show()

    def save_text(self):
        with open('test.txt', 'w') as fh:
            my_text = self.text.toPlainText()
            fh.write(my_text)


app = QApplication([])
a_window = Notepad()
sys.exit(app.exec_())