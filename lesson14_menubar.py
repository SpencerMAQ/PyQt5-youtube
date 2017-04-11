from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp)          # QtGui for images
import sys
import os


'''
Lesson 14: Making Menu Bars
>create root menus
>create menu actions
>add the actions or sub-menus


(3/5) Save Files
File Dialog, SOrted Dialog
Menu Bar
Put all together for Notepad program
'''

'dasdasd'

class Notepad(QMainWindow):     # QMainWindow instead of widget because now we have menu bars



    def __init__(self):

        super(Notepad, self).__init__()                  # this is essential the same as w = QTWidgets.QWidget() where init happens automatically

        # create menu bar
        bar = self.menuBar()        # self = QMainWindow a_window instance


        # create root menus         # i.e. things to click in menu bar
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # create actions for menus
        save_action = QAction('Save', self)     # 2nd arg = reference to widget
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)       # 2nd arg = reference to widget
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('&Quit', self)    # 2nd arg = reference to widget
        # if with starting ampersand, when you click 'Q' when File is clicked, it will quit the app
        quit_action.setShortcut('Ctrl+Q')

        find_action = QAction('Find...', self)

        replace_action = QAction('Replace...', self)

        # add actions to menus
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        find_menu = edit.addMenu('Find')        # add 'Find' the 'Edit' menu bar
        find_menu.addAction(find_action)        # add submenu to the Find menu
        find_menu.addAction(replace_action)

        # events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("My Menus")
        self.resize(600, 600)

        self.show()

    def quit_trigger(self):
        qApp.quit()     # quits the app

    @staticmethod
    def selected(q):
        # question to self, where does 'q' come from
        print(q.text() + ' selected')
        # prints name of the clicked button to console

app = QApplication([])
a_window = Notepad()
sys.exit(app.exec_())
