# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClubSelect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

##########################
from cores import football
import functools
import itertools

##########################

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

class UiFootballSelect(QtGui.QWidget):
    def __init__(self, parent = None):
        
        super(UiFootballSelect, self).__init__(parent)

        #######################
        self.fromFootball = football.Footy()
        #######################
        
        self.Form = QtGui.QWidget()
        self.Form.setObjectName(_fromUtf8("Form"))
        self.Form.resize(590, 358)
        self.comboBox = QtGui.QComboBox(self.Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 60, 141, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.Form)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 60, 181, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.graphicsView = QtGui.QGraphicsView(self.Form)
        self.graphicsView.setGeometry(QtCore.QRect(170, 100, 256, 192))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(120, 40, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.buttonBox = QtGui.QDialogButtonBox(self.Form)
        self.buttonBox.setGeometry(QtCore.QRect(190, 310, 193, 28))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.setCombos()

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def setCombos(self):
        for x in self.fromFootball.Competition(season = 2017):
            print(str(x['name']))
            self.comboBox.addItem(str(x['name']))
        self.comboBox.activated.connect(self.setCombo2)

    def setCombo2(self, x):
        num = self.comboBox.findText(str(self.comboBox.currentText()))
        league_id = next(itertools.islice(self.fromFootball.Competition(season = 2017), num - 1, None))['id']

        for x in self.fromFootball.CompetitionTeams(league_id = league_id):
            self.comboBox_2.addItem(str(x['name']))

        self.comboBox_2.activated.connect(functools.partial(self.foo, league_id))

    def foo(self, league_id):
        num2 = self.comboBox_2.findText(str(self.comboBox_2.currentText()))
        team_id = next(itertools.islice(self.fromFootball.CompetitionTeams(league_id = league_id), num2 - 1, None))

        print(num2)
        print(team_id)





    def retranslateUi(self, Form):
        
        Form.setWindowTitle(_translate("Form", "Select your club", None))
        self.label.setText(_translate("Form", "Select the league", None))
        self.label_2.setText(_translate("Form", "Select the team", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    a = UiFootballSelect()
    a.Form.show()
    sys.exit(app.exec_())



