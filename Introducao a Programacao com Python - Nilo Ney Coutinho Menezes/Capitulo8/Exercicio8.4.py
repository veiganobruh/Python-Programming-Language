def area_triangulo(b , h):
    area = b*h/2
    return area
base = float( input("DIGITE A BASE DO TRIANGULO: "))
altura = float( input("DIGITE A ALTURA DO TRIANGULO: "))

print("AREA = {0:^5}".format(area_triangulo(base,altura)))