def valor_inteiro (mensagem,minimo,maximo):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= maximo and valor>=minimo:
                return valor
            else:
                print("VALOR INVALIDO! DIGITAR VALORES ENTRE {0} E {1}".format(minimo,maximo))
        except: 
            print("O VALOR TEM QUE SE UM NUMEOR INTEIRO ENTRE {0} E {1}".format(minimo,maximo))