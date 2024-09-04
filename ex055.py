soma = 0

while True:
    number = int(input("Digite um numero ou digite 999 para sair do loop: "))
    if number == 999:
        break
    else:
        soma += number
print(soma)