from PyQt5.QtWidgets import QApplication,QWidget,QComboBox,QMainWindow,QPushButton,QLineEdit,QLabel
import sys

class Mapp(QMainWindow):
    def __init__(self):
        super(Mapp, self).__init__()
        self.central=QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle("Combobox 2018")
        self.setFixedSize(400,200)
        self.setGeometry(400,200,300,200)
        self.com=QComboBox(self.central)
        self.dico=["senegal","gambie","mali"]
        self.result=QLabel("Resultat",self.central)
        self.result.move(120,100)
        self.result.setFixedSize(200,30)
        self.btn=QPushButton("Ajouter un item ",self.central)
        self.btn.move(120,60)
        self.zone=QLineEdit(self.central)
        self.zone.move(120,20)
        self.btn.clicked.connect(self.ajout)
        self.com.activated.connect(self.lblres)
        self.com.move(20,20)
        self.ajout()
    def ajout(self):
        mot=self.zone.text()
        if mot.strip()=="":
            pass
        else:
            if mot.lower() in self.dico:
                self.zone.setText("")
                pass
            else:
                self.dico.append(mot.lower())
        self.com.clear()

        for c in self.dico:
            self.com.addItem(c.capitalize())
    def lblres(self):
        self.result.setText(self.com.currentText())



app=QApplication(sys.argv)

f=Mapp()
f.show()

sys.exit(app.exec_())
