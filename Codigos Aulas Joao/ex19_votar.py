ano_nascimento = int(input("Qual o seu Ano de Nascimento? : "))
idade = 2025 - ano_nascimento 

if idade  >=18 or 18:
    print("Voce esta permitido a Votar! ")

elif idade <=17:
    print("Voce nao esta permitido a Votar!")

else:
    print("Invalido.")