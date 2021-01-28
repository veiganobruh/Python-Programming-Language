# Programa para aprovar um empréstimo bancário p/ compra uma casa 

# Perguntar o valor da casa a comprar, o salário , e a quantidade de prestações

print("\n\n\t\t\t MENU\n\n")


valor_casa = float(input("O VALOR DA CASA: "))
valor_salario = float(input("O SEU SALÁRIO: "))
quantidade_prestacoes = int(input ( "O NÚMERO DE PRESTAÇÕES: ")) 

# O valor da prestaçao mensal nao pode ser superior a 30% do salário

parcelas = valor_casa/quantidade_prestacoes

if (parcelas <=  (valor_salario*30/100)):
    print("EMPRÉSTIMO APROVADO!")
else:
    print("EMPRÉSTIMO REPROVADO!")
