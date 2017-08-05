
import sys

from guis import mainwindow
from PyQt4 import QtGui

def main():
	
	app = QtGui.QApplication(sys.argv)
	homepage = mainwindow.Ui_MainWindow()
	homepage.MainWindow.show()
	
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

