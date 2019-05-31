from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox,QPushButton
from  PyQt5.QtCore import QMetaObject,pyqtSlot
import sys

class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.btnok=QPushButton("Ok",self)
        self.btnok.setObjectName("btnok")
        QMetaObject.connectSlotsByName(self)
        self.setFixedSize(300,200)
        self.setWindowTitle("slot and signal")
        self.btnok.clicked.connect(self.slot1)
        self.btnok.clicked.connect(self.slot2)

    def slot1(self):
        QMessageBox.information(self,"Slot 1","je suis le premier SLOt")

    def slot2(self):
        QMessageBox.information(self,"Slot 2","je suis le deuxieme SLOt")

    @pyqtSlot()
    def on_btnok_clicked(self):
        QMessageBox.information(self,"info ","un slot ameliorer")




app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())


