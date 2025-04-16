
classificaçao_carro = str(input("Qual o Tipo do Carro? (Luxo ou Popular): "))

km_percorrido = int(input("Quantos KM percorridos? : "))

dias = int(input("Quantos dias alugado? : "))

if classificaçao_carro == "Luxo" or "luxo":
    dias_preço = 150 * dias
    if km_percorrido <= 100 or 100:
        preço_geral = 0.20 * km_percorrido
        pagar = dias_preço + preço_geral
        print(f"Por conta de ser um de Luxo, Voce tem que pagar {pagar}.")

    elif km_percorrido >= 100:
        preço_geral = 0.20 * km_percorrido
        pagar = dias_preço + preço_geral
        print(f"Por conta de ser um de Luxo, Voce tem que pagar {pagar}.")

elif classificaçao_carro == "Popular" or "popular":
    dias_preço = 90 * dias
    if km_percorrido <= 200 or 200:
        preço_geral = 0.30 * km_percorrido
        pagar = dias_preço + preço_geral
        print(f"Por conta de ser um de Luxo, Voce tem que pagar {pagar}.")

    elif km_percorrido >= 200:
        preço_geral = 0.25 * km_percorrido
        pagar = dias_preço + preço_geral
        print(f"Por conta de ser um de Luxo, Voce tem que pagar {pagar}.")

else:
    print("Invalido")