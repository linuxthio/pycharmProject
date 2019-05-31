class Vecteur:
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def addition(self,v):
        self.x=self.x+v.x
        self.y=self.y+v.y
        self.z=self.z+v.z

    def toString(self):
        return "x=%d,y=%d,z=%d"%(self.x,self.y,self.z)


ab=Vecteur(23,22,231)
ab.addition(Vecteur(34,2,1))
print(ab.toString())

