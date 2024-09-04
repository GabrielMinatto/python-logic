soma = 0
count = 0 
for i in range(1, 7):
    number = int(input(f"Digite número inteiro {i}: "))
    if number % 2 == 0:
        soma += number
        count += 1
print(f'Voce informou {count} numeros e a soma de seus numero pares é {soma}')