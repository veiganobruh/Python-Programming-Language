L1 = []
L2 = []
L3 = []

while True:
    n1 = input("INSIRA O ELEMENTO DA LISTA 1 (0 SAIR): ")
    if n1=='0':
        break
    L1.append(n1)
print('\n\n')
while True:
    n2 = input("INSIRA O ELEMENTO DA LISTA 2 (0 SAIR): ")
    if n2=='0':
        break
    L2.append(n2)

L3.append(L1[0])
L3.append(L2[0])

x = 0 
print("\n\nLISTA 1: ")
while x<len(L1):
    print(L1[x])
    x=x+1

x = 0 
print("\n\nLISTA 2: ")
while x<len(L2):
    print(L2[x])
    x=x+1

x = 0 
print("\n\nLISTA 3: ")
while x<len(L3):
    print(L3[x])
    x=x+1
