# perguntar qual a distancia que um passageiro quer em km
# calcule o preço da passagem cobrando 0.50 para viagens normais
# se passar de 200km e 0.45 para viagens mais longas

km = float(input("Qual a quantidade a ser percorrida? : "))

valorViagem_Normal = 0.50
valorViagem_Longa = 0.45

if km <= 200 or 200:
    valorApagar = valorViagem_Normal * km
    print(f"Por {km} voce deve pagar no final {valorApagar}")

elif km >= 200:
    valorApagar = valorViagem_Longa * km
    print(f"Por {km} voce deve pagar no final {valorApagar}, por conta de ")

else:
    ("Quantidade invalida")
