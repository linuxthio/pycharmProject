from PyQt5.QtCore import QDate,QTime ,QDateTime,Qt,QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QFont
import sys
"""
d=QTime.currentTime()
print(d.toString(Qt.ISODate))
print(d.toString(Qt.DefaultLocaleShortDate))
"""
class Mainw(QMainWindow):
    def __init__(self):
        super(Mainw, self).__init__()
        self.arret = False
        self.setWindowTitle("Horloge pyQt5")
        self.resize(200,100)
        self.central=QWidget()
        self.setCentralWidget(self.central)
        self.aff=QLabel("<h4 style='color:red;'>%s</h4>"%QTime.currentTime().toString(),self.central)
        self.aff.move(2,2)
        self.uptemp=QTimer()
        self.uptemp.timeout.connect(self.settime)
        self.uptemp.start(1000)
        self.aff.setFont(QFont("Arial",32))
        self.setFixedSize(200,100)
        self.neww=QPushButton("Pause",self)
        self.neww.move(2,60)
        self.neww.clicked.connect(self.nouveau)
    def nouveau(self):
        if not self.arret:
            self.uptemp.stop()
            self.arret=True
            self.neww.setText("Activer")
        else:
            self.uptemp.start()
            self.arret=False
            self.neww.setText("Pause")
    def settime(self):
        self.aff.setText("<h4 style='color:red;'>%s</h4>"%QTime.currentTime().toString())

app=QApplication(sys.argv)
f=Mainw()
f.show()
sys.exit(app.exec_())
