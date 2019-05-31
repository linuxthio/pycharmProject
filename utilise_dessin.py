from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QMainWindow
from dessin import Ui_Form
import sys

class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        self.autre=QLabel(self)
        self.autre.setText("Bonjour monlabel okk")
        self.autre.move(550,200)
        self.autre.setFixedWidth(200)
        print("autre ",self.autre.text())



app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())
