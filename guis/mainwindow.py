# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!



from guis import SeriesSelect, MangaSelect, ClubSelect
import DatabaseManager
import webbrowser
from cores import football, lyrics

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

class Ui_MainWindow(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__(parent)

		self.fromfootball = football.Footy()


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
		# self.tab_movies = QtGui.QWidget()
		# self.tab_movies.setObjectName(_fromUtf8("tab_movies"))
		# self.series_search_label_3 = QtGui.QLabel(self.tab_movies)
		# self.series_search_label_3.setGeometry(QtCore.QRect(440, 10, 141, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		# self.series_search_label_3.setFont(font)
		# self.series_search_label_3.setObjectName(_fromUtf8("series_search_label_3"))
		# self.series_lineEdit_3 = QtGui.QLineEdit(self.tab_movies)
		# self.series_lineEdit_3.setGeometry(QtCore.QRect(590, 10, 251, 21))
		# self.series_lineEdit_3.setText(_fromUtf8(""))
		# self.series_lineEdit_3.setObjectName(_fromUtf8("series_lineEdit_3"))
		# self.series_search_pushButton_3 = QtGui.QPushButton(self.tab_movies)
		# self.series_search_pushButton_3.setGeometry(QtCore.QRect(850, 10, 71, 21))
		# self.series_search_pushButton_3.setObjectName(_fromUtf8("series_search_pushButton_3"))
		# icon = QtGui.QIcon.fromTheme(_fromUtf8("a"))
		# self.tabWidget.addTab(self.tab_movies, icon, _fromUtf8(""))
		self.tab_manga = QtGui.QWidget()
		self.tab_manga.setObjectName(_fromUtf8("tab_manga"))
		self.manga_search_pushbutton = QtGui.QPushButton(self.tab_manga)
		self.manga_search_pushbutton.setGeometry(QtCore.QRect(850, 20, 71, 21))
		self.manga_search_pushbutton.setObjectName(_fromUtf8("manga_search_pushbutton"))
		self.manga_search_label = QtGui.QLabel(self.tab_manga)
		self.manga_search_label.setGeometry(QtCore.QRect(440, 20, 141, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.manga_search_label.setFont(font)
		self.manga_search_label.setObjectName(_fromUtf8("manga_search_label"))
		self.manga_linedit = QtGui.QLineEdit(self.tab_manga)
		self.manga_linedit.setGeometry(QtCore.QRect(590, 20, 251, 21))
		self.manga_linedit.setText(_fromUtf8(""))
		self.manga_linedit.setObjectName(_fromUtf8("manga_linedit"))
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


		###adding songs tab
		self.tab_songs = QtGui.QWidget()
		self.tab_songs.setObjectName(_fromUtf8("tab_songs"))
		self.tabWidget.addTab(self.tab_songs, icon, _fromUtf8(""))
		##adding songs search bar
		self.songs_search_label = QtGui.QLabel(self.tab_songs)
		self.songs_search_label.setGeometry(QtCore.QRect(440, 10, 141, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.songs_search_label.setFont(font)
		self.songs_search_label.setObjectName(_fromUtf8("series_search_label"))
		self.songs_search_label.setText(_translate("MainWindow", "Search your song:", None))
		self.artist_linedit =  QtGui.QLineEdit(self.tab_songs)
		self.artist_linedit.setGeometry(QtCore.QRect(590, 10, 130, 21))
		self.artist_linedit.setText(_fromUtf8(""))
		self.artist_linedit.setObjectName(_fromUtf8("artist_linedit"))
		self.song_linedit =  QtGui.QLineEdit(self.tab_songs)
		self.song_linedit.setGeometry(QtCore.QRect(700, 10, 130, 21))
		self.song_linedit.setText(_fromUtf8(""))
		self.song_linedit.setObjectName(_fromUtf8("song_linedit"))
		self.song_linedit.setPlaceholderText(_translate("MainWindow", "Song", None))
		self.artist_linedit.setPlaceholderText(_translate("MainWindow", "Artist Name", None))

		self.lyrics_display = QtGui.QPlainTextEdit(self.tab_songs)
		self.lyrics_display.setGeometry(QtCore.QRect(50,50, 400,800))
		self.lyrics_display.setObjectName(_fromUtf8("lyrics_display"))

		self.song_search_pushbutton = QtGui.QPushButton(self.tab_songs)
		self.song_search_pushbutton.setGeometry(QtCore.QRect(835, 10, 65, 30))
		self.song_search_pushbutton.setObjectName(_fromUtf8("song_search_pushbutton"))
		self.song_search_pushbutton.setText(_translate("MainWindow", "Get Lyrics", None))



		
		self.tabWidget.setCurrentIndex(1)
		

		###button connections
		self.football_addteam_pushbutton.clicked.connect(self.footballSearchWindow)
		self.manga_search_pushbutton.clicked.connect(self.mangaSearchWindow)
		self.series_search_pushButton.clicked.connect(self.seriesSearchWindow)
		self.song_search_pushbutton.clicked.connect(self.lyricsDisplay)
		# self.series_search_pushButton_3.clicked.connect(self.moviesSearchWindow)

		
		##adding table to main window to display main data
		self.setSeriesTable()
		self.setMangaTable()

		self.setLeagueTable()
		self.setClubScores()
		
		##adding refresh button in manga and series and foorball. to refresh the table
		self.series_refresh = QtGui.QPushButton(self.tab_series)
		self.series_refresh.setGeometry(QtCore.QRect(10, 10, 55, 30))
		self.series_refresh.setObjectName(_fromUtf8("series_refresh"))

		self.manga_refresh = QtGui.QPushButton(self.tab_manga)
		self.manga_refresh.setGeometry(QtCore.QRect(10, 10, 55, 30))
		self.manga_refresh.setObjectName(_fromUtf8("manga_refresh"))

		self.football_refresh = QtGui.QPushButton(self.tab_football)
		self.football_refresh.setGeometry(QtCore.QRect(10, 10, 55, 30))
		self.football_refresh.setObjectName(_fromUtf8("football_refresh"))

		#refresh button actions
		self.series_refresh.clicked.connect(lambda: self.setTableData())
		self.manga_refresh.clicked.connect(lambda: self.setDatas())
		# self.football_refresh.clicked.connect()


		self.retranslateUi(self.MainWindow)
		QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

	def lyricsDisplay(self):
		self.lyr = lyrics.Lyric()
		self.text = self.lyr.getLyrics(str(self.artist_linedit.text()), str(self.song_linedit.text()))

		self.lyrics_display.setPlainText(self.text)




	def setLeagueTable(self):
		self.league_table_label = QtGui.QLabel(self.tab_football)
		self.league_table_label.setGeometry(QtCore.QRect(480, 80, 141, 20))
		self.league_table_label.setText(_translate("MainWindow", "League Table", None))
		self.league_table = QtGui.QTableWidget(self.tab_football)
		self.league_table.setGeometry(QtCore.QRect(500, 100, 400, 500))

		self.league_table.setColumnCount(3)
		self.league_table.setHorizontalHeaderLabels('position;team;points;GD'.split(";"))


		self.league_table.setRowCount(20)

		for x, tup in zip(range(20), self.fromfootball.LeagueTable(league_id = 426)):
			for y in range(3):
				# if y == 0: self.league_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['position'])))
				if y == 0: self.league_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['teamName'])))
				if y == 1: self.league_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['points'])))
				if y == 2: self.league_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['goalDifference'])))

	def setClubScores(self):
		self.score_label = QtGui.QLabel(self.tab_football)
		self.score_label.setGeometry(QtCore.QRect(180, 80, 141, 20))
		self.score_label.setText(_translate("MainWindow", "Scores of Your Club", None))
		self.score_table = QtGui.QTableWidget(self.tab_football)
		self.score_table.setGeometry(QtCore.QRect(20, 100, 400, 500))

		self.score_table.setColumnCount(4)
		self.score_table.setHorizontalHeaderLabels('home team;home score;away team;away score'.split(";"))

		self.score_table.setRowCount(38)

		for x, tup in zip(range(38), self.fromfootball.TeamFixtures(team_id = 65)):
			for y in range(4):
				if y == 0: self.score_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['homeTeamName'])))
				if y == 1: self.score_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['homeScore'])))
				if y == 2: self.score_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['awayScore'])))
				if y == 3: self.score_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup['awayTeamName'])))


	def setSeriesTable(self):
		
		self.series_table = QtGui.QTableWidget(self.tab_series)
		self.series_table.setGeometry(QtCore.QRect(30, 50, 800, 500))
		self.series_table.setColumnCount(4)
		self.series_table.setHorizontalHeaderLabels("series name; season;latest epi; link".split(";"))
		self.setTableData()

	def setTableData(self):

		self.db = DatabaseManager.DatabaseForAll(tablename = 'series_table')
		self.count_row = sum(1 for _ in self.db.GetTable())
		print(self.count_row)
		self.series_table.setRowCount(self.count_row)
		self.series_table.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

		self.link_buttons = dict(enumerate([QtGui.QPushButton('Goto site') for i in range(self.count_row + 1)]))

		for x, tup in zip(range(self.count_row+1), self.db.GetTable()):
			for y in range(self.count_row + 1):
				if y == 0: self.series_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[1])))
				if y == 1: self.series_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[2])))
				if y == 2: self.series_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[3])))
				if y == 3: self.series_table.setCellWidget(x, y, self.link_buttons[x])

		for x, tup in zip(range(self.count_row), self.db.GetTable()):
			self.link_buttons[x].clicked.connect(functools.partial(self.gotoSite, x))

	def gotoSite(self, x):
		
		for i,y in enumerate(self.db.GetTable()):
			if x == i:
				webbrowser.open(y[4])
				self.db.updateTable(ID = int(x)+1)
				self.setTableData()




	def setMangaTable(self):
		self.manga_table = QtGui.QTableWidget(self.tab_manga)
		self.manga_table.setGeometry(QtCore.QRect(30, 50, 500, 400))
		self.manga_table.setColumnCount(3)
		self.manga_table.setHorizontalHeaderLabels("Manga name; last watched; link".split(';'))
		self.setDatas()

	def setDatas(self):
		self.db1 = DatabaseManager.DatabaseForAll(tablename = 'manga_table')
		self.count_row = sum(1 for _ in self.db1.GetTable())
		print(self.count_row)
		self.manga_table.setRowCount(self.count_row)

		self.view_buttons = dict(enumerate([QtGui.QPushButton('Read chapter') for i in range(self.count_row + 1)]))

		for x, tup in zip(range(self.count_row+1), self.db1.GetTable()):
			for y in range(self.count_row + 1):
				if y == 0: self.manga_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[1])))
				if y == 1: self.manga_table.setItem(x, y, QtGui.QTableWidgetItem(str(tup[2])))
				if y == 2: self.manga_table.setCellWidget(x, y, self.view_buttons[x])

		for x in range(self.count_row):
			self.view_buttons[x].clicked.connect(functools.partial(self.gotoLink, x))

	def gotoLink(self, x):
		
		for i,y in enumerate(self.db1.GetTable()):
			# print(y[1])
			if x == i:
				webbrowser.open('http://mangastream.com/manga/'+str(y[1]).replace(' ', '_'))
				self.db1.updateTable(ID = int(x)+1)
				self.setDatas()
		

	### modules for buttn connections
	def seriesSearchWindow(self):

		print(self.series_lineEdit.text())
		ser = SeriesSelect.Ui_series_search(str(self.series_lineEdit.text()))
		ser.series_search.show()

	def footballSearchWindow(self):

		ball = ClubSelect.UiFootballSelect(self)
		ball.Form.show()

	def mangaSearchWindow(self):

		print(self.manga_linedit.text())
		manga = MangaSelect.UiMangaSelect(str(self.manga_linedit.text()))
		manga.Form.show()

	# def moviesSearchWindow(self):
	#     pass


	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("MainWindow", "Home", None))
		self.series_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter the series or anime", None))
		self.series_search_label.setText(_translate("MainWindow", "Search your series:", None))
		self.series_search_pushButton.setText(_translate("MainWindow", "Search", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_series), _translate("MainWindow", "Series", None))
		# self.series_search_label_3.setText(_translate("MainWindow", "Search your movie:", None))
		# self.series_lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter a movie", None))
		# self.series_search_pushButton_3.setText(_translate("MainWindow", "Search", None))
		# self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_movies), _translate("MainWindow", "Movies", None))
		self.manga_search_pushbutton.setText(_translate("MainWindow", "Search", None))
		self.manga_search_label.setText(_translate("MainWindow", "Search your manga:", None))
		self.manga_linedit.setPlaceholderText(_translate("MainWindow", "Enter your manga", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manga), _translate("MainWindow", "Manga", None))
		self.football_addteam_pushbutton.setText(_translate("MainWindow", "Add a team to follow", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_football), _translate("MainWindow", "Football", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_songs), _translate("MainWindow", "Songs", None))
		self.series_refresh.setText(_translate("MainWindow", "Refresh", None))
		self.manga_refresh.setText(_translate("MainWindow", "Refresh", None))
		self.football_refresh.setText(_translate("MainWindow", "Refresh", None))


def main():
	import sys
	app = QtGui.QApplication(sys.argv)
	a = Ui_MainWindow()
	a.MainWindow.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

