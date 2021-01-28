
ultimo1 = 10
ultimo2 = 5

fila1 = list(range(1,ultimo1+1))
fila2 = list(range(1,ultimo2+1))

while True: 
    print('\nEXISTEM %d CLIENTES NA FILA 1: '%len(fila1))
    print(fila1)
    print('\nEXISTEM %d CLIENTES NA FILA 2: '%len(fila2))
    print(fila2)
    
    print('DIGITE F PARA ADICIONAR UM CLIENTE AO FIM DA FILA 1')
    print('DIGITE G PARA ADICIONAR UM CLIENTE AO FIM DA FILA 2')
    print("DIGITE A PARA REALIZAR O ATENDIMENTO NA FILA 1")
    print("DIGITE B PARA REALIZAR O ATENDIMENTO NA FILA 2")
    print("DIGITE S PARA SAIR ")

    opcao = input("\n\nDIGITE UMA DAS OPÇÕES: ")
    if opcao =='A':
        if( len(fila1)>0):
            fila1.pop(0)
        else: 
            print("FILA 1 VAZIA ! NINGUEM PARA ATENDER")
    elif opcao =='B':
        if( len(fila2)>0):
            fila2.pop(0)
        else: 
            print("FILA 2 VAZIA ! NINGUEM PARA ATENDER")
    elif opcao== 'F':
        ultimo1=ultimo1+1
        fila1.append(ultimo1)
    elif opcao== 'G':
        ultimo2=ultimo2+1
        fila2.append(ultimo2)
    elif opcao == 'S':
        break
    else:
        print("OPÇÃO INVALIDA!")