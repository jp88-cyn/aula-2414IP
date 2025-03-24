# Programa que le se a Idade do Usuario e Criança, Adolescente, Jovem, Adulto ou Idoso. 
# Adicionei mais Coisas so pq sim 

idade = int(input("Qual a Sua Idade: "))

if idade <= -0 or 0:
    print("Voce nao EXISTE!!!")
    pass

elif idade >= 1 or idade <=5:
    print("Voce e um Bebe.")
    pass

elif idade >=6 or idade <=8:
    print("Voce e uma Criança!")
    pass

elif idade >=9 or idade <=17:
    print("Voce e um Adolescente!")
    pass





# O If e sempre o primeiro a iniciar sendo o "Se" da coisa, O Else e para caso ocorra algo 
# alem do if tipo "Outro", e o Elif pode ser usado varias vezes como uma junçao do Else+If.