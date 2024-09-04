preco = float(input("Preço do produtos R$ "))
while preco <= 0:
    print(">>> INSIRA UM PREÇO VÁLIDO")
    preco = float(input("Preço do produtos R$ "))

def calculaPrecos(preco):
    precov = preco * 0.1
    precofinal = preco - precov
    precop = preco *1.08
    print(f"O preço do produto é R$ {preco}, a vista ele sai por R$ {precofinal} e parcelado ele sai por R$ {precop}")

calculaPrecos(preco)

    