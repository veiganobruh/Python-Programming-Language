estoque = {"tomate": [1000, 2.30],
           "alface": [500 , 0.45],
           "batata": [2001, 1.20],
           "feijao": [100 , 1.50] }
total = 0 
print("Vendas:\n")

while(True):
    produto = input("Nome do Produto ( sair ): ")
    if (produto =="sair"):
        break
    if produto in estoque:
        quantidade = int (input("Quantidade:"))
        if ( estoque[produto][0]>= quantidade):
            preco = estoque[produto][1]
            custo = preco*quantidade
            print("%12s: %3d    x %6.2f = % 6.2f"%(produto, quantidade, preco,custo))
            estoque[produto][0]-=quantidade
            total+=custo
        else:
            print("Quantidade indisponível!")
    else:
        print("Produto inválido!")
print("\nCusto total: %10.2f\n"%total)
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ",chave)
    print("Quantidade: ",dados[0])
    print("Preço: %6.2f\n"%dados[1])