String1 = input("String1: ")
String2 = input("String2: ")
String3 = input("String3: ")
resultado = ""

if len(String2) == len (String3):
    for letra in String1:
        posicao = String2.find(letra)
        if ( posicao >= 0 ):
            resultado += String3[posicao]
        else:
            resultado +=letra
    print("Os caracteres %s encontrado na %s foram substituido por %s resultando: %s"%(String2,String1,String3,resultado))
else: 
    print("Tamanho da string2 e string3 são diferentes! ")
