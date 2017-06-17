# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MangaSelect.ui'
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

class UiMangaSelect(QtGui.QWidget):
    def __init__(self, parent = None):
        super(UiMangaSelect, self).__init__(parent)
        self.Form = QtGui.QWidget()
        self.Form.setObjectName(_fromUtf8("Form"))
        self.Form.resize(400, 164)
        self.label = QtGui.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(60, 10, 231, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 60, 201, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.buttonBox = QtGui.QDialogButtonBox(self.Form)
        self.buttonBox.setGeometry(QtCore.QRect(90, 110, 193, 28))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Select manga", None))
        self.label.setText(_translate("Form", "From which episode you want to track:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    a = UiMangaSelect()
    a.Form.show()
    sys.exit(app.exec_())

