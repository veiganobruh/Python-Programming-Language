lista = [1,[2,3,4,[5,6,7]]]

def imprimi_lista(lista):
    for i,e in enumerate(lista):
        if type(e)==int:
            print(" "*i,e)
        elif type(e)==list:
            imprimi_lista(e)
            
imprimi_lista(lista)