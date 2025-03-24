km = float(input("Qual a Quantidade de Kilometros percoridos?: "))
dias = int(input("Qual os dias em que o Carro continou Alugado?: "))

preço_dia = 90 * dias
preço_km = 0.20 * km
total = preço_dia + preço_km

print(f"O Valor a pagar é de {total}.")
