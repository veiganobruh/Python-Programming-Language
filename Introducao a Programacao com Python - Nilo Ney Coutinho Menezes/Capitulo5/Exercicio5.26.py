
dividendo = int ( input("Dividendo:"))
divisor = int(input("Divisor: "))

resto = dividendo - divisor
resultado = 1 
while(True):
    resto = resto - divisor
    resultado = resultado + 1
    if ( divisor == dividendo ):

       #print("Resutado: 1" )
        print("Resto: 0 " )
        break
    
    if ( resto < divisor ):

        #print("Resutado : %d" %resultado)
        print("Resto: %d" %(dividendo-(resultado*divisor)))
        break
   
