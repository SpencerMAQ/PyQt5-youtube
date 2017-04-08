from PyQt5 import QtWidgets
import sys

def window():
    app = QtWidgets.QApplication([])
    mw = QtWidgets.QWidget()
    mw.setWindowTitle('PyQt5 Lesson 1')
    mw.show()
    #sys.exit(app.exec_())
    app.exec_()

window()