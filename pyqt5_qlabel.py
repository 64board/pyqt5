#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,500,300)
    win.setWindowTitle("CodersLegacy")

    label = QtWidgets.QLabel(win)
    label.setText("GUI application with PyQt5")
    label.adjustSize()
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())

def main():
    window()

if __name__ == '__main__':
    main()

##END##
