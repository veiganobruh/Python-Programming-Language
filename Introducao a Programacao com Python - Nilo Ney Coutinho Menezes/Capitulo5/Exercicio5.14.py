'''
Escrever um programa que leia números inteiros do teclado.
Programa deve ler os números até que o usuário digite 0 (Zero). 
Exibir a quantidade de números digitados, assim como a soma e a média aritmética 

'''
print(" \n\n\n\t\t\t MENU \n\n 0 - Para Sair\n\n") # Menu descritivo 

soma = 0                                            # acumulador
contador =0                                         # contando  a quantidade de numeros que foi digitado 
while True:                                         # laço de repetição - loop 
    valor = float (input("NÚMEROS DE ENTRADA: "))     # entrada das variaveis 
    if valor == 0:                                 # condição de para sair do loop 
        break
    soma = soma + valor                             # calcular a soma de todos os numero digitado
    contador = contador + 1                            # incremento 

if contador ==0:
    print("SOMA = 0  e MÉDIA = 0")
else :
    media = soma/contador 
    print("SOMA = %f  e MÉDIA = %f" %(soma,media))
