t = [-10,-8,0,1,2,5,-2,-4]

maior = t[0]
menor = t[0]
soma = 0
x = 0  
for e in t :
    if ( e > maior):
        maior = e
    elif e < menor :
        menor = e 
    soma = soma + e 
    x+=1

print("MAIOR: %d\nMENOR: %d\nMEDIA: %f"%(maior,menor,soma/x))  