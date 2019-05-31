from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
import sys



import sqlite3
"""
auteur :djibril thiongane
date : 04 10 2018
lieu : thies / dakar
"""
dico=['accepter','acheter','aider','aimer',	"ajouter",'appeler','apporter','approcher','appuyer','arrêter','arriver','assurer','avancer','briller','brûler','cacher','calmer','causer','cesser','changer','chanter','charger','chercher','clamer','commencer','compter','continuer','coucher','crier	','décider','demander','deviner','donner','écouter','élever','embrasser','emporter','entrer','envoyer','espérer','essayer','exister','expliquer','exprimer','fermer','former','frapper','gagner','garder','glisser','jeter','jouer','juger','lever','manger','manquer','marcher','monter','montrer','nommer','occuper','oublier','parler','passer','payer','penser','placer','pleure','porter','poser','posséder','pousser','préparer','présenter','prier','prononcer','quitter','raconter','rappeler','refuser','regarder','rencontrer','rentrer','répéter','ressembler','rester','retourner','retrouver','rêver','rouler','sauver','sembler','tirer','tomber','torturer','toucher','tourner','travailler','traverser','tromper','trouver','tuer','voiler','voler','voyager'];
pronom=["je","tu","il","elle","nous","vous","ils","elles"]
terminaison=["e","es","e","e","ons","ez","ent","ent"]
terminaison_eter=["te","tes","te","te","ons","ez","tent","tent"]
terminaison_eler=["le","les","le","le","ons","ez","lent","lent"]
terminaison_yer=["ie","ies","ie","ie","yons","yez","ient","ient"]

class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.setWindowIcon(QIcon("icons/ico2.png"))
        self.setWindowTitle("Conjugaison 2018")
        self.w,self.h=400,550
        self.setFixedSize(self.w,self.h)
        self.filename="verbe.bdd"
        self.dobdd()
        self.lblverbe=QLabel("Verbe ",self)
        self.lblverbe.move(10,10)
        self.txtverbe=QLineEdit(self)
        self.txtverbe.move(120,10)
        self.txtverbe.setFixedSize(200,25)
        self.btnreg=QPushButton("Enregistrer",self)
        self.btnreg.move(10,60)
        self.btnreg.clicked.connect(self.txt_to_bd)
        self.lbl_nb_verbe=QLabel(self)
        self.lbl_nb_verbe.move(130,60)
        r=len(self.nbr_verbe())
        self.lbl_nb_verbe.setText("Total : {}".format(len(self.nbr_verbe())))
        self.montableau=QTableWidget(r,2,self)
        self.montableau.move(10,100)
        self.montableau.setFixedSize(300,self.h-100)
        self.remplirtab()
        self.btnfermer=QPushButton("Fermer",self)
        self.btnfermer.move(260,60)
        self.btnfermer.clicked.connect(self.fermer)
        self.moi=QLabel(self)
        self.moi.setPixmap(QPixmap("icons/moi.jpg"))
        self.moi.move(self.w-80,self.h-70)
        self.moi.setScaledContents(True)
        self.moi.setFixedSize(60,70)


    def fermer(self):
        ok=QMessageBox.question(self,"Fermeture  ","vous voulez quitter")
        if ok==QMessageBox.Yes:
            QMessageBox.information(self,"Bye ","Bye Bye !!!!!!!")
            self.close()
    def nbr_verbe(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("select * from verbes ")
        vb=[]
        for c in cur:
            vb.append(c[1])
        cur.close()
        con.close()
        return vb

    def remplirtab(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("select * from verbes ")
        vb=[]
        for c in cur:
            vb.append(c[1])
        cur.close()
        con.close()
        id=0
        vb.sort()
        self.montableau.setHorizontalHeaderLabels(["Numero","Verbes"])
        for v in vb:
            tid = QTableWidgetItem("{0}".format(id+1))
            tvb = QTableWidgetItem(v)
            self.montableau.setItem(id, 0, tid)
            self.montableau.setItem(id, 1, tvb)
            id = id + 1

    def txt_to_bd(self):
        verbe=self.txtverbe.text()
        if verbe.strip()=="":
            QMessageBox.information(self,"Manque de donnees","Entrer un verbe dans la zone de texte")
        else:
            self.insereVerbe(verbe)
            self.montableau.setRowCount(len(self.nbr_verbe()))
            self.remplirtab()
            self.txtverbe.setText("")
            self.lbl_nb_verbe.setText("Total : {}".format(len(self.nbr_verbe())))
        self.txtverbe.setFocus(Qt.OtherFocusReason)

    def dobdd(self):
        try:
            con=sqlite3.connect(self.filename)
            cur=con.cursor()
            sql="create table verbes(id integer primary key autoincrement,verbe varchar(255) , groupe integer )"
            cur.execute(sql)
            cur.close()
            con.close()
            self.exportverbe()
        except:
            pass

    def isvalide(self):
        verbe=self.txtverbe.text()
        ponct=".,/?';:!@#$%&*(){-_}+=][><0123456789"
        for p in ponct:
            if p in verbe:
                QMessageBox.information(self,"Caratere speciaux","Pas de caratere speciaux ni de ponctuation ni de chiffres")
                return False
        term = verbe[(len(verbe) - 2):len(verbe)]
        if (len(verbe) < 4):
            QMessageBox.information(self,"Mot court","un verbe du premier groupe contient plus de trois lettres")
            return False
        elif (len(verbe.split(' ')) > 1):
            QMessageBox.information(self,"Validation","pas d'espace dans un verbe")
            return False
        else:
            if (term != "er"):
                QMessageBox.information(self,"Existence","Ce n'est pas un verbe du premier groupe car la terminaison  (" + term + ") est different de 'er'")
                return False
        return True

    def insereVerbe(self,verbe,grp=1):
        if self.isvalide():
            if self.isverbe_exist(verbe):
                QMessageBox.information(self,"Verbe ","Ce verbe <<{0}>>existe dans la base de donnée".format(verbe))
            else:
                con = sqlite3.connect(self.filename)
                cur = con.cursor()
                sql="insert into verbes(verbe,groupe) values('{0}','1')".format(verbe)
                cur.execute(sql)
                con.commit()
                cur.close()
                con.close()

    def isverbe_exist(self,verbe):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        cur.execute("select * from verbes ")
        vb=[]
        for c in cur:
            vb.append(c[1])
        cur.close()
        con.close()
        if verbe in vb:
            return True
        else:
            return False

    def exportverbe(self):
        con = sqlite3.connect(self.filename)
        cur = con.cursor()
        for v in dico:
            sql="insert into verbes(verbe ,groupe) values('{0}' , '1')".format(v)
            cur.execute(sql)
        con.commit()
        cur.close()
        con.close()

    def sync_bd(self,bd):
        con2=sqlite3.connect(bd)
        cur2=con2.cursor()
        con=sqlite3.connect(self.filename)
        cur=con.cursor()




app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())