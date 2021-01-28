# perguntar o valor inicial de uma divida, o juro mensal e o valor total a ser pago no mês 
#imprima o numero de meses para que a divida seja paga , total pago e o total de juros pago.


print("\n\n\n\t\t\tMENU\n\n\n")#menu
# criando as variaveis 
saldo = float (input("DIGITE A TOTAL DA DIVIDA: "))
juro = float (input("DIGITE O JURO MENSAL: "))
prestacao = float (input("DIGITE O VALOR TOTAL DA PARCELA: "))

contador = 0 

while saldo > 0:
    juro = saldo*juro/100
    saldo = saldo - (prestacao-juro)
    print(saldo)
    contador = contador + 1 


print("\nNUMERO DE MESES PARA PAGAR A  DIVIDA = ",contador)
print("TOTAL PAG0 = " )
print("TOTAL DE JUROS = ")