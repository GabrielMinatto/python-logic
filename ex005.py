valor = int(input("Insira um valor para saber sua tabuada: "))
while valor < 0:
    print(">>>Insira um valor válido")
    valor = int(input("Insira um valor para saber sua tabuada: "))
for i in range(1, 11):
    mult = valor * i
    print(f"{valor} X {i} = {mult}")

