days = int(input("Informe a quantidade de dias que você ficou com o carro: "))
kilometer = float(input("Informe quantos quilometros você rodou: "))
daysPrice = days * 60
kiloPrice = kilometer * 0.15

print(f"Você ficou com o carro por {days} e rodou {kilometer} logo você deverá pagar {daysPrice + kiloPrice}")



