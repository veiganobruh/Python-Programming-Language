
string1 = input("String1: ")
string2 = input("String2: ")

if ( string2 in string1):
    posicao = string1.rfind(string2)

print("%s encontrado na posição % d de %s"%(string2,posicao,string1))