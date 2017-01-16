# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import des
import hashlib


def md5(s):
    m = hashlib.md5()
    m.update(s.encode(encoding="utf-8"))
    s = int('0x' + m.hexdigest()[0: 32], 16)
    return bin(s).replace('0b','').zfill(128)



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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(960, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/statsic/stastic/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/bg_main.png);"))
        #MainWindow.setIconSize(QtCore.QSize(55, 55))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ob_input = QtGui.QPlainTextEdit(self.centralwidget)
        self.ob_input.setGeometry(QtCore.QRect(200, 150, 230, 90))
        self.ob_input.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/bg_text.png);"))
        self.ob_input.setDocumentTitle(_fromUtf8(""))
        self.ob_input.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.ob_input.setBackgroundVisible(False)
        self.ob_input.setCenterOnScroll(False)
        #self.ob_input.setPlaceholderText(_fromUtf8(""))
        self.ob_input.setObjectName(_fromUtf8("ob_input"))
        self.ob_key = QtGui.QPlainTextEdit(self.centralwidget)
        self.ob_key.setGeometry(QtCore.QRect(530, 150, 230, 90))
        self.ob_key.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/bg_text.png);"))
        self.ob_key.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.ob_key.setObjectName(_fromUtf8("ob_key"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 280, 120, 50))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/btn_en.png);"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 280, 120, 50))
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/btn_de.png);"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.ob_output = QtGui.QPlainTextEdit(self.centralwidget)
        self.ob_output.setGeometry(QtCore.QRect(290, 370, 391, 87))
        self.ob_output.setStyleSheet(_fromUtf8("border-image: url(:/statsic/stastic/bg_text.png);"))
        self.ob_output.setReadOnly(True)
        self.ob_output.setObjectName(_fromUtf8("ob_output"))
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Enc)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.Dec)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "3DES加解密程序", None))


    def Enc(self):
        inputvalue = ''
        inputvalue0 = str(self.ob_input.toPlainText())
        for i in inputvalue0:
            inputvalue = inputvalue + bin(ord(i)).replace('0b','').zfill(8)
        key = md5(str(self.ob_key.toPlainText()))
        outputvalue = ''
        while len(inputvalue) > 64:
            outputvalue = outputvalue + des.ThreeDESencrypt(inputvalue[0:64], key)
            inputvalue = inputvalue[64:]
        outputvalue = outputvalue + inputvalue
        self.ob_output.setPlainText(outputvalue)


    def Dec(self):
        outputvalue = ''
        inputvalue = str(self.ob_input.toPlainText())
        key = md5(str(self.ob_key.toPlainText()))
        outputvalue0 = ''
        while len(inputvalue) > 64:
            outputvalue0 = outputvalue0 + des.ThreeDESdecrypt(inputvalue[0:64], key)
            inputvalue = inputvalue[64:]
        outputvalue0 = outputvalue0 + inputvalue
        for i in range(0, len(outputvalue0), 8):
            outputvalue = outputvalue + chr(int(outputvalue0[i: i+8], 2))
        self.ob_output.setPlainText(outputvalue)

import interface_rc
