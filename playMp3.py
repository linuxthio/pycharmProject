import pygame
import pygame.mixer as mus
from PyQt5 import QtCore, QtGui, QtWidgets

"""
Auteur : Djibril Thiongane 
Date : Nuit du Vendredi 09/11/2018 
Lieu : Thies

"""

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(470, 180)
        self.tabmp3=["../son/03.mp3","../son/05.mp3","../son/06.mp3","../son/08.mp3","../son/09.mp3"]
        self.id=0
        mus.init()
        self.entrain=False
        self.log1=self.logo("img1.jpg",200,10,100,100)

        self.sldprogress = QtWidgets.QSlider(Form)
        self.sldprogress.setGeometry(QtCore.QRect(10, 80, 451, 20))
        self.sldprogress.setOrientation(QtCore.Qt.Horizontal)
        self.sldprogress.setObjectName("sldprogress")
        self.sldvolume = QtWidgets.QSlider(Form)
        self.sldvolume.setGeometry(QtCore.QRect(320, 120, 141, 20))
        self.sldvolume.setOrientation(QtCore.Qt.Horizontal)
        self.sldvolume.setMinimum(0)
        self.sldvolume.setMaximum(150)

        self.sldvolume.setObjectName("sldvolume")
        self.btnplay = QtWidgets.QPushButton(Form)
        self.btnplay.setGeometry(QtCore.QRect(90, 110, 61, 35))
        self.btnplay.setObjectName("btnplay")
        self.btnstop = QtWidgets.QPushButton(Form)
        self.btnstop.setGeometry(QtCore.QRect(160, 110, 61, 35))
        self.btnstop.setObjectName("btnstop")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 60))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setItalic(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.btnopen = QtWidgets.QPushButton(Form)
        self.btnopen.setGeometry(QtCore.QRect(380, 30, 80, 35))
        self.btnopen.setObjectName("btnopen")
        self.btnopen.clicked.connect(self.openFile)


        self.lblnom = QtWidgets.QLabel(Form)
        self.lblnom.setGeometry(QtCore.QRect(10, 40, 400, 60))
        self.lblnom.setObjectName("lblnom")
        font = QtGui.QFont()
        #font.setPointSize(21)
        font.setItalic(True)
        font.setKerning(True)
        self.lblnom.setFont(font)

        self.lblauteur = QtWidgets.QLabel(Form)
        self.lblauteur.setGeometry(QtCore.QRect(470/2-60, 140, 130, 60))
        self.lblauteur.setObjectName("lblauteur")

        self.btnrecule = QtWidgets.QPushButton(Form)
        self.btnrecule.setGeometry(QtCore.QRect(20, 110, 61, 35))
        self.btnrecule.setObjectName("btnrecule")
        self.btnavance = QtWidgets.QPushButton(Form)
        self.btnavance.setGeometry(QtCore.QRect(230, 110, 61, 35))
        self.btnavance.setObjectName("btnavance")

        self.uptemp=QtCore.QTimer()
        self.uptemp.timeout.connect(self.setprogress_marche_pas)
        #self.uptemp.timeout.connect(self.setprogress)
        self.uptemp.start(100)

        self.btnstop.clicked.connect(self.stopmp3)
        self.btnplay.clicked.connect(self.playmp3)
        self.btnrecule.clicked.connect(self.recule)
        self.btnavance.clicked.connect(self.avance)
        mus.music.set_volume(0.3)
        self.sldvolume.setValue(mus.music.get_volume()*100)
        self.sldvolume.valueChanged.connect(lambda x:mus.music.set_volume(self.sldvolume.value()/100))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def logo(self,filename,x,y,w,h):
        f=QtWidgets.QLabel(Form)
        photo=QtGui.QPixmap()
        photo.load(filename)
        photo.scaled(QtCore.QSize(w,h))
        f.setPixmap(photo)
        f.setScaledContents(True)
        f.move(x,y)
        f.setFixedSize(w,h)
        return f

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PlayMp3 "))
        self.btnplay.setText(_translate("Form", "Play"))
        self.btnstop.setText(_translate("Form", "Stop"))
        self.btnopen.setText(_translate("Form", "Open File"))
        self.label.setText(_translate("Form", "Super Lecteur MP3"))
        self.lblnom.setText(_translate("Form",self.tabmp3[self.id]))
        self.lblauteur.setText(_translate("Form","Djibril Thiongane"))
        self.btnrecule.setText(_translate("Form", "<<"))
        self.btnavance.setText(_translate("Form", ">>"))

    def openFile(self):
        """
        appeler qfilechooser
        recupere le filename
        ajouter le filename dans tabmp3
        donner self.id la position du filename   len(tabmp3)-2
        appeler playmp3
        """
        try:
            opendial = QtWidgets.QFileDialog()
            filename = opendial.getOpenFileName()
            self.tabmp3.append(filename[0])
            self.id=len(self.tabmp3)-1
            self.playmp3()
        except:
            pass
    def setprogress_marche_pas(self):
        try:
            #mus.Sound(self.tabmp3[self.id])
            #self.sldprogress.setMaximum(mus.Sound.get_length())
            print("sommes dans try ......")

            p=QtMultimedia.QMediaPlayer(Form)
            p.setMedia(QtCore.QUrl.fromLocalFile(self.tabmp3[self.id]))
            dur=p.duration()
            self.sldprogress.setMaximum(dur)
            print("duree",dur)
        except:
            pass

        #self.sldprogress.setMaximum(600000)
        self.sldprogress.setValue(mus.music.get_pos())
        #print(mus.music.get_pos())
    def setprogress(self):
        if self.entrain:
            self.sldprogress.setValue(mus.music.get_pos())
        else:
            self.sldprogress.setValue(0)
        self.sldprogress.setMaximum(self.getduration())
        print(self.getduration())
        #self.sldprogress.setMaximum(600000)

    def getduration(self):
        import os
        #os.chdir(foo)  # Get into the dir with sound
        statbuf = os.stat(self.tabmp3[self.id])
        print(statbuf)
        mbytes = statbuf.st_size / 1024
        duration = mbytes #/ 200
        return duration*170

    def findlen(self):
        n=0
        i=0
        while 1:
            try:
                mus.music.se
                n+=1
                i+=1
            except:
                mus.music.rewind()
                pass
        return n

    def playmp3(self):
        mus.music.load(self.tabmp3[self.id])
        mus.music.play()
        self.entrain=True
        self.retranslateUi(Form)
        #print(self.findlen())

    def stopmp3(self):
        mus.music.rewind()
        mus.music.stop()
        self.entrain=False
    def recule(self):
        if self.id>0:
            self.id-=1
            mus.music.load(self.tabmp3[self.id])
            self.playmp3()
            self.retranslateUi(Form)

    def avance(self):
        # si len(tabmp3)=4 et self.id=3 on ne peut pas jaouter id car l'indice max est 4-1=3
        # on incremente id si id < (4-1)-1 donc id< 4-2
        if self.id<len(self.tabmp3)-2:
            self.id+=1
            mus.music.load(self.tabmp3[self.id])
            self.playmp3()
            self.retranslateUi(Form)
        else:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())