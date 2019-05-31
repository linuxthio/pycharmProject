class Vecteur:
    def __init__(self,nom,x=0,y=0):
        self.x=x
        self.y=y
        self.nom=nom

    @staticmethod
    def hello(s):
        return s
    def hellonon(self,s="non static"):
        return s





print(Vecteur.hello("je suis la"))
print(Vecteur("vecteur OM").nom)
print(Vecteur("").hellonon())