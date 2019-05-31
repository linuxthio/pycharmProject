import sys
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPen,QPainter,QBrush,QFont,QRadialGradient
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QSpinBox,QLabel


class MApp(QMainWindow):
    def __init__(self):
        super(MApp,self).__init__()
        self.setWindowTitle("PainFen")
        self.central=QWidget(self)
        self.setCentralWidget(self.central)
        self.setGeometry(200,200,600,400)
        self.setFixedSize(600,400)
        self.btnfermer=QPushButton("Fermer",self.central)
        self.btnfermer.move(10,355)
        self.btnfermer.setFont(QFont("times new roman",20))
        self.btnfermer.clicked.connect(self.fermer)
        self.rayon=100
        self.xsol=100
        self.ysol=100
        self.spinx=QSpinBox(self.central)
        self.spiny=QSpinBox(self.central)
        self.spinx.move(250,362)
        self.spiny.move(360,362)
        self.spinx.setMaximum(580)
        self.spiny.setMaximum(300)
        QLabel("rayon soleil",self.central).move(130,350)
        QLabel("x soleil",self.central).move(250,350)
        QLabel("y soleil",self.central).move(360,350)
        self.spinx.setValue(self.xsol)
        self.spinx.valueChanged.connect(self.spinch_x)
        self.spiny.setValue(self.ysol)
        self.spiny.valueChanged.connect(self.spinch_y)
        self.spin=QSpinBox(self.central)
        self.spin.move(130,362)
        self.spin.setMaximum(1000)
        self.spin.setValue(self.rayon)
        self.spin.valueChanged.connect(self.spinch)

    def spinch(self):
        self.rayon=self.spin.value()
        self.repaint()

    def spinch_x(self):
        self.xsol=self.spinx.value()
        self.repaint()

    def spinch_y(self):
        self.ysol=self.spiny.value()
        self.repaint()

    def fermer(self):
        self.close()

    def paintEvent(self, e):
        painter=QPainter(self)
        painter.setPen(QPen(Qt.black,2,Qt.SolidLine))
        painter.setFont(QFont("Arial",12))
        painter.drawRect(10,10,100,30)
        painter.drawText(12,28,"Fichier")
        painter.drawRect(120,10,100,30)
        painter.drawText(122,28,"Edition")
        painter.drawRect(230,10,100,30)
        painter.drawText(232,28,"Affichage")
        painter.drawRect(340,10,100,30)
        painter.drawText(342,28,"Help")
        painter.drawRect(10,40,580,300)
        radial=QRadialGradient(QPoint(self.xsol*2,2*self.ysol),self.rayon)
        radial.setColorAt(0.0,Qt.red)
        radial.setColorAt(0.8,Qt.yellow)
        radial.setColorAt(1.0,Qt.green)
        painter.drawText(230,400,"Djibril Thiongane :2018")
        painter.setBrush(QBrush(radial))
        painter.drawRect(15,45,570,288)

app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())



