
anos_trabalhando = int(input("Por quantos anos voce trabalha aqui? : "))
genero = str(input("Sexo: "))
salario_atual = float(input("Salario Atual: "))

if genero == "Feminino" or "F":

# Nao sei qual a conta exata pra isso, talvez esteja errado btw :(
    if anos_trabalhando <= 15:
        subtraçao = salario_atual - 0.5
        divisao = subtraçao / salario_atual
        aumento_final = divisao * 100
        print(f"Voce teve um aumento de 5% agora sendo {aumento_final:.4}")

    elif anos_trabalhando >= 15 or <= 20:
        subtraçao = salario_atual - 0.12
        divisao = subtraçao / salario_atual
        aumento_final = divisao * 100
        print(f"Voce teve um aumento de 12% agora sendo {aumento_final:.4}")

    elif anos_trabalhando >= 20:
        subtraçao = salario_atual - 0.23
        divisao = subtraçao / salario_atual
        aumento_final = divisao * 100
        print(f"Voce")

    
elif genero == "Masculino" or "M":
    subtraçao = salario_atual