# Ocorre um erro de loop infinito - devido ao rebondamento 
valor = float ( input("DIGITE O VALOR A PEGAR: "))*1000
cedulas = 0
atual = 100000 
apagar = valor
while True:
    if atual <= apagar:
        apagar -=atual
        cedulas +=1
    else:
        print("%d CÉDULA(S) DE R$: %.3f"%(cedulas,atual/1000))
        if apagar ==0 :
            break
        if atual ==100000:
            atual=50000
        elif atual ==50000:
            atual = 20000
        elif atual==20000:
            atual=10000
        elif atual==10000:
            atual=5000
        elif atual==5000:
            atual = 1000
        elif atual==1000:
            atual = 500
        elif atual ==500:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 1
        cedulas=0