
dicionario = {}
palavra = input("Palavra:")

for letra in palavra:
    if (letra in dicionario):
        if ( letra != " "):
            dicionario[letra] = dicionario[letra]+1
    else:
        if ( letra != " "):
            dicionario[letra] = 1
print(dicionario)

