# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClubSelect.ui'
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

class UiFootballSelect(QtGui.QWidget):
    def __init__(self, parent = None):
        super(UiFootballSelect, self).__init__(parent)
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

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Select your club", None))
        self.comboBox.setItemText(0, _translate("Form", "league placeholder", None))
        self.comboBox_2.setItemText(0, _translate("Form", "team place holder", None))
        self.label.setText(_translate("Form", "Select the league", None))
        self.label_2.setText(_translate("Form", "Select the team", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    a = UiFootballSelect()
    a.Form.show()
    sys.exit(app.exec_())

