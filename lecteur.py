# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lecteur.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 150)
        self.sldprogress = QtWidgets.QSlider(Form)
        self.sldprogress.setGeometry(QtCore.QRect(10, 80, 451, 20))
        self.sldprogress.setOrientation(QtCore.Qt.Horizontal)
        self.sldprogress.setObjectName("sldprogress")
        self.sldvolume = QtWidgets.QSlider(Form)
        self.sldvolume.setGeometry(QtCore.QRect(320, 120, 141, 20))
        self.sldvolume.setOrientation(QtCore.Qt.Horizontal)
        self.sldvolume.setObjectName("sldvolume")
        self.btnplay = QtWidgets.QPushButton(Form)
        self.btnplay.setGeometry(QtCore.QRect(90, 110, 61, 35))
        self.btnplay.setObjectName("btnplay")
        self.btnstop = QtWidgets.QPushButton(Form)
        self.btnstop.setGeometry(QtCore.QRect(160, 110, 61, 35))
        self.btnstop.setObjectName("btnstop")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setItalic(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnplay_2 = QtWidgets.QPushButton(Form)
        self.btnplay_2.setGeometry(QtCore.QRect(20, 110, 61, 35))
        self.btnplay_2.setObjectName("btnplay_2")
        self.btnplay_3 = QtWidgets.QPushButton(Form)
        self.btnplay_3.setGeometry(QtCore.QRect(230, 110, 61, 35))
        self.btnplay_3.setObjectName("btnplay_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnplay.setText(_translate("Form", "Play"))
        self.btnstop.setText(_translate("Form", "Stop"))
        self.label.setText(_translate("Form", "Super Lecteur MP3"))
        self.btnplay_2.setText(_translate("Form", "<<"))
        self.btnplay_3.setText(_translate("Form", ">>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

