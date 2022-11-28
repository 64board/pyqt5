#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QApplication, QVBoxLayout)

class PyQtLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        button1 = QPushButton('PyQt')
        button2 = QPushButton('Layout')
        button3 = QPushButton('Management')

        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Layout')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

##END##
