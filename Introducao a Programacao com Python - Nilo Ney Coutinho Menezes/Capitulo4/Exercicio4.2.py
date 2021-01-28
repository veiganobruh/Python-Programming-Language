'''

Escreve um programa que pergunte a velocidade do carro de um usuario .
Caso ultrapasse 80km/h , exiba uma mesnagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando 5 reais acima de 80km/h
'''
print("\n\n\t\t\tMULTA DE TRÂNSITO ")
# Perdi o para o usuario o valor da velocidade
velocidade = input('O VALOR DA VELOCIDADE EM KM/H:')
if int(velocidade)>80:
    valor_multa = (int(velocidade)-80)*5
    print("\n\nVOCÊ FOI MULTADO !\nVALOR DA MULTA:",valor_multa,'Reais')
else:
    print("PARABÉNS, CONTINUE DANDO ESSE EXEMPLO NO TRÂNSITO!")