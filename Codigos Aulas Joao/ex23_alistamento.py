
ano_nascimento = int(input("Qual o seu Ano de Nascimento? : "))
idade = 2025 - ano_nascimento

if idade == 18:
    print(f"Voce ja pode se alistar ao exercito tendo {idade} anos de idade. ")


elif idade >=19:
    anos_passados = idade - 18
    print(f"Voce ja passou do tempo para se alistar, Em especifico {anos_passados} anos se passaram.")
    

elif idade <= 17 or 17:
    anos_faltando = 18 - idade
    print(f"Voce ainda nao pode se alistar ao exercito, Faltando {anos_faltando} Anos para maior idade.")
    

else:
    print("Invalido")