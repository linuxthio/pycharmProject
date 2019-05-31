from PyQt5.QtWidgets import *
import sys,sqlite3
from PyQt5.QtCore import QDate,QTime ,QDateTime,Qt,QTimer,QUrl
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtMultimedia import *
from pygame.locals import *
"""
14/10/2018 a thies

"""
class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.table_reveil=[]
        self.filename="reveil.bd"
        self.total=0
        self.sonplayed=False
        self.creerBd()
        self.inittime()
        self.initCompenent()
        self.affiche()
    def initCompenent(self):
        self.w,self.h=700,300
        self.ecran=QLabel("",self)
        self.lblh=QLabel("h",self)
        self.lblm=QLabel("m",self)
        self.lbls=QLabel("s",self)
        self.ecran.setFixedSize(self.w-60,60)
        self.ecran.move(30,5)
        self.ecran.setFont(QFont("arial",32))
        wsp,hsp=30,30
        xlb=20
        ylb=60
        self.nbrmin=0
        self.lblh.move(xlb+xlb+wsp,ylb)
        self.lblm.move(2*xlb+xlb+wsp+50,ylb)
        self.lbls.move(4*xlb+xlb+wsp+90,ylb)

        self.sph=QSpinBox(self)
        self.spm=QSpinBox(self)
        self.sps=QSpinBox(self)
        self.sph.setMaximum(23)
        self.spm.setMaximum(59)
        self.sps.setMaximum(59)

        self.sph.setFixedSize(40,30)
        self.spm.setFixedSize(40,30)
        self.sps.setFixedSize(40,30)

        self.sph.move(xlb,ylb)
        self.spm.move(xlb+xlb+wsp+25,ylb)
        self.sps.move(xlb+2*(xlb+wsp+25),ylb)

        self.btncreer=QPushButton("Creer",self)
        self.btncreer.move(2*xlb+4*(xlb+wsp+5),ylb)
        r=self.gettotal()
        self.montableau = QTableWidget(r, 6, self)
        self.montableau.setFixedSize(self.w-20,self.h-100)
        self.montableau.move(xlb,1.6*ylb)
        self.settime()

        self.uptemp=QTimer()
        self.uptemp.timeout.connect(self.settime)
        self.uptemp.start(1000)

        self.il_est_heur=QTimer()
        self.il_est_heur.timeout.connect(self.ilestlheur)
        self.il_est_heur.start(60000)
        self.btncreer.clicked.connect(self.btninser)

        self.setWindowIcon(QIcon("icons/ico2.png"))
        self.setGeometry(300,200,self.w,self.h)
        self.setFixedSize(self.w,self.h)

    def settime(self):
        self.ecran.setText("<h4 style='color:red;'>%s</h4>"%QTime.currentTime().toString())
        self.estceHeure2()

    def ilestlheur(self):
        self.nbrmin+=1
        self.inittime()
        self.setWindowTitle("# %d ## %d : %d : %d "%(self.nbrmin,self.heur,self.minute,self.second))
        #self.estceHeure()

    def inittime(self):
        self.heur=QTime.currentTime().hour()
        self.minute=QTime.currentTime().minute()
        self.second=QTime.currentTime().second()

    def creerBd(self):
        try:
            con=sqlite3.connect(self.filename)
            cur=con.cursor()
            sql="create table lesreveil(id integer primary key autoincrement ,h integer,m integer ,s integer ,nom varchar(255),etat integer)"
            cur.execute(sql)
            con.commit()
            cur.close()
            con.close()
        except:
            pass

    def gettotal(self):
        con=sqlite3.connect(self.filename)
        cur=con.cursor()
        sql="select * from lesreveil"
        cur.execute(sql)
        id=0
        for c in cur:
            id=id+1
        self.total=id
        cur.close()
        con.close()
        return  id

    def affiche(self):
        con=sqlite3.connect(self.filename)
        cur=con.cursor()
        sql="select * from lesreveil"
        cur.execute(sql)
        self.table_reveil=[]
        for c in cur:
            self.table_reveil.append(Reveil(c[1],c[2],c[3],c[4],c[5]))
            print(c)
        id=0
        print(cur)
        print(self.table_reveil)
        #"""
        cur.close()
        con.close()
        self.montableau.setHorizontalHeaderLabels(["id","h","m","s","nom","etat"])
        for s in self.table_reveil:
            i=QTableWidgetItem("%d"%id)
            h=QTableWidgetItem("%d"%s.h)
            m=QTableWidgetItem("%d"%s.m)
            ss=QTableWidgetItem("%d"%s.s)
            nom=QTableWidgetItem(s.nom)
            etat=QTableWidgetItem("%d"%s.etat)

            self.montableau.setItem(id,0,i)
            self.montableau.setItem(id,1,h)
            self.montableau.setItem(id,2,m)
            self.montableau.setItem(id,3,ss)
            self.montableau.setItem(id,4,nom)
            self.montableau.setItem(id,5,etat)
            id = id + 1
        #"""
        self.total=len(self.table_reveil)
    def insereData(self):
        con=sqlite3.connect(self.filename)
        cur=con.cursor()
        num=self.total
        sql="insert into lesreveil(h,m,s,nom,etat) values('{0}','{1}','{2}','{3}','0')".format(self.sph.value(),self.spm.value(),self.sps.value(),"reveil %d"%num)
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
        self.total=self.total+1
    def btninser(self):
        self.insereData()
        self.montableau.setRowCount(self.gettotal())
        self.affiche()
    def playgame(self):
        import pygame.mixer
        pygame.mixer.init()
        sound = pygame.mixer.music.load("son/06.mp3")
        pygame.mixer.music.play()

    def playkivy(self):
        pass
        """
        from kivy.core.audio import SoundLoader
        s=SoundLoader.load("son/06.mp3")
        s.play()
        """
    def isExist(self,h,m,s,h1,m1,s1):
        if h==h1 and m==m1 and s==s1:
            print("True : {0}  {1}  {2}  {3}  {4}  {5} ".format(h,m,s,h1,m1,s1))
            return True
        else:
            print("False : {0}  {1}  {2}  {3}  {4}  {5} ".format(h,m,s,h1,m1,s1))
            return  False


    def playsonnerie(self):
        son=QMediaPlayer()
        son.setMedia(QMediaContent(QUrl.fromLocalFile("son/06.mp3")))
        son.setVolume(50)

        son.play()
        self.sonplayed=True
    def estceHeure(self):
        con=sqlite3.connect(self.filename)
        cur=con.cursor()
        sql="select * from lesreveil"
        cur.execute(sql)
        id=0

        for c in cur:
            if self.isExist(self.sph.value(),self.spm.value(),self.sps.value(),int(c[1]),int(c[2]),int(c[3])):
                if  self.sonplayed==False:
                    self.playgame()
                    self.sonplayed=True

        self.total=id
        cur.close()
        con.close()
        return  id
    def estceHeure2(self):
        con=sqlite3.connect(self.filename)
        cur=con.cursor()
        sql="select * from lesreveil"
        cur.execute(sql)
        id=0

        for c in cur:
            if self.isExist(self.sph.value(),self.spm.value(),int(c[3]),int(c[1]),int(c[2]),int(c[3])):
                if  self.sonplayed==False:
                    self.playgame()
                    self.sonplayed=True

        self.total=id
        cur.close()
        con.close()
        return  id


class Reveil:
    num=0
    def __init__(self,h=0,m=0,s=0,nom="reveil %d"%num,etat=0):
        self.h=h
        self.m=m
        self.s=s
        self.etat=etat
        self.nom=nom
        Reveil.num=Reveil.num+1
    @staticmethod
    def isExist(h,m,s,h1,m1,s1):
        if h==h1 and m==m1 and s==s1:
            return True
        else:
            return  False


app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())

