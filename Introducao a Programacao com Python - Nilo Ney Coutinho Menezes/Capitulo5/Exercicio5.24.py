


quantidade = int(input("Quantidade de número primo:"))

if (quantidade <= 0):
    print("Quantidade inválida!")
else: 
    if (quantidade >= 1):
        numero = 2 
        print("%d"%numero)
        contador = 1
        i = 3
        while contador < quantidade:
            numero = 3
            while(numero < i):
                if( i % numero == 0):
                    break
                numero = numero + 2
            if numero == i:
                print("%d"%numero)
                contador = contador + 1
            i += 1