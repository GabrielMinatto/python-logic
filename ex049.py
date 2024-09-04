num1 = int(input("Digite o Primeiro valor: "))
num2 = int(input("Digite o Segundo valor: "))


while True:
    operation = int(input("[1] para somar \n[2] para Multiplicar \n[3] para Maior \n[4] Novos valores \n[5] Sair do programa\n"))
    if operation == 1:
        sum = num1 + num2
        print(f'{num1} + {num2} = {sum}')
    elif operation == 2:
        mult = num1 * num2
        print(f'{num1} X {num2} = {mult}')
    elif operation == 3:
        if num1 > num2:
            higher = num1
            lower = num2
            print(f'num1: {higher} > num2: {lower}')
        if num2 > num1:
            higher = num2
            lower = num1
            print(f'num2: {higher} > num1: {lower}')
    if operation == 4:
        num1 = int(input("Digite o Primeiro valor: "))
        num2 = int(input("Digite o Segundo valor: "))
    if operation == 5:
        print('FIM DO PROGRAMA')
        break
    