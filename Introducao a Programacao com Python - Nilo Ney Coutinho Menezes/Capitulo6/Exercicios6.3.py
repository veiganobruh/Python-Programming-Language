Lista1 = []
Lista2 = []
Lista3 = []

while (True):
    valor = int ( input("Inserir os elementos da Lista1 ( 0 para sair ):"))
    if valor == 0:
        break
    Lista1.append(valor)
while (True):
    valor = int ( input("Inserir os elementos da Lista2 ( 0 para sair ):"))
    if valor == 0:
        break
    Lista2.append(valor)

i = 0 
aux = Lista1[:]
aux.extend(Lista2)
while ( i < len(aux)):
    j=0
    while(j<len(Lista3)):
        if ( aux[i]==Lista3[j]):
            break
        j +=1
    if ( j == len(Lista3)):
        Lista3.append(aux[i])
    i +=1

i = 0 
while ( i < len(Lista3)):
    print("Lista = %d"%Lista3[i])
    i +=1
        