
# JOGO DA VELHA # 
listapalavra = ["brasil","argentina","paraguai","chile","uruguai","bolivia","colombia","equador"]
# Criando uma indice
numero = int(input("Numero: "))
# Escolhendo uma palavra na lista
palavra=listapalavra[(numero*776)%len(listapalavra)]

# Escondendo a palavra digitada para que o jogar nao veja a palavra digitada
for i in range(100):
    print()          

# Criando duas lista Palavra_digitada e Palavra_Correta 
Palavra_digitada = [] # Lista começa vazia 
Palavra_Correta = [] # Lista começa vazia

# criando uma variavel contador de erros 
Contador_erros = 0 # inicializada como Valor Zero 

# Lista de desenho 
desenho = """
X==:==
X  :
X
X
X
X
=======

"""
linha = []
for l in desenho.splitlines():
    linha.append(list(l))

#Criando o Loop Principal 
while True:
    senha = "" # crianddo um variavel senha que iniciada em vazio 

    # inicio da estrutura para mostra a palavra na tela 
    for letra in palavra:                 # Essa estrutura faz com que as palavras que foram acertadas sejam exibidas na tela
        if letra in Palavra_Correta:       # mostrando para o usuario como a palavra esta ficando
            senha = senha + letra
        else:
            senha = senha + "."
    print(senha)                        # final da estrutura 

    # caso a palavra digita está correta o jogo finaliza
    if senha == palavra:
        print("VOCÊ ACERTOU! ")
        break
    # caso a palavra nao estiver completa vem para essa estrutura 

    Tentativa = input("\nDIGITE UM LETRA: ").lower().strip() # faz a o usuario digitar uma palavra 
    
    # nessa condição , verificar se o usuario ja digitou a letra anteriomente 
    if Tentativa in Palavra_digitada:
        print("VOCÊ JÁ TENTOU ESSA LETRA!")  
        continue # faz o usuario diigtar a palavra novamente, vontando o programa para fora do if 
    else:  # se a palavra nao foi digitada , entra no else 
        Palavra_digitada += Tentativa     # faz um armazendo da letra 

        # se a tentativa estiver entro da palavra 
        if Tentativa in palavra:
            Palavra_Correta += Tentativa  # a palavra correta recebe tentativa
        else:
            Contador_erros = Contador_erros + 1 # senao contamos o erro 
            print("VOCÊ ERRO!")
    
    # Fazendo o desenho do homemzinho 
            if Contador_erros == 1:
                linha[3] = "X  O"
            elif Contador_erros == 2:
                linha[4] = "X  |"
            elif Contador_erros == 3:
                linha[4] = "X /|"
            elif Contador_erros == 4:
                linha[4] = "X /|\ "
            elif Contador_erros == 5:
                linha[5] = "X / "
            elif Contador_erros == 6:
                linha[5] = "X / \ "

    for l in linha:
        print("".join(l))
 
    if Contador_erros==6:
        print("Game Over - Enforcado") # final do programa
        print("A palavra secreta era: %s"%palavra)
        break  # Sair do loop 
