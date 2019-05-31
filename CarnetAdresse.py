from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
import sys,sqlite3
"""
Auteur: Djibril Thiongane 
Lieu :Dakar
Date :fin septembre 2018
A propos : Carnet d'adresse ecrit avec pyqt5 et sqlite3 en utilisant pycharm2018
"""
class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.setWindowTitle("Carnet d'adresse 2018")
        self.w,self.h=600,400
        self.setFixedSize(self.w,self.h)
        self.setWindowIcon(QIcon("icons/ico1.png"))
        self.initCompenents()
        self.createBdd()
        self.remplirtab()
        #self.mettreVal()

    def initCompenents(self):
        self.lblprenom=QLabel("Prenom",self)
        self.lblprenom.move(10,10)

        self.lblnom=QLabel("Nom",self)
        self.lblnom.move(10,40)

        self.lbltel=QLabel("Tel",self)
        self.lbltel.move(10,70)

        self.editp=QLineEdit(self)
        self.editp.move(120,10)

        self.editn=QLineEdit(self)
        self.editn.move(120,40)

        self.edittel=QLineEdit(self)
        self.edittel.move(120,70)

        self.editp.setPlaceholderText("entrer prenom")
        self.editn.setPlaceholderText("entrer nom")
        self.edittel.setPlaceholderText("enter your number phone")

        self.editp.setFixedSize(200,30)
        self.editn.setFixedSize(200,30)
        self.edittel.setFixedSize(200,30)

        self.btnnew=QPushButton("Nouveau ",self)
        self.btnnew.move(10,100)
        self.btnnew.clicked.connect(self.nouveau)

        self.btnreg=QPushButton("Enrégistrer ",self)
        self.btnreg.move(120,100)
        self.btnreg.clicked.connect(self.mettreVal)

        self.btnfermer=QPushButton("Fermer ",self)
        self.btnfermer.move(220,100)
        self.btnfermer.clicked.connect(self.fermer)
        r=len(self.getDATA())
        self.montableau=QTableWidget(r,4,self)
        self.montableau.move(10,140)
        self.montableau.setFixedSize(430,240)
        self.photo=QLabel(self)
        photo=QPixmap()
        photo.load("icons/ico1.png")
        #photo.load("icons/moi.jpg")
        photo.scaled(QSize(100,155))
        self.photo.setPixmap(photo)
        self.photo.setScaledContents(True)
        mw=self.w-140
        self.photo.move(mw,20)
        self.photo.setFixedSize(120,175)
        self.auteur=QLabel("Djibril Thiongane <br>Informaticien freelance",self)
        self.auteur.move(mw,210)
        self.auteur.setFixedSize(200,100)
        self.auteur.setPalette(QPalette(QColor(245,167,40)))

    def nouveau(self):
        self.montableau.clearSpans()
        self.montableau.repaint()
    def fermer(self):
        self.close()
    def createBdd(self):
        try:
            con=sqlite3.connect("carnet.bdd")
            cur=con.cursor()
            sqlbdd="create table carnet(id integer primary key ,prenom varchar(255),nom varchar(255),tel varchar(9))"
            cur.execute(sqlbdd)
        except:
            pass

    def verifie_champ_vide(self):
        if self.editp.text().strip()=="" or self.editn.text().strip()=="" or self.edittel.text().strip()=="":
            return True
        else:
            return False

    def mettreVal(self):
        p=self.editp.text()
        n=self.editn.text()
        t=self.edittel.text()
        self.insertBdd(p,n,t)
        self.montableau.clearSpans()
        self.remplirtab()

    def remplirtab(self):
        i = 0
        self.montableau.setHorizontalHeaderLabels(["Id ","Prenom","Nom","Téléphone"])
        for e in self.getDATA():
            id=QTableWidgetItem(e.id)
            ip=QTableWidgetItem(e.prenom)
            inn=QTableWidgetItem(e.nom)
            it=QTableWidgetItem(e.tel)
            self.montableau.setItem(i,0,id)
            self.montableau.setItem(i,1,ip)
            self.montableau.setItem(i,2,inn)
            self.montableau.setItem(i,3,it)
            i=i+1
        self.montableau.updateEditorData()
        print("lecture terminer")

    def insertBdd(self,prenom,nom,tel):
        if self.verifie_champ_vide():
            print("champ vide")
            QMessageBox.information(self,"Enregistrement","Remplissez les zones de texte c'est obligatoire")
            return False
        try:
            con=sqlite3.connect("carnet.bdd")
            cur=con.cursor()
            sqlins="insert into carnet(prenom,nom,tel) values('%s','%s','%s')"%(prenom,nom,tel)
            cur.execute(sqlins)
            con.commit()
            cur.close()
            con.close()
            return "insertion reussit"
        except:
            return "donnees non inserer"

    def getDATA(self):
        con=sqlite3.connect("carnet.bdd")
        cur=con.cursor()
        cur.execute("select * from carnet")
        tout=[]
        for i in cur:
            tout.append(databdd(i[0],i[1],i[2],i[3]))
        cur.close()
        con.close()
        for i in tout:
            print(i)
        return tout


class databdd:
    def __init__(self,id,p,n,t):
        self.id=id
        self.prenom=p
        self.nom=n
        self.tel=t
    def getbdd(self):
        s=[self.id,self.prenom,self.nom,self.tel]
        return s


if __name__ == '__main__':
    app=QApplication(sys.argv)
    f=MApp()
    f.show()
    sys.exit(app.exec_())
