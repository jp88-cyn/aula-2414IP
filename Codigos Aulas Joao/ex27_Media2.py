nome = input("Qual o seu Nome? : ")
nota01 = float(input("Qual a sua nota em Biologia? : "))
nota02 = float(input("Qual a sua nota em Matematica? : "))

media = nota01 + nota02
mediatotal = media / 2

if mediatotal == 7.0 or mediatotal >= 7.0:
    print(f"Media de 7.0 pra cima: APROVADO")
    pass

elif mediatotal >= 5.0 or mediatotal == 6.9:
    print("Media entre 5.0 a 6.9: RECUPERAÇAO")

elif mediatotal <= 4.9 or mediatotal == 4.9:
    print(f"Media ate 4.9: REPROVADO")