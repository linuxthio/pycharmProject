from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QTreeView,QDirModel,QMainWindow


class Mapp(QMainWindow):
    def __init__(self):
        super(Mapp, self).__init__()
        self.dir=QDirModel(self)
        self.tree=QTreeView(self)
        self.tree.setModel(self.dir)
        w,h=800,600
        r=30
        self.tree.setFixedSize(w-r,h-r)
        self.tree.move(10,10)
        self.setFixedSize(w,h)
        self.tree.clicked.connect(self.montre)

    def montre(self):
        pass

        #self.setWindowTitle("%d"%self.tree.currentIndex())


import sys
app=QApplication(sys.argv)
f=Mapp()
f.show()
sys.exit(app.exec_())