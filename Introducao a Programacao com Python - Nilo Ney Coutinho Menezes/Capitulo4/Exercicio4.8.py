# leia dois número e pergunta se quer fazer soma, subtração, multiplicação ou divisão 
#  e exiba o valor do resultado 


# MENU 
print('\n\n\t\t\tMENU DE OÇÕES DE OPERAÇÕES\n')
print("\n1 - SOMA \n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n\n")

# VARIAVEL PARA ESCOLHER A OPÇÃO 
opcao = int(input('DIGITE UM NÚMERO DAS OPÇÕES ACIMA: '))
print("\n")
# MOSTRA A OPÇÃO ESCOLHIDA NA TELA 
if  opcao == 1 :
    print("OPERADOR - SOMA (+)")
elif opcao ==  2 :
   print("OPERADOR - SUBTRAÇÃO (-)")
elif opcao ==  3 :
   print("OPERADOR - MULTIPLICAÇÃO (*)")
elif opcao ==  4 :
   print("OPERADOR - DIVISÃO (/)")

# VARIAVEIS DE ENTRADA PARA FAZER AS OPERAÇÕES 
num1 = float(input("\nDIGITE O PRIMEIRO NÚMERO: ")) # convertendo o valor digitado pelo usuario para um numero, para que se possa fazer operações matematicas 
num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))# convertendo o valor digitado pelo usuario para um numero, para que se possa fazer operações matematicas

if  opcao == 1 :
    resultado = num1 + num2
    print("RESULTADO = ",resultado)
elif opcao ==  2 :
    resultado = num1 - num2
    print("RESULTADO = ",resultado)
elif opcao ==  3 :
    resultado = num1 * num2
    print("RESULTADO = ",resultado)
elif opcao ==  4 :
   resultado = num1 / num2 # P/ num2 diferente de zero 
   print("RESULTADO = ",resultado)

