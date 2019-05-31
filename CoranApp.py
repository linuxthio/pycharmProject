from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QPushButton,QLabel,QLineEdit,QTableWidget
import sys,sqlite3

class MApp(QMainWindow):
    def __init__(self):
        super(MApp, self).__init__()
        self.w,self.h=800,600
        self.setFixedSize(self.w,self.h)
        self.setWindowTitle("Coran App")
        self.montableau=QTableWidget(self)
        r=4
        self.montableau = QTableWidget(r, 6, self)
        self.montableau.setFixedSize(self.w-20,self.h-100)
        self.montableau.move(32,32)
        lbl=QLabel(self.menu1(),self)
        lbl.setFixedSize(300,100)
        lbl.move(10,400)

    def menu1(self):
        s = "Menu\n"
        s = s + " 1 . Introduction\n"
        s = s + " 2 . sommaire\n"
        s = s + " 3 . Conclusion \n"
        return s

    def openbdd(self):
        con=sqlite3.connect("quran.db")
        cur=con.cursor()
        sql="select * from arabic_text"
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()

class Sourate:
    def __init__(self,nm,nb_ay,num_srt,):
        self.nom=nm
        self.nbr_ayat=nb_ay
        self.num_sourate=num_srt


app=QApplication(sys.argv)
f=MApp()
f.show()
sys.exit(app.exec_())





