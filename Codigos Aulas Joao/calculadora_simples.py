# calculadora simples

while True:
    operacao = str(input("Escolha a Operaçao de (+, -, *, /): "))
    comando = str(input("Digite 'sair' para Parar( e digite qualquer coisa para continuar): "))
    if comando.lower() == "sair":
        print("Bye Bye!")
        break

    elif operacao.lower() == "+":
        primeironumero = int(input("Primeiro Numero: "))
        segundonumero = int(input("Segundo Numero: "))
        resultado = primeironumero + segundonumero
        print(f"{primeironumero} + {segundonumero} = {resultado} ")
        pass

    elif operacao.lower() == "-":
        primeironumero = int(input("Primeiro Numero: "))
        segundonumero = int(input("Segundo Numero: "))
        resultado = primeironumero - segundonumero 
        print(f"{primeironumero} - {segundonumero} = {resultado}")
        pass

    elif operacao.lower() == "*":
        primeironumero = int(input("Primeiro Numero: "))
        segundonumero = int(input("Segundo Numero: "))
        resultado = primeironumero * segundonumero 
        print(f"{primeironumero} * {segundonumero} = {resultado}")
        pass

    elif operacao.lower() == "/":
        primeironumero = int(input("Primeiro Numero: "))
        segundonumero = int(input("Segundo Numero: "))
        resultado = primeironumero // segundonumero 
        print(f"{primeironumero} / {segundonumero} = {resultado}")
        pass
    else:
        print("Invalido.")
    pass

