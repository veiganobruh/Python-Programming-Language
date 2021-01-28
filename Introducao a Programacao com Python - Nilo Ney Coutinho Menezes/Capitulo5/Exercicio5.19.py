
valor = float ( input("DIGITE O VALOR A PEGAR: "))*100
cedulas = 0
atual = 10000  
apagar = valor
while True:
    if atual <= apagar:
        apagar -=atual
        cedulas +=1
    else:
        print("%d CÉDULA(S) DE R$: %.2f"%(cedulas,atual/100))
        if apagar ==0 :
            break
        if atual ==10000:
            atual=5000
        elif atual ==5000:
            atual = 2000
        elif atual==2000:
            atual=1000
        elif atual==1000:
            atual=500
        elif atual==500:
            atual = 100
        elif atual==100:
            atual = 50
        elif atual ==50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas=0