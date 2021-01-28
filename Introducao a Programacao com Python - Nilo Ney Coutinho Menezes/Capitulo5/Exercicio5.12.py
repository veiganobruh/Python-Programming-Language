
#Perguntar a taxa de juros e volor inicial de depósito 
#exiba os valores mes a mes para os 24 primeiros meses 
#Escreva o total de ganho com juros no periodo 
#Pode deposita no inicio de cada mes e considera o calculo para o mês seguinte 
# E a quantidade de mêses para investimento 


# Menu 
print("\n\n\n\t\t\tMENU\n\n\n")

deposito_inicial = float (input("DIGITE O DEPÓSITO INICIAL:  "))
deposito_mensal = float (input("DIGITE O DEPÓSITO MENSAL:  "))
taxa_juros = float (input("DIGITE A TAXA DE JUROS EM %:  "))
meses_investimento = int( input("QUANTIDADE DE MÊSES PARFA INVESTIMENTO: "))

deposito_inicial1 = deposito_inicial
# exibindo o deposito inicial 
print("\n\nDEPOSITO INICIAL = ",deposito_inicial,"\n")

contador = 1 
while contador<=meses_investimento:
        deposito_inicial = deposito_inicial + (deposito_inicial*taxa_juros/100)
        print("%d MÊS: %f"%(contador,deposito_inicial))
        contador = contador + 1 
        deposito_inicial = deposito_inicial + deposito_mensal



print("VALOR TOTAL  = ",deposito_inicial-deposito_mensal,"REAIS")
