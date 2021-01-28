import random
import validacao

n = random.randint(1,10)
i = 0 
while i<3:
    tentativa = "ESCOLHA UM NUMERO ENTRE 1 E 10: "
    valor = validacao.valor_inteiro(tentativa,1,10)
    if  valor == n:
        print("PARABENS VOCÊ ACERTOU! ")
        break
    else:
        print("VOCÊ ERROU! ")
        i = i +1 

print("VALOR GERADO: {0}\nVALOR INSERIDO: {1}".format(n,valor))