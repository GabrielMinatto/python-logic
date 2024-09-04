
numbers = list()
highest = 0 
lower = 0 
for cont in range(0,5):
    numbers.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        highest = lower = numbers[cont]
    else:
        if numbers[cont] > highest:
            highest = numbers[cont]
        if numbers[cont] < lower:
            lower = numbers[cont]

print(numbers)
for i, n in enumerate(numbers):
    if n == highest:
        print(f'{i}...', end = '')
    if n == lower:
        print(f'{i}...', end = '')
print(f'O MAIOR valor da lista foi {highest} nas posições ', end = '')
print(f'O MENOR valor da lista foi {lower} nas posições ', end = '')