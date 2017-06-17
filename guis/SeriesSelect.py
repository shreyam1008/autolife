# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeriesSelect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_series_search(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Ui_series_search, self).__init__(parent)
        self.series_search = QtGui.QWidget()
        self.series_search.setObjectName(_fromUtf8("series_search"))
        self.series_search.resize(583, 389)
        self.series_list_tableView = QtGui.QTableView(self.series_search)
        self.series_list_tableView.setGeometry(QtCore.QRect(20, 50, 291, 211))
        self.series_list_tableView.setObjectName(_fromUtf8("series_list_tableView"))
        self.series_search_window_label = QtGui.QLabel(self.series_search)
        self.series_search_window_label.setGeometry(QtCore.QRect(90, 10, 411, 31))
        self.series_search_window_label.setObjectName(_fromUtf8("series_search_window_label"))
        self.series_image_graphicsview = QtGui.QGraphicsView(self.series_search)
        self.series_image_graphicsview.setGeometry(QtCore.QRect(320, 50, 256, 192))
        self.series_image_graphicsview.setObjectName(_fromUtf8("series_image_graphicsview"))
        self.buttonBox = QtGui.QDialogButtonBox(self.series_search)
        self.buttonBox.setGeometry(QtCore.QRect(140, 350, 193, 28))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(self.series_search)
        self.label.setGeometry(QtCore.QRect(80, 270, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.series_search)
        self.comboBox.setGeometry(QtCore.QRect(80, 300, 73, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(self.series_search)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 300, 73, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_2 = QtGui.QLabel(self.series_search)
        self.label_2.setGeometry(QtCore.QRect(30, 300, 53, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.series_search)
        self.label_3.setGeometry(QtCore.QRect(250, 300, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(self.series_search)
        QtCore.QMetaObject.connectSlotsByName(self.series_search)

    def retranslateUi(self, series_search):
        series_search.setWindowTitle(_translate("series_search", "Select your series", None))
        self.series_search_window_label.setText(_translate("series_search", "Multiple series with same name: Which one do you mean", None))
        self.label.setText(_translate("series_search", "From where you wanna track", None))
        self.label_2.setText(_translate("series_search", "Season", None))
        self.label_3.setText(_translate("series_search", "Episode", None))

        

def runthis():
    import sys
    app = QtGui.QApplication(sys.argv)
    a = Ui_series_search()
    a.series_search.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    runthis()



