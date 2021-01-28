quantidade_cigarro_dia = int(input("Quantidade de cigarros fumado por dia ?  "))
tempo = int ( input("Quantos anos já fumou ?  "))

total_cigarro = tempo*365*quantidade_cigarro_dia
tempo_perdido = (total_cigarro*10)/(60*24)
print("Tempo de vida perdido: %0.2f"%tempo_perdido, "Dias")