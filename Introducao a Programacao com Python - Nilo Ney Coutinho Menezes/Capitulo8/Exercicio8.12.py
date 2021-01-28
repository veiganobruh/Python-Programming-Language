def Comparador(string, lista):
    string = list(string)
    
    for e in lista:
        if e in string:
            return True
    else:
        return False


lista = list("mundo")
string = "olha mundo"

print(Comparador(string,lista))