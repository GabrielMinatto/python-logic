preco = float(input("Qual é o preço do produtos? R$ "))

def descontar(preco):
    desconto = preco * 0.05
    precofinal = preco - desconto
    print(f"o produto que custava R${preco}, na promoção com 5% de desconto custará R${precofinal:.2f}")

descontar(preco)
