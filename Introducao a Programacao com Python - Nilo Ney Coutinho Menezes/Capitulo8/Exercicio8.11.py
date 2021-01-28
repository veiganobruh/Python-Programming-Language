
def validacao_string( pergunta , minimo, maximo):
    while True:
        palavra = input(pergunta)
        if len(palavra)<minimo or len(palavra)>maximo:
            print("PALAVRA INVÁLIDA! DIGITE UMA PALAVRA COM NO MINIMO {0} CARACTERES E NO MÁXIMO {1} CARACTERES\n\n".format(minimo,maximo))
        else:
            return palavra

pergunta = "INSIRA A PALAVRA: "
print(validacao_string(pergunta,4,10))
