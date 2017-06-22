# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeriesSelect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

########### self added lines
from cores import series
##########################
import functools
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
    def __init__(self, series_name, parent = None ):
        super(Ui_series_search, self).__init__(parent)

        ##########################################
 
        self.fromseries = series.SeriesNAnime(name = series_name, season = 1)

        ############################################
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

        ########################################################
        self.setTable()
        self.setCombos()


    def setTable(self):
        self.table = QtGui.QTableWidget(self.series_list_tableView)
        self.table.resize(291, 211)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels("name;start date;select;".split(";"))

        self.count_row = sum(1 for _ in self.fromseries.samenames())

        self.table.setRowCount(self.count_row)
        self.table.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

        self.select_buttons = dict(enumerate([QtGui.QPushButton('this') for i in range(self.count_row + 1)]))

        for x, tup in zip(range(self.count_row + 1), self.fromseries.samenames()) :
            for y in range(self.count_row + 1):
                if y == 0: self.table.setItem(x, y, QtGui.QTableWidgetItem(tup['seriesname']))
                if y == 1: self.table.setItem(x, y, QtGui.QTableWidgetItem(tup['date']))
                if y == 2: self.table.setCellWidget(x, y, self.select_buttons[x])

    def setCombos(self):
         #combobox for season
        self.comboBox = QtGui.QComboBox(self.series_search)
        self.comboBox.setGeometry(QtCore.QRect(80, 300, 73, 22))
        
        #combobox for episode
        self.comboBox_2 = QtGui.QComboBox(self.series_search)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 300, 73, 22))

        #to generate season combobox
        for x in range(self.count_row):
            self.select_buttons[x].clicked.connect(functools.partial(self.seasonSelect, x))

        #to generate episode combobox
        self.comboBox.activated.connect(self.episodeSelect)

    def seasonSelect(self, ser_no):
        print('series no is ', ser_no)
        #change range to no of seaosn by search
        for x in range(self.fromseries.seasonNumber()):
            self.comboBox.addItem(str(x))

    def episodeSelect(self):
        print('season no is ', int(self.comboBox.currentText()))
        #find total epi and add
        for x in range(sum(1 for _ in self.fromseries.epiList())):
            self.comboBox_2.addItem(str(x))

    def retranslateUi(self, series_search):
        series_search.setWindowTitle(_translate("series_search", "Select your series", None))
        self.series_search_window_label.setText(_translate("series_search", "Multiple series with same name: Which one do you mean", None))
        self.label.setText(_translate("series_search", "From where you wanna track", None))
        self.label_2.setText(_translate("series_search", "Season", None))
        self.label_3.setText(_translate("series_search", "Episode", None))

        

def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    a = Ui_series_search()
    a.series_search.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



