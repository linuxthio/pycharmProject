c=0
d=0
"""
while d<10:
    print("table de ",d)
    while c<11:
        print(d," x ",c,"= ",d*c)
        c=c+1
    d=d+1
    c=0
    
"""
def multiplication(nb,limite):
    c=0
    d=0
    while d<=nb:
        print("table de ",d)
        while c<=limite:
            print(d," x ",c,"= ",d*c)
            c=c+1
        d=d+1
        c=0


#multiplication(3,10)


a,b,c,r=9,8,"fer",True


def menu():
    print("Menu")
    print(" 1 . Introduction")
    print(" 2 . sommaire")
    print(" 3 . Conclusion ")

def menu1():
    s="Menu\n"
    s=s+" 1 . Introduction\n"
    s=s+" 2 . sommaire\n"
    s=s+" 3 . Conclusion \n"
    return s


menu()
menu1()

s="je \n"
s=s+"suis\n"
s=s+"senegalais"

print(s)

def personne(prenom,nom):
    s="Prenom : "+prenom+"\n"
    s=s+"Nom :"+nom+"\n"
    print("print",s)
    return s

#a=personne("djib","thio")

print(personne("ali","ly"))
