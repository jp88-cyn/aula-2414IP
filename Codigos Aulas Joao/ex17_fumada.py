dias_fumado = int(input("Quantos Cigarros voce fuma por dia? : "))
anos_fumando = int(input("Por quantos anos voce Fuma? : "))


tempo_perdido = anos_fumando + dias_fumado
dias_perdidos = 10 * tempo_perdido

print(f"Voce perdeu {dias_perdidos} dias de Vida fumando por {anos_fumando} anos.")