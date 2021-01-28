# tabuada - o usuario pode digita o inicio e final 

print("\n\n\t\tTABAUDA\n\n")

fixo = int(input(" TABUADA DO NUMERO:"))
variavel_inicio = int (input(" O NUMERO DE INICIO DA TABUADA:"))
variavel_final = int (input(" O NUMERO DE TERMINO DA TABUADA:"))


while variavel_inicio<=variavel_final:
    print("%d x %d ="%(fixo,variavel_inicio), fixo*variavel_inicio)
    variavel_inicio = variavel_inicio+1 
    