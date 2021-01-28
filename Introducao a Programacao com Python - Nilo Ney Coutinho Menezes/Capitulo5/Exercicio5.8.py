# Imprimindo o resultada multiplicação de dois números 
# utlizando a soma, ou seja, 2 x 3 = 2+2+2 = 6 

# MENU 
print("\n\n\t\tTABUADA PELA SOMAn\n\n")

numero1 = int( input("  DIGITE O PRIMEIRO NUMERO:"))
numero2 = int (input("  DIGITE O SEGUNDO NUMERO:"))

soma = 0 
contador = 0 

while contador<numero2:
    soma = soma + numero1
    if contador ==0 :
        print("%d\r"%numero1)
    else:
        print("+ %d\r"%numero1)
    
    contador = contador+1 

print("%d x %d = " %(numero1,numero2), soma)