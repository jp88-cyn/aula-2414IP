#ler nome, sexo, valor_compras
# homens 5% de desconto
# 0.05
# mulher 13% de desconto
# 0.13


nome = str(input("Qual o seu Nome? : "))
sexo = str(input("Sexo: "))

if sexo == "M":
    compra_valor = float(input("Valor total da Compra: "))
    desconto = compra_valor * 0.05
    valor_desconto = compra_valor - desconto
    print(f"Ola {nome} sua compra recebeu um desconto de 5%, Fazendo ela agora estar por {valor_desconto}")
    pass
elif sexo == "F":
    compra_valor = float(input("Valor total da Compra: "))
    desconto = compra_valor * 0.13
    valor_desconto = compra_valor - desconto
    print(f"Ola {nome} sua compra recebeu um desconto de 13%. Fazendo ela agora estar por {valor_desconto}")
    pass
else:
    print("Invalido.")
   