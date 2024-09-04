numbers  = []

while True:
    number = int(input('Digite um valor: '))
    if number in numbers:
        print('Valor duplicado')
    else:
        numbers.append(number)
    stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if stop == 'N':
        break
if 5 in numbers:
    print('o valor CINCO está presente na lista')
else:
    print('O valor CINCO não está presente na lista')

numbers.sort(reverse=True)

print(f'{numbers}')