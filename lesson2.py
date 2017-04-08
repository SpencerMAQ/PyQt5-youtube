from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

def window():
    app = QtWidgets.QApplication([])
    mw = QtWidgets.QWidget()


    l1 = QtWidgets.QLabel(mw)               # add label to mw
    l1.setText('PyQt Lesson 2 Label')       # add text to above object

    l2 = QtWidgets.QLabel(mw)
    l2.setPixmap(QtGui.QPixmap('globe.png'))

    mw.setWindowTitle('PyQt5 Lesson 1')
    mw.setGeometry(100, 100, 300, 200)      # first 2 args: origin, 2nd 2 args= size

    l1.move(100, 20)                        # move l1 object
    l2.move(120, 90)

    mw.show()   # show window, if this was placed before l1,
                # the label would not show

    sys.exit(app.exec_())
    #app.exec_()

window()