def pesquisa( lista, valor):
   for i, e in enumerate(lista):
      if e == valor:
         return i 
   return None


lista = list(range(1,10))
valor = int (input("DIGITE O VALOR A PROCURAR: "))
indice = pesquisa(lista,valor)
if indice!=None:
   print("Lista[{0}] = {1}".format(indice,lista[indice]))
else:
   print('VALOR NÃO ENCONTRADO! ')