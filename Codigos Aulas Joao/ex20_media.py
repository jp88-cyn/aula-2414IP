
nome = input("Qual o seu Nome? : ")
nota01 = float(input("Qual a sua nota em Biologia? : "))
nota02 = float(input("Qual a sua nota em Matematica? : "))

mediatotal = nota01 + nota02 / 2

if mediatotal <=7.0:
    print(f"{nome}, voce teve uma media de {mediatotal} , Um proveito ruim dos seus estudos.")

elif mediatotal == 7.0:
    print(f"{nome}, voce teve uma media de {mediatotal} , Um proveito bom dos seus estudos. ")

elif mediatotal >= 7.0:
    print(f"{nome}, voce teve uma media de {mediatotal} , Um proveito muito bom dos seus estudos!")

else:
    print("Invalido XD")