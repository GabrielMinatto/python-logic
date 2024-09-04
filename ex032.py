
n1 = int(input("digita tamanho do primeiro lado: "))
n2 = int(input("digita tamanho do segundo lado: "))
n3 = int(input("digita tamanho do terceiro lado: "))

if n1 < (n1 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    print('Podem formar um triangulo')
    if n1 == n2 and n2 == n3:
        print('é um triangulo equilatero')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print("Isósceles")
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print("escaleno")
else:
    print('Não podem formar um triangulo')

