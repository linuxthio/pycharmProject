# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphs.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(713, 484)
        self.form=Form
        self.id=0
        self.valzoom=0
        self.scene=QtWidgets.QGraphicsScene(Form)
        self.scene.setObjectName("scene")
        self.vue = QtWidgets.QGraphicsView(Form)
        self.vue.setScene(self.scene)
        self.vue.setGeometry(QtCore.QRect(10, 60, 511, 411))
        self.vue.setObjectName("vue")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 481, 19))
        self.label.setObjectName("label")
        self.btnzp = QtWidgets.QPushButton(Form)
        self.btnzp.setGeometry(QtCore.QRect(580, 30, 120, 35))
        self.btnzp.setObjectName("btnzp")
        self.btnzm = QtWidgets.QPushButton(Form)
        self.btnzm.setGeometry(QtCore.QRect(580, 80, 120, 35))
        self.btnzm.setObjectName("btnzm")

        self.btncercle = QtWidgets.QPushButton(Form)
        self.btncercle.setGeometry(QtCore.QRect(580, 120, 120, 35))
        self.btncercle.setObjectName("btncercle")

        self.nbcercle=1
        self.lblinfocercle=self.monlabel("lblinfocercle",580, 160, 120, 35)
        self.lblinfocercle.setText("il y'a %d cercles"%self.nbcercle)

        self.btncercle.clicked.connect(self.dessine)
        self.boul1=self.faireRond(20,20,40,QtGui.QColor(234,23,2),1)

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

    def zoomp(self):
        self.valzoom+=1

    def dessine(self):
        import random
        w,h=300,200
        r=100
        x,y,r=w*random.random(),h*random.random(),r*random.random()
        cr,cg,cb=255*random.random(),255*random.random(),255*random.random()
        #print(x,y,r,"  ",cr,cg,cb)
        self.nbcercle+=1
        self.lblinfocercle.setText("il y'a %d cercles"%self.nbcercle)
        self.faireRond(x,y,r,QtGui.QColor(cr,cg,cb),1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dessinons "))
        self.label.setText(_translate("Form", "Zone de dessin"))
        self.btnzp.setText(_translate("Form", "Zoom +"))
        self.btnzm.setText(_translate("Form", "Zoom-"))
        self.btncercle.setText(_translate("Form", "Ajouter un cercle"))

    def monlabel(self,name,x,y,w,h):
        l = QtWidgets.QLabel(self.form)
        l.setGeometry(QtCore.QRect(x,y,w,h))
        l.setObjectName(name)
        return  l


    def faireRond(self,x,y,r,coul,op):
        rond=QtWidgets.QGraphicsEllipseItem(x,y,r,r)
        rond.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        rond.setOpacity(op)
        rond.setBrush(QtGui.QBrush(coul))
        rond.setPen(QtGui.QPen(QtCore.Qt.SolidLine))
        rond.setZValue(self.id+1)
        rond.setScale(2)
        self.scene.addItem(rond)
        self.id+=1
        #print(rond.zValue())
        return rond



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

