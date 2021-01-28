preco = float ( input("O preço da  mercadoria: "))
desconto = float ( input("O percentual de desconto:"))

print("Desconto  = %0.2f"%(preco*desconto/100),"Reais \nValor Mercadoria = %0.2f"%(preco-(preco*desconto/100)),"Reais" )