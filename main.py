from __future__ import print_function
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

from maker import maker_main

class UniViewSigGrpMakerWindow(QtGui.QMainWindow):
    def __init__(self):
        super(UniViewSigGrpMakerWindow, self).__init__()
        exit_btn = QtGui.QPushButton('Exit!', self)
        exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        exit_btn.resize(exit_btn.sizeHint())
        exit_btn.move(100, 100)

        input_file_btn = QtGui.QPushButton('CSV file', self)
        input_file_btn.clicked.connect(self.inputFilePicker)
        input_file_btn.resize(input_file_btn.sizeHint())
        input_file_btn.move(0, 0)

        output_file_btn = QtGui.QPushButton('Output file', self)
        output_file_btn.clicked.connect(self.outputFilePicker)
        output_file_btn.resize(output_file_btn.sizeHint())
        output_file_btn.move(0, 50)

        do_action_btn = QtGui.QPushButton('Convert', self)
        do_action_btn.clicked.connect(self.do_action)
        do_action_btn.resize(do_action_btn.sizeHint())
        do_action_btn.move(0, 100)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Uniview signal group maker')
        self.show()

    def inputFilePicker(self):
        self.input_file = QtGui.QFileDialog.getOpenFileName(self, 'Open file')

    def outputFilePicker(self):
        self.output_file = QtGui.QFileDialog.getOpenFileName(self, 'Open file')

    def do_action(self):
        maker_main([None, self.input_file, self.output_file])

def main():
    app = QtGui.QApplication(sys.argv)

    ex = UniViewSigGrpMakerWindow()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
