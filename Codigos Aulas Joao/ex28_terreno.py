
largura = int(input("Qual a Largura em metros do Terreno: "))
comprimento = int(input("Qual o Comprimento em Metros do Terreno: "))

m2total = comprimento * largura

if  m2total >= 500:
    print(f"Terreno VIP de {m2total}")
    

elif m2total >= 100 or m2total == 500:
    print(f"Terreno MASTER de {m2total}")
    

elif m2total <= 100:
    print(f"Terreno Popular de {m2total}")
    

else:
    print("Terreno abaixo da Media precisa.")

