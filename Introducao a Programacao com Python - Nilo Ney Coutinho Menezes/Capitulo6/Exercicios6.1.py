# Fazer a media das notas digitada pelo aluno 
# total de notas = 7 

print("\n\n\t\t CÁLCULO DA MÉDIA DE UM ALUNO\n\n")
print("INSIRA AS NOTAS:\n")
nota = [0,0,0,0,0,0,0]
soma = 0 
x = 0 
while x < 7: # armazenando as notas 
    nota [x]  = float(input("NOTA %d: " %x))
    x = x +1 
    soma = soma + nota[x]

print("\n\nIMPRIMINDO AS NOTASA\n\n")
x= 0 
while x < 7: # imprimindo na tela 
    print("NOTA %d: %5.2f"%(x,nota[x]))
    x = x + 1 
    
     
media = soma /x 
print("\n\nMÉDIA = %f"%media)