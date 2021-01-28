
numero = int(input("Número:"))

if numero < 0:
    print("Número inválido!")

if (numero == 0 or numero == 1):
    print("%d não é primo!" %numero)
else:
    if (numero == 2):
        print("%d é primo"%numero)
    elif (numero%2 == 0):
        print("%d não é primo!" %numero)
    else:
        i = 3
        while(numero > i ):
            if numero % i == 0:
                break
            i +=1
        if i == numero :
            print("%d é primo" % numero)
        else:
            print("%d não é primo, porque é divisível por %d" % (numero, i))