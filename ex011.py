tempF = float(input("Informe a temperatura em fahrenheit que deseja ser convertida: "))
while tempF < -50 or tempF > 120:
    print(">>> TEMPRATURA INVÁLIDA")
    tempF = float(input("Informe a temperatura em fahrenheit que deseja ser convertida: "))

def converte(tempF):
    formula = (tempF - 32) * 5/9
    print(f"A temperuta em Fahrenheit é {tempF} em celsius é {formula:.2f}")

converte(tempF)
