# Escreva um programa que leia três números e que imprima o maior e o menor 

print('\n\n\t\t\tDIGITE TRÊS NÚMEROS\n\n')
numero1 = float (input("DIGITE O PRIMEIRO NÚMERO: "))
numero2 = float (input("DIGITE O SEGUNDO NÚMERO: "))
numero3 = float (input("DIGITE O TERCEIRO NÚMERO: "))

# calculando o maior número 

if (numero1>numero2) and (numero1>numero3):
        print("\nPRIMEIRO NÚMERO É O MAIOR NÚMERO!")
elif (numero2>numero1) and (numero2>numero3):
        print("\nSEGUNDO NÚMERO É O MAIOR NÚMERO!")
elif (numero3>numero1) and (numero3>numero2):
        print("\nTERCEIRO NÚMERO É O MAIOR NÚMERO!")

# calculando o menor número 

if (numero1<numero2) and (numero1<numero3):
        print("\nPRIMEIRO NÚMERO É O MENOR NÚMERO!")
elif (numero2<numero1) and (numero2<numero3):
        print("\nSEGUNDO NÚMERO É O MENOR NÚMERO!")
elif (numero3<numero1) and (numero3<numero2):
        print("\nTERCEIRO NÚMERO É O MENOR NÚMERO!")
