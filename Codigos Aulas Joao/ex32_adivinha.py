
import random

while True:

    escolha_pc = random_integer = random.randint(1, 10)

    escolha_player = int(input("Tente adivinhar qual numero de 1 a 10 que o PC escolheu: "))

    if escolha_pc == escolha_player:
        print(f"O Computador escolheu {escolha_pc}, Logo voce acertou!")
        break

    elif escolha_pc != escolha_player:
        print(f"O Computador escolheu {escolha_pc}, Logo voce perdeu.")

    else:
        print("INVALIDO.")
