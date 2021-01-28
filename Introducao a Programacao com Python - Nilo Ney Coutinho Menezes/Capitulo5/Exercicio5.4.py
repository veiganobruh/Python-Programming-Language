# Fazer a contagem entre o numero inicial e final digitado pelo usuario imprimindo  apenas o numeros imparares 


print("\n\n\t\t\tCONTADOR\n\n") # menu 
inicio = int(input("DIGITE O NUMERO INICIAL:")) # variavel de entrada inicial
final = int (input("DIGITE O NUMERO FINAL:"))  # variavel de entrada final 

# contador loop while 

while inicio<=final:
    if (inicio%2)!=0: # condição para mostrar apenas os numeros imparares 
        print("%d"%inicio)
    inicio = inicio+1 
