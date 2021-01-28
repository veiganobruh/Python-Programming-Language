'''
Escrever um programa que leia códigos do produto do teclado.
Programa deve ler os números até que o usuário digite 0 (Zero). 
Exibir o total de compra depois que  o usuario digitar zero, outro condigo deve aparecer na tela uma mensagem de erro! 

'''
print(" \n\n\n\t\t\t MENU \n\n 0 - Para Sair\n\n") # Menu descritivo 
print("|\t\t CÓDIGO \t\t | \t\t PREÇO \t\t\t|")
print("---------------------------------------------------------------------------------")
print("|\t\t    1   \t\t | \t\t 0,50 \t\t\t|")
print("---------------------------------------------------------------------------------")
print("|\t\t    2   \t\t | \t\t 1,00 \t\t\t|")
print("---------------------------------------------------------------------------------")
print("|\t\t    3   \t\t | \t\t 4,00 \t\t\t|")
print("---------------------------------------------------------------------------------")
print("|\t\t    5   \t\t | \t\t 7,00 \t\t\t|")
print("---------------------------------------------------------------------------------")
print("|\t\t    9   \t\t | \t\t 8,00 \t\t\t|")
print("---------------------------------------------------------------------------------\n\n\n")
soma = 0 
contador = 0

while True:
    codigo = int ( input("DIGITE O CÓDIGO DO PRODUTO: "))
    if codigo == 0 :
        break 
    elif codigo ==1:
        valor = 0.5 
    elif codigo == 2:
        valor  = 1.00
    elif codigo == 3:
        valor = 4.00
    elif codigo == 5:
        valor = 7.00
    elif codigo == 9:
        valor = 8.00
    else:
        print("CÓDIGO INVÁLIDO !")
        valor = 0
        contador = contador - 1 

    soma = soma + valor
    contador = contador + 1 

print("\n\nTOTAL COMPRA = % f E QUANTIDADE DE PRODUTO = %d"%(soma,contador))