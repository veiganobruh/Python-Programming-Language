
string1 = input("String1:")

contador = {}
for letra in string1:
    if letra in contador:
        if ( letra != " "):
            contador[letra] +=1
    else:
        if ( letra != " "):
            contador[letra] = 1

for chave in contador:
    print(f"{chave}:{contador[chave]}x")