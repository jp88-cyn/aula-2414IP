km_passados = int(input("Qual a Velocidade atual do seu Carro?(km): "))

if km_passados <= 80:
    print("Voce esta na media de velocidade Permitida.")


elif km_passados >= 80:
    acima_velocidade = km_passados - 80
    multa = 5 * acima_velocidade
    print(f"Voce foi multado por Ultrapassar a velocidade permitida. O valor a pagar é de {multa}")
    

else:
    print("Invalido.")