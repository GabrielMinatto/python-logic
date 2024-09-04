numbers = [[], []]
for i in range(1,8):
    number = int(input(f'Digite o {i}o número: '))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
        

print(f'O valores Pares digitados foram {sorted(numbers[0])}')
print(f'O valores Ímpares digitados foram {sorted(numbers[1])}')