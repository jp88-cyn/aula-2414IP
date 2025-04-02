# exemplo de contador simples
#contador = 0 
#while contador < 5:  # se o contador for abaixo de 5 ele vai continuando
#    print(f"Contagem: {contador}")
#    contador += 1 # adiciona 1 pra contagem 

#senha = "1234" # define a senha aqui mesmo
#tentativa = "" # tentativa do usuario

#while tentativa != senha: # O ! e caso seja diferente do que é preciso pra continuar, com o while 
    #tentativa = input("Digite sua Senha: ") 
#print("Acesso concedido!")


#Exemplo de Loop infinito
while True:
    comando = input("Digite 'sair' para parar: ")
    if comando.lower() == "sair":
        print("Goodbye!")
        break
    print(f"Voce digitou: {comando}")
