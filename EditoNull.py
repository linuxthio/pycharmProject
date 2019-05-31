import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QColor,QPalette,QIcon
from PyQt5.QtWidgets import QMessageBox,QWidget,QFileDialog,QColorDialog,QFontDialog,QApplication,QPushButton,QLabel,QLineEdit,QPlainTextEdit,QMainWindow,QAction
"""
Auteur :Djibril Thiongane  Lieu : Yeumbeul Layenne Dakar Date : septembre 2018 Version : 1.0.18
"""
class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.setWindowTitle("EditoNull 2018")
        self.w,self.h=900,400
        self.setFixedSize(self.w,self.h)
        self.setGeometry(300,90,self.w,self.h)
        self.setPalette(QPalette(QColor(193,193,243)))
        self.initWin()
    def fermerapp(self):
        self.close()
    def initWin(self):
        menubar=self.menuBar()
        filemn=menubar.addMenu("Fichier")
        editMenu=menubar.addMenu("Edition")
        helpMenu=menubar.addMenu("Help")
        self.toolbar=self.addToolBar('ToolBar')
        ouvreAct=QAction(QIcon('icons/ico1.png'),"Ouvrir",self)
        self.toolbar.addAction(ouvreAct)
        self.addAction(ouvreAct)
        self.edition=QPlainTextEdit(self)
        self.edition.move(5,60)
        self.edition.setFixedSize(self.w-10,self.h-100)
        self.font=QFont("Arial",12)
        self.edition.setFont(self.font)
        self.btnfont=QPushButton("Police ...",self)
        self.btnfont.move(220,self.h-35)
        self.btnfont.clicked.connect(self.myfont)
        self.reg=QPushButton("Enregistrer",self)
        self.reg.move(120,self.h-35)
        self.reg.clicked.connect(self.regme)
        self.auteur=QLabel('Djibril Thiongane <img src="icons/ico1.png" width="60px"/>',self)
        self.auteur.move(self.w-120,self.h-25)
        self.auteur.setWindowOpacity(.1)
        self.auteur.setPalette(QPalette(QColor(34,4,109)))
        self.auteur.setFixedSize(310,30)
        self.op=QPushButton("Ouvrir",self)
        self.op.move(20,self.h-35)
        self.op.clicked.connect(self.openme)

        #self.btnforeground=QPushButton("Couleur Text",self)
        self.btnbackground=QPushButton("Couleur fond",self)

        #self.btnforeground.move(420,self.h-35)
        self.btnbackground.move(320,self.h-35)

        #self.btnforeground.clicked.connect(self.fore)
        self.btnbackground.clicked.connect(self.back)

        self.fermer=QPushButton("X",self)
        self.fermer.move(self.w-40,self.h-40)
        self.fermer.setPalette(QPalette(QColor(233,23,23,233)))
        self.fermer.setToolTip("Fermer l'app")
        self.fermer.setFixedSize(40,20)
        self.fermer.clicked.connect(self.fermerapp)

    def openme(self):
        try:
            opendial=QFileDialog()
            filename=opendial.getOpenFileName()
            with open(filename[0],"r") as f:
                self.edition.setPlainText(f.read())
        except:
            pass

    def back(self):
            self.setPalette(QPalette(QColorDialog.getColor()))
            self.repaint()

    def myfont(self):
        try:
            #self.font=QFontDialog()
            self.edition.setFont(QFontDialog.getFont()[0])
            self.edition.repaint()
        except:
            pass

    def regme(self):
        try:
            regdialog=QFileDialog()
            filename=regdialog.getSaveFileName()
            with open(filename[0],"w") as f:
                f.write(self.edition.toPlainText())
            QMessageBox.information(self,"Enregistrement ","Le fichier %s a ete bien enregistrer"%filename[0])
        except:
            pass

app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())