# Preço a pagar pelo fornecimento de energia elétrica 

# Pergunte a quantidade kWh consumida e o tipo de instalação R : residencial , I: industrial e C: Comércios 
print("\n\n\t\t\tPREÇO A PAGAR PELO FORNECIMENTO DE ENERGIA ELEÉTRICA\n\n")

quantidade_kwh = float ( input("QUANTIDADE DE KWh CONSUMIDA: "))

tipo_instalacao = input( " ESCOLHA UM TIPO DE INSTALAÇÃO: \nR - RESIDENCIAL\nI - INDUSTRIAL\nC - COMÉRCIOS\n")


# preco para instalação residencial 
if (tipo_instalacao == 'R' ) or (tipo_instalacao == 'r'):
    if quantidade_kwh<=500:
        print("TIPO DE INSTALAÇÃO: RESIDENCIAL\n")
        preco = quantidade_kwh*0.40
        print("PREÇO = ", preco)
    else:
        print("TIPO DE INSTALAÇÃO: RESIDENCIAL\n")
        preco = quantidade_kwh*0.65
        print("PREÇO = ", preco,"Reais")

# preco para instalação comercial 
elif (tipo_instalacao == 'C' ) or (tipo_instalacao == 'c') :
    if quantidade_kwh<=1000:
        print("TIPO DE INSTALAÇÃO: COMERCIAL\n")
        preco = quantidade_kwh*0.55
        print("PREÇO = ", preco,"Reais")
    else:
        print("TIPO DE INSTALAÇÃO: COMERCIAL\n")
        preco = quantidade_kwh*0.60
        print("PREÇO = ", preco,"Reais")

# preco oara instalação industrial
elif (tipo_instalacao == 'I' ) or (tipo_instalacao == 'i') :
    if quantidade_kwh<=5000:
        print("TIPO DE INSTALAÇÃO: INDUSTRIAL\n")
        preco = quantidade_kwh*0.55
        print("PREÇO = ", preco,"Reais")
    else:
        print("TIPO DE INSTALAÇÃO: INDUSTRIAL\n")
        preco = quantidade_kwh*0.60
        print("PREÇO = ", preco,"Reais")
else:
    print("DESCULPA, OPÇÃO INVÁLIDA ! ")
