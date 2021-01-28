l=[15,7,27,39]

p = int(input("DIGITE O VALOR A PROCURAR: "))
v = int(input("DIGITE OUTRO VALOR A PROCURAR: "))
x = 0 
achoup = False
achouv = False
auxp =-1
auxv =-1
while x<len(l):
    if l[x]==p:
        achoup = True
        auxp= x 
    if l[x]==v:
        achouv = True
        auxv = x
    x=x+1
if auxp < auxv and achouv and achoup :
    print(" %d encontrado primeiro na posição %d"%(p,auxp))
    print("%d achado na posição %d"%(v,auxv))     
elif auxp > auxv and achouv and achoup :
    print("%d encontrado primeiro na posição %d"%(v,auxv))
    print("%d achado na posição %d"%(p,auxp))
      