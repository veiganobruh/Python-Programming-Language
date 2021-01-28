
numero = float ( input("Numero:"))
base = 2
p = base 
while (abs(numero -(base*base) ) >0.0001):
    p = ( base + (numero/base))/2 
    base = p 
print ("A raiz quadrada de %f é aproximadamente %f" % (numero, p))


