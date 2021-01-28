
numero = int(input ("Número:"))

controle = 0
while 10 ** controle < numero:
    controle +=1

inicio = controle
final = 0
numerof = numeroi = numero 
especiali = especialf = 0 

while inicio > final:
    especiali = int(numeroi / (10 ** (inicio-1))) 
    especialf = numerof % 10  

    if especiali != especialf: 
        break
    final +=1 
    inicio -=1 

    numeroi = numeroi - (especiali * (10 ** inicio )) 
    numerof = int(numerof / 10) 

if especiali == especialf:
    print("%d é um palíndromo" % numero)
else:
    print("%d não é um palíndromo" % numero)
