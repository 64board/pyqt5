#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QTextEdit, QPushButton,
                             QApplication, QVBoxLayout)

class PyQtTextEdit(QWidget):

    def __init__(self):
        super().__init__()
        self.UI()

    def display(self):
        print(self._text_edit.toPlainText().splitlines())

    def UI(self):
        self._text_edit = QTextEdit()
        self.button_check = QPushButton('Check')
        self.button_check.clicked.connect(self.display)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self._text_edit)
        self.vbox.addWidget(self.button_check)

        self.setLayout(self.vbox)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('PyQt5 QTextEdit')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = PyQtTextEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

##END##
