# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys

from guis import mainwindow

from PyQt4 import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    homepage = mainwindow.Ui_MainWindow()

    #print(homepage.series_lineEdit.text())
    homepage.MainWindow.show()

     

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

