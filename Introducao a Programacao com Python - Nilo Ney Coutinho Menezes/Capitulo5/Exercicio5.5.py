'''Fazer a contagem entre o numero inicial e final digitado pelo usuario imprimindo os x numero 
digitado pelo usuario multiplo de algum numero digitado pelo usuario  '''


print("\n\n\t\t\tCONTADOR\n\n") # menu 
inicio = int(input("DIGITE O NUMERO INICIAL:")) # variavel de entrada inicial
final = int (input("DIGITE O NUMERO FINAL:"))  # variavel de entrada final 

imp = int ( input("DIGITE O NUMERO DE IMPRESSOES:"))
mult = int (input("DIGITE O NUMERO MULTIPLO:"))

# contador loop while 
contador = 0 
while inicio<=final:
    if ((inicio%mult) == 0) and (contador <imp): # condição para mostrar apenas os numeros imparares 
        print("%d"%inicio)
        contador = contador+1
    inicio = inicio + 1