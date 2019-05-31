import sys
from PyQt5 import QtWidgets



def windows():
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()

    w.show()
    w.setWindowTitle("Premiere fenetre 2018")


    sys.exit(app.exec_())


windows()