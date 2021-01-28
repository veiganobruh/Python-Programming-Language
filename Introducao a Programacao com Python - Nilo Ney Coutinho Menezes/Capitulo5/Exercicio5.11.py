
#Perguntar a taxa de juros e volor inicial de depósito 
#exiba os valores mes a mes para os 24 primeiros meses 
#Escreva o total de ganho com juros no periodo 



# Menu 

print("\n\n\n\t\t\tMENU\n\n\n")

deposito_inicial = float (input("DIGITE O DEPÓSITO INICIAL:  "))
taxa_juros = float (input("DIGITE A TAXA DE JUROS EM %:  "))

deposito_inicial1 = deposito_inicial
# exibindo o deposito inicial 
print("\n\nDEPOSITO INICIAL = ",deposito_inicial,"\n")

contador = 1 

while contador<=24:
        deposito_inicial = deposito_inicial + (deposito_inicial*taxa_juros/100)
        print("%d MÊS: %f"%(contador,deposito_inicial))
        contador = contador + 1 


print("VALOR TOTAL  = ",deposito_inicial,"REAIS")
print("GANHO TOTAL  = ",deposito_inicial-deposito_inicial1," REAIS")