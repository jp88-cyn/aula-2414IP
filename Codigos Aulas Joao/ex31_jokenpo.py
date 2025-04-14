
import random

while True:
    escolha_jogador = str(input("Escolha entre Pedra, Papel e Tesoura: "))
    Tesoura = 1
    Papel = 2
    Pedra = 3

    escolha_pc = random_integer = random.randint(1, 3)

    if escolha_jogador == Papel and escolha_pc == 2:
        print(f"Empate. Pois os dois escolheram a mesma opçao.")

    elif escolha_jogador == Tesoura and escolha_pc == 1:
        print(f"Empate. Pois os dois escolheram a mesma opçao.")

    elif escolha_jogador == Pedra and escolha_pc == 3:
        print(f"Empate. Pois os dois escolheram a mesma opçao.")

    elif escolha_jogador == "Tesoura" and escolha_pc == 2:
        print("Voce Venceu! Ele escolheu Papel")

    elif escolha_jogador == "Papel" and escolha_pc == 3:
        print("Voce Venceu! Ele escolheu Pedra")

    elif escolha_jogador == "Pedra" and escolha_pc == 1:
        print("Voce Venceu! Ele escolheu Tesoura")

    elif escolha_jogador == "Pedra" and escolha_pc == 2:
        print("Voce perdeu! O Pc escolheu Papel")

    elif escolha_jogador == "Papel" and escolha_pc == 1:
        print("Voce perdeu! O Pc escolheu Tesoura.")

    elif escolha_jogador == "Tesoura" and escolha_pc == 3:
        print("Voce perdeu! O Pc escolheu Pedra")

    else:
        print("Invalido, tente novamente. ")

    saida = str(input("Digite s para sair, caso nao queira apenas digite qualquer coisa: "))
    if saida.lower() == "s":
        print("Bye Bye!")
        break


    # https://docs.vultr.com/python/examples/generate-a-random-number?ref=9141995&utm_source=performance-max-latam&utm_medium=paidmedia&obility_id=17096555207&&utm_campaign=LATAM_-_Brazil_-_Performance_Max_-_1001&utm_term=&utm_content=&ref=9141995&gad_source=1&gclid=EAIaIQobChMI-vDK04rYjAMVyixECB2sLBBgEAAYASAAEgID6vD_BwE