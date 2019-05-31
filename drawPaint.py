import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QBrush,QPen
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget



class Mpain(QMainWindow):
    def __init__(self):
        super(Mpain,self).__init__()
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Peinture ")
        self.setCentralWidget(QWidget())
    def paintEvent(self, e):
        painter=QPainter(self)
        painter.setBrush(QBrush(Qt.yellow,Qt.RadialGradientPattern))
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.drawRect(0,0,600,400)
        for i in range(10):
            painter.setPen(QPen(Qt.yellow, i, Qt.SolidLine))
            painter.drawRect(20+i*10,20+i*10,100,60)
            painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
            painter.drawEllipse(200,200,10*i,10*i)

app=QApplication(sys.argv)
f=Mpain()
f.show()
sys.exit(app.exec_())