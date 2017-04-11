from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QWidget)          # QtGui for images
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp)          # QtGui for images
import sys
import os


'''
Lesson 15:
Notepad with menu bar
'''

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

class Writer(QMainWindow):

    def __init__(self):
        super(Writer, self).__init__()

        self.form_widget = Notepad()        # creates an instance of Notepad (which happens to be a QWidget)
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()    # self, note you can't set this as a class att
                                # because you are setting the menubar for the writer instance, self
        file = bar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.show()

    @staticmethod
    def quit_trigger():
        qApp.quit()

    # I'm still wondering why this works, what argument was passed as  'q'?
    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()    # form_widget = instance of Notepad
        elif signal == '&Open':
            self.form_widget.open_text()     # open, clear are super methods from Notepad
        elif signal == '&Save':
            self.form_widget.save_text()

app = QApplication([])
writer = Writer()
sys.exit(app.exec_())