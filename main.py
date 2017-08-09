
import sys

from guis import mainwindow, login
from PyQt4 import QtGui

def main():
	
	app = QtGui.QApplication(sys.argv)
	
	homepage = mainwindow.Ui_MainWindow()
	homepage.MainWindow.show()
	
	# ex = login.Ui_Login()
	# ex.show()
	

	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

