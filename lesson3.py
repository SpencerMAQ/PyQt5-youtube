from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

'''
Lesson 3: Adding buttons
'''

def window():
    app = QtWidgets.QApplication([])
    mw = QtWidgets.QWidget()

    button = QtWidgets.QPushButton(mw)
    l = QtWidgets.QLabel(mw)
    button.setText('PushMe Lesson3')
    l.setText('setText')

    mw.setWindowTitle('PyQt5 Lesson 1')

    button.move(100, 50)
    l.move(110, 100)

    mw.setGeometry(100, 100, 300, 200)      # first 2 args: origin, 2nd 2 args= size

    mw.show()

    sys.exit(app.exec_())
    #app.exec_()

window()