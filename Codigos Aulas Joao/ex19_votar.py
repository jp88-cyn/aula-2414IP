ano_nascimento = int(input("Qual o seu Ano de Nascimento? : "))
idade = 2025 - ano_nascimento 

if idade  >=18:
    print("Voce esta permitido a Votar! ")

elif idade <=17 or 17:
    print("Voce nao esta permitido a Votar!")

elif idade <=0 or 0:
    print("Idade abaixo da permitida para existir.")

else:
    print("Invalido.")

