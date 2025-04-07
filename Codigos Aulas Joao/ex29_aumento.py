
nome = str(input("Qual o seu Nome?: "))
salario = float(input("Qual o seu Salario?: "))
anos_trabalhando = int(input("Por quantos anos voce trabalha Aqui?: "))

if anos_trabalhando <= 3:
    subtraçao_salario = (100 * salario ) / 100
    print(f"Seu Salario de {salario} agora teve um aumento de 3%, agora sendo {subtraçao_salario}")

elif anos_trabalhando >= 3 or 3 or anos_trabalhando <= 10:
    subtraçao_salario = (salario * 0.12 ) / 100
    print(f"Seu Salario de {salario} agora teve um aumento de 12.5%, agora é {subtraçao_salario}. ")