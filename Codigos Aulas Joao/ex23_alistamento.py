
ano_nascimento = int(input("Qual a sua idade: "))
idade = 2025 - ano_nascimento


if idade == 18:
    tempo_faltando = 18 - idade
    print("Voce ja pode se alistar ao exercito!")
    pass

elif idade >=18:
    tempo_faltando = 18 - idade
    print(f"Voce ja poderia ter se alistado ao exercito, com {tempo_faltando} anos que ja passou.")
    pass