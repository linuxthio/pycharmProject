def t(k):
    t1=10+20*6*k
    t2=50+20*6*k
    return [t1,t2]

for i in range(6):
     print("k = ",i," t ",i+1," = ",t(i)[0]," & t ",i+2," =",t(i)[1])

for i in range(6):
     print(i,t(i))

def tt(k):
    t1=-50+20*6*k
    t2=-10+20*6*k
    return [t1,t2]

for i in range(6):
    print(i,tt(i))
