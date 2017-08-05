# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from guis import SeriesSelect, MangaSelect, ClubSelect
import DatabaseManager
import webbrowser


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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.MainWindow = QtGui.QMainWindow()
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.MainWindow.resize(959, 750)
        self.MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setIconSize(QtCore.QSize(50, 50))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_home = QtGui.QWidget()
        self.tab_home.setObjectName(_fromUtf8("tab_home"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("a"))
        self.tabWidget.addTab(self.tab_home, icon, _fromUtf8(""))
        self.tab_series = QtGui.QWidget()
        self.tab_series.setObjectName(_fromUtf8("tab_series"))
        self.series_lineEdit = QtGui.QLineEdit(self.tab_series)
        self.series_lineEdit.setGeometry(QtCore.QRect(590, 10, 251, 21))
        self.series_lineEdit.setText(_fromUtf8(""))
        self.series_lineEdit.setObjectName(_fromUtf8("series_lineEdit"))
        self.series_search_label = QtGui.QLabel(self.tab_series)
        self.series_search_label.setGeometry(QtCore.QRect(440, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.series_search_label.setFont(font)
        self.series_search_label.setObjectName(_fromUtf8("series_search_label"))
        self.series_search_pushButton = QtGui.QPushButton(self.tab_series)
        self.series_search_pushButton.setGeometry(QtCore.QRect(850, 10, 71, 21))
        self.series_search_pushButton.setObjectName(_fromUtf8("series_search_pushButton"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("a"))
        self.tabWidget.addTab(self.tab_series, icon, _fromUtf8(""))
        self.tab_movies = QtGui.QWidget()
        self.tab_movies.setObjectName(_fromUtf8("tab_movies"))
        self.series_search_label_3 = QtGui.QLabel(self.tab_movies)
        self.series_search_label_3.setGeometry(QtCore.QRect(440, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.series_search_label_3.setFont(font)
        self.series_search_label_3.setObjectName(_fromUtf8("series_search_label_3"))
        self.series_lineEdit_3 = QtGui.QLineEdit(self.tab_movies)
        self.series_lineEdit_3.setGeometry(QtCore.QRect(590, 10, 251, 21))
        self.series_lineEdit_3.setText(_fromUtf8(""))
        self.series_lineEdit_3.setObjectName(_fromUtf8("series_lineEdit_3"))
        self.series_search_pushButton_3 = QtGui.QPushButton(self.tab_movies)
        self.series_search_pushButton_3.setGeometry(QtCore.QRect(850, 10, 71, 21))
        self.series_search_pushButton_3.setObjectName(_fromUtf8("series_search_pushButton_3"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("a"))
        self.tabWidget.addTab(self.tab_movies, icon, _fromUtf8(""))
        self.tab_manga = QtGui.QWidget()
        self.tab_manga.setObjectName(_fromUtf8("tab_manga"))
        self.series_search_pushButton_4 = QtGui.QPushButton(self.tab_manga)
        self.series_search_pushButton_4.setGeometry(QtCore.QRect(850, 20, 71, 21))
        self.series_search_pushButton_4.setObjectName(_fromUtf8("series_search_pushButton_4"))
        self.series_search_label_4 = QtGui.QLabel(self.tab_manga)
        self.series_search_label_4.setGeometry(QtCore.QRect(440, 20, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.series_search_label_4.setFont(font)
        self.series_search_label_4.setObjectName(_fromUtf8("series_search_label_4"))
        self.series_lineEdit_4 = QtGui.QLineEdit(self.tab_manga)
        self.series_lineEdit_4.setGeometry(QtCore.QRect(590, 20, 251, 21))
        self.series_lineEdit_4.setText(_fromUtf8(""))
        self.series_lineEdit_4.setObjectName(_fromUtf8("series_lineEdit_4"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("on"))
        self.tabWidget.addTab(self.tab_manga, icon, _fromUtf8(""))
        self.tab_football = QtGui.QWidget()
        self.tab_football.setObjectName(_fromUtf8("tab_football"))
        self.football_addteam_pushbutton = QtGui.QPushButton(self.tab_football)
        self.football_addteam_pushbutton.setGeometry(QtCore.QRect(750, 20, 161, 31))
        self.football_addteam_pushbutton.setObjectName(_fromUtf8("football_addteam_pushbutton"))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("a"))
        self.tabWidget.addTab(self.tab_football, icon, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        ###button connections
        self.football_addteam_pushbutton.clicked.connect(self.footballSearchWindow)
        self.series_search_pushButton_4.clicked.connect(self.mangaSearchWindow)
        self.series_search_pushButton_3.clicked.connect(self.moviesSearchWindow)

        
        ##adding table to main window to display main data
        self.series_search_pushButton.clicked.connect(self.seriesSearchWindow)
        self.table = QtGui.QTableWidget(self.tab_series)
        self.table.setGeometry(QtCore.QRect(30, 50, 800, 500))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels("series name; season;latest epi; link".split(";"))
        self.setTableData()


    def setTableData(self):
        self.db = DatabaseManager.DatabaseForAll(tablename = 'series_table')
        for vsk in self.db.GetTable():
            print(vsk[0], vsk[1], vsk[2], vsk[3], vsk[4])
        self.count_row = sum(1 for _ in self.db.GetTable())
        print(self.count_row)
        self.table.setRowCount(self.count_row)
        self.table.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

        self.link_buttons = dict(enumerate([QtGui.QPushButton('Goto site') for i in range(self.count_row + 1)]))


        for x, tup in zip(range(self.count_row+1), self.db.GetTable()):
            for y in range(self.count_row+1):
                if y == 0: self.table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[1])))
                if y == 1: self.table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[2])))
                if y == 2: self.table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[3])))
                if y == 3: self.table.setCellWidget(x, y, self.link_buttons[x])

        for x, tup in zip(range(self.count_row), self.db.GetTable()):
            self.link_buttons[x].clicked.connect(lambda: webbrowser.open(tup[4]))


    ### modules for buttn connections
    def seriesSearchWindow(self):

        print(self.series_lineEdit.text())
        a = SeriesSelect.Ui_series_search(str(self.series_lineEdit.text()))
        a.series_search.show()

    def footballSearchWindow(self):

        a = ClubSelect.UiFootballSelect(self)
        a.Form.show()

    def mangaSearchWindow(self):

        a = MangaSelect.UiMangaSelect()
        a.Form.show()

    def moviesSearchWindow(self):
        pass


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("MainWindow", "Home", None))
        self.series_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the series or anime", None))
        self.series_search_label.setText(_translate("MainWindow", "Search your series:", None))
        self.series_search_pushButton.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_series), _translate("MainWindow", "Series", None))
        self.series_search_label_3.setText(_translate("MainWindow", "Search your movie:", None))
        self.series_lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter a movie", None))
        self.series_search_pushButton_3.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_movies), _translate("MainWindow", "Movies", None))
        self.series_search_pushButton_4.setText(_translate("MainWindow", "Search", None))
        self.series_search_label_4.setText(_translate("MainWindow", "Search your manga:", None))
        self.series_lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter a movie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manga), _translate("MainWindow", "Manga", None))
        self.football_addteam_pushbutton.setText(_translate("MainWindow", "Add a team to follow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_football), _translate("MainWindow", "Football", None))


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    a = Ui_MainWindow()
    a.MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

