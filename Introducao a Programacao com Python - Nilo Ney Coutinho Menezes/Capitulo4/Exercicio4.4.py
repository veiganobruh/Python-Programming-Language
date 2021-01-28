# Calcule o aumento de um salário 
print('\n\n\t\t\t CÁLCULO DO AUMENTO DO SALÁRIO\n\n')
salario = float (input("DIGITE O SEU SALÁRIO: "))
if salario>1250:
    resultado = salario+(salario*10/100)
elif salario<=1250:
    resultado = salario+(salario*15/100)

print("SEU AUMENTO SERÁ DE",resultado, 'Reais')
