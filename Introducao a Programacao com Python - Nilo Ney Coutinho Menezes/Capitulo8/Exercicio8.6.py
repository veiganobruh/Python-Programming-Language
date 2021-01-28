def Soma ( lista ):
    soma = 0 
    for i, e in enumerate(lista):
        soma +=lista[i] 
    
    return soma 
def Maximo( lista):
    maximo = lista[0]
  
    for i,e in enumerate(lista):
        if e> maximo:
            maximo = lista[i]
    return maximo
def Minimo( lista):
    minimo = lista[0]
    for i,e in enumerate(lista):
        if e<minimo:
            minimo= lista[i]
    return minimo

L = [1,7,2,9,15]
print("SOMA = {0}\nMÁXIMO: {1}\nMÍNIMO: {2}".format(Soma(L),Maximo(L),Minimo(L)))
