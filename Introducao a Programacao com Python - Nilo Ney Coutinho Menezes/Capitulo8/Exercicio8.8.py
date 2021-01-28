# Maximo divisor comum - é o maior número que ao mesmo tempo pode dividir todos esse números 
def MDC(a , b ):
    if  b == 0:
        return a
    if a>b:
        return MDC(b,a%b)
# minimo divisor comum  - é o menor número que, ao mesmo tempo, é múltiplo de todos esse numeros 

def MMC(a,b):
    res = abs(a*b)/MDC(a,b)
    return res

a = int ( input("DIGITE 1 - NÚMERO: "))
b = int ( input("DIGITE 2 - NÚMERO: "))

print("MMC: {0}".format(MMC(a,b)))