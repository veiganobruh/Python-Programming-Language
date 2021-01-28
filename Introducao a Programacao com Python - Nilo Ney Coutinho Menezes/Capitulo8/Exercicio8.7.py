# Maximo divisor comum 
def MDC(a , b ):
    if  b == 0:
        return a
    if a>b:
        return MDC(b,a%b)

a = int ( input("DIGITE 1 - NÚMERO: "))
b = int ( input("DIGITE 2 - NÚMERO: "))

print("MDC: {0}".format(MDC(a,b)))
