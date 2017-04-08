from PyQt5 import QtWidgets, QtGui          # QtGui for images
import sys

'''
Lesson 4: Box Layout (1/3 of series of buttons that do somehting)
'''

def window():
    app = QtWidgets.QApplication([])
    mw = QtWidgets.QWidget()
    #note that objects below were not added to mw
    button = QtWidgets.QPushButton('Push Me')       # prev lession, the argument was mw
    l = QtWidgets.QLabel('Look at Me')              # Note that the string args are usually done with setText


    # hBox = horizontal box
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()      # stretch = will fill up as much space horizontally as it can
    h_box.addWidget(l)
    h_box.addStretch()      # in this program, this was used to centralize the label 'look at me'

    # put button and l in a vBoxLayout
    # vBox = vertical box
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(button)
    # v_box.addWidget(l)    # because already in hBox
    v_box.addLayout(h_box)

    mw.setLayout(v_box)     # what does this do again?

    mw.setWindowTitle('PyQt5 Lesson 4')
    mw.show()

    sys.exit(app.exec_())

window()