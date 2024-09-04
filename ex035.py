n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro numero inteiro: '))

if n1 > n2:
    print(f'n1 {n1} é maior que n2 {n2}')
elif n2 > n1:
    print(f'n2 {n2} é maior que n1 {n1}')
else:
    print(f'Os números {n1, n2} são iguais')