 # Ordenação

L = [3,3,1,5,4]

fim = 5 

while fim > 1:
    trocou = False
    x=0
    while x < (fim-1):
        if (L[x]>L[x+1]):
            trocou =True
            temp = L[x]
            L[x]=L[x+1]
            L[x+1]=temp 
        x +=1
    if not trocou:
        break
    fim -=1

for e in L:
    print(e)

# quando existe dois valores iguais na lista instrução do if (L[x]>L[x+1] não é executada, até que toda a lista esteja ordenada! 