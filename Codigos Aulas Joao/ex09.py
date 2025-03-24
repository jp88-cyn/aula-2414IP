altura = float(input("Qual a sua Altura: "))
peso = int(input("Qual o seu Peso?:"))
altura2 = altura * altura
IMC = peso / altura2
print(IMC)

if IMC <=0 and 18.4:
    print(f"Voce esta Abaixo do Peso, com {IMC:.3} de IMC.")
    

elif IMC <= 18.5 and 24.9:
    print(f"Voce esta na Media de Peso, Com {IMC:.3} de IMC.")
    

elif IMC <=25 and 30:
    print(f"Voce esta em Sobrepeso, Com {IMC:.3} de IMC.")
    

elif IMC <=31 and 35:
    print(f"Voce esta com Sobrepeso Classe 1, com {IMC:.3} de IMC.")
    

elif IMC <=36 and 40:
    print(f"Voce esta com Sobrepeso Classe 2, Com {IMC:.3} de IMC. ")


elif IMC >= 40:
    print(f"Voce com Sobrepeso Classe 3, com {IMC:.3} de IMC.")
    pass


else:
    print("Invalido.")

# eu talvez tenha resolvido isso em casa (ta na pasta de VSCODEJonatham)

