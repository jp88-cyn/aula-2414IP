
horas_treinadas = int(input("Por Quantas horas voce treinou nessa Semana?: "))

if horas_treinadas <= 10:
    ganho_pontos = 2 * horas_treinadas
    ganho_dinheiro = 0.55 * ganho_pontos
    print(f"Voce treinou por {horas_treinadas}, Acumulou {ganho_pontos} pontos assim podendo sacar {ganho_dinheiro:.4}. ")

elif horas_treinadas >= 10 or horas_treinadas <= 20:
    ganho_pontos = 5 * horas_treinadas
    ganho_dinheiro = 0.55 * ganho_pontos
    print(f"Voce treinou por {horas_treinadas}, Acumulou {ganho_pontos} pontos assim podendo sacar {ganho_dinheiro:.4}.")

elif horas_treinadas >= 20:
    ganho_pontos = 10 * horas_treinadas
    ganho_dinheiro = 0.55 * ganho_pontos
    print(f"Voce treinou por {horas_treinadas}, Acumulou {ganho_pontos} pontos assim podendo sacar {ganho_dinheiro:.4}. ")


else:
    print("Invalido.")