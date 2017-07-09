# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(640, 480)

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.n1 = QtGui.QLCDNumber(Form)
        self.n1.setGeometry(QtCore.QRect(30, 40, 64, 23))
        self.n1.setObjectName(_fromUtf8("n1"))
        self.n2 = QtGui.QLCDNumber(Form)
        self.n2.setGeometry(QtCore.QRect(30, 90, 64, 23))
        self.n2.setObjectName(_fromUtf8("n2"))
        self.q1 = QtGui.QLabel(Form)
        self.q1.setGeometry(QtCore.QRect(50, 210, 46, 13))
        self.q1.setObjectName(_fromUtf8("q1"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.form = Form

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.q1.setText(_translate("Form", "TextLabel", None))

    def move(self, x, y):
        self.form.move(x, y)

    def resize(self, s):
        self.form.resize(*s)
