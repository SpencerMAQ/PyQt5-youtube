from PyQt5.QtWidgets import (QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog)          # QtGui for images
import sys
import os


'''
Lesson 13: (1/5) Simple Text Editor with QFIleDialog
(3/5) Save Files
File Dialog, SOrted Dialog
Menu Bar
Put all together for Notepad program
'''

'dasdasd'

class Notepad(QWidget):

    def __init__(self):

        super(Notepad, self).__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.sav_btn = QPushButton('Save')      # added 2 more buttons from prev
        self.opn_btn = QPushButton('Open')

        self.init_ui()
        # return self, text, clr_btn

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)


        v_layout.addWidget(self.text)
       # v_layout.addWidget(self.clr_btn)  # previous vid
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)   # new
        self.opn_btn.clicked.connect(self.open_text)       #new

        self.setLayout(v_layout)
        self.setWindowTitle('Lesson11: QTextEdit')

        self.show()

    def save_text(self):
        # args = (self, __title of Dialog Box__, )
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as fh:      # QFileDialog.get.... returns a tuple, you only want the first
            my_text = self.text.toPlainText()
            fh.write(my_text)

    def clear_text(self):   # new from prev vid
        self.text.clear()

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as fh:      # QFileDialog.get.... returns a tuple, you only want the first
            file_text = fh.read()
            self.text.setText(file_text)

app = QApplication([])
a_window = Notepad()
sys.exit(app.exec_())