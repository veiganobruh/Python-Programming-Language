ultimo = 0 
fila = list(range(1,ultimo+1)) # criar uma lista de 1 ate 10 

while True: 
    print('\nEXISTEM %d CLIENTES NA FILA'%len(fila))
    print("FILA ATUAL:",fila)
    print('DIGITE F PARA ADICIONAR UM CLIENTE AO FIM DA FILA,')
    print(" A PARA REALIZAR O ATENDIMENTO E S PARA SAIR")

    opcao = input("Opção ( F, A ou S):")
    if opcao == 'A':
        if( len(fila)>0):
            atendido = fila.pop(0)
            print("CLIENTE %d ATENDIDO"%atendido)
        else: 
            print("FILA VAZIA ! NINGUEM PARA ATENDER")
    elif opcao =='F':
        ultimo+=1
        fila.append(ultimo)
    elif opcao =='S':
        break
    else:
        print("OPÇÃO INVALIDA! DIGITE APENAS F, A OU S !")