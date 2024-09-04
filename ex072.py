numbers = []
pair = []
odd = []
while True:
    number = int(input('Digite um valor: '))
    if number in numbers:
        print('Valor duplicado')
    else: 
        numbers.append(number)
        if number % 2 == 0:
            pair.append(number)
        if number % 2 != 0:
            odd.append(number)
    stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if stop == 'N':
        break

print('-' * 50)
print(f'Lista com TODOS os números {numbers}')
print('-' * 50)
print(f'Lista com os números PARES {pair}')
print('-' * 50)
print(f'Lista com os números ÍMPARES {odd}')
        