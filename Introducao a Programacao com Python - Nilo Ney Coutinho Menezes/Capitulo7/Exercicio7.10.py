import string
import os

#CRIANDO UM FUNÇÃO PARA A EXIBIÇÃO DO  DESENHO DO JOGO DA VELHA
def Exibir_Jogo_Velha(lista):                                   
    print("\n\n\t\t  {0[0]:^1}  |  {0[1]:^1}  |  {0[2]:^1}  \n\t\t-----+-----+-----\n"
              "\t\t  {0[3]:^1}  |  {0[4]:^1}  |  {0[5]:^1}  \n\t\t-----+-----+-----\n"
              "\t\t  {0[6]:^1}  |  {0[7]:^1}  |  {0[8]:^1}  \n".format(lista)) 


#CRIANDO UMA LISTA PARA ARMAZENAMENTO 
lista = [1,2,3,4,5,6,7,8,9]    

print("\t\t   {0:-^10}".format("MENU"))
Exibir_Jogo_Velha(lista)


primeiro = True
while primeiro : #1 - loop 
    # Escolhendo a opção X ou  bolinha "O"
    jogador1 = input("1 - JOGADOR: (X OU O): ").lower() #opção 1 

    #Condição do para atribuir x ou o para o segundo jogador
    if ( jogador1 == 'x'):
        print("O JOGADOR {0}  É  \" O \"  ".format(2))
        jogador2 = "o"
        primeiro = False        #Condição para sair do while 
    elif jogador1 == 'o':
        print("O JOGADOR {0}  É  \" X \"  ".format(2))
        jogador2 = 'x'
        primeiro = False        #Condição para sair do while 
    else:                       #Caso a opção nao for x ou o, exibi um  mensagem de erro e retorna para a opção 1 
        print("ESCOLHA INVÁLIDA") 
        continue

aux = 1                 #Variavel de condição do loop 3 e 4 
contador=0              #Contador p/ verificar se não tem ganhador
fim = 0                 #Variavel de condição do loop principal  2 


while fim!=1:           #2 - Loop principal 
    while aux==1:       #3 - Loop do jogador 1 
        print("\n\t\tJOGADA DO JOGADOR 1") # inidicar o jogador            
        jogo1 = int(input("DIGITE O NÚMERO DA POSIÇÃO: ")) #Informar a posição para colocar X ou O 
        if (jogo1>0) and (jogo1<10): #Condição de validação da posição : Valores validos 1 ate 9 
            if jogo1 not in lista:  #Condição se a posição digitada nao estiver na lista  
                print("POSICAO JÁ PREENCHIDA") # informar que a posição ja está preenchida 
                continue  # retornar para o jagador Informa a posição 
            else:  
                lista[jogo1-1]= jogador1   # colocar o X ou O na lista  
                # condição de ganhador 
                if (lista[0]==jogador1 and lista[1]==jogador1 and lista[2]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1
                    break
                if (lista[3]==jogador1 and lista[4]==jogador1 and lista[5]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1 
                    break
                if (lista[6]==jogador1 and lista[7]==jogador1 and lista[8]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1 
                    break
                if (lista[0]==jogador1 and lista[3]==jogador1 and lista[6]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1 
                    break
                if (lista[1]==jogador1 and lista[4]==jogador1 and lista[7]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1
                    break
                if (lista[2]==jogador1 and lista[5]==jogador1 and lista[8]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1
                    break
                if (lista[0]==jogador1 and lista[4]==jogador1 and lista[8]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1 
                    break
                if (lista[2]==jogador1 and lista[4]==jogador1 and lista[6]==jogador1 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(1))
                    fim = 1
                    break
                Exibir_Jogo_Velha(lista) # exibir a o Jogo da velha para o usuario 
                contador +=1  # incremento do contador 
        else:
            print("VALOR INVÁLIDO") #informar que a posição é invalida nao esta entre os valores 1 e 9 
            continue
        aux = 2 #Aux recebe 2 para entrar no 4 - loop jogador 2  
        if ( contador == 9 ): # informar que nao houver ganhador - empate 
            print("NENHUM GANHADOR! EMPATE ")
            fim = 1
            aux = 0  
            break 
    while aux ==2:      #4 - Loop do jogador 2 
        #igual ao jogador 1 
        print("\n\t\tJOGADA DO JOGADOR 2")                
        jogo2 = int(input("DIGITE O NÚMERO DA POSIÇÃO: "))
        if (jogo2>0) and (jogo2<10):
            if jogo2 not in lista:
                print("POSICAO JÁ PREENCHIDA") 
                continue 
            else:  
                lista[jogo2-1]= jogador2    
                if (lista[0]==jogador2 and lista[1]==jogador2 and lista[2]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1
                    break
                if (lista[3]==jogador2 and lista[4]==jogador2 and lista[5]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1 
                    break
                if (lista[6]==jogador2 and lista[7]==jogador2 and lista[8]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1 
                    break
                if (lista[0]==jogador2 and lista[3]==jogador2 and lista[6]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1 
                    break
                if (lista[1]==jogador2 and lista[4]==jogador2 and lista[7]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1
                    break
                if (lista[2]==jogador2 and lista[5]==jogador2 and lista[8]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1
                    break
                if (lista[0]==jogador2 and lista[4]==jogador2 and lista[8]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1
                    break
                if (lista[2]==jogador2 and lista[4]==jogador2 and lista[6]==jogador2 ):
                    Exibir_Jogo_Velha(lista)
                    print("Jogador {0} Vencedor !".format(2))
                    fim = 1
                    break      
                Exibir_Jogo_Velha(lista)
                contador +=1
        else:
            print("VALOR INVÁLIDO")
            continue
        aux = 1 
        if ( contador == 9 ):
            print("NENHUM GANHADOR! EMPATE ")
            fim = 1 
            aux = 0 
            break 

os.system("pause")
    
