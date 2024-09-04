number = int(input("diga um número inteiro: "))
division = 0
for i in range(1, number+1):
    if number % i == 0:
        division +=1

if division == 2:
    print(f'{number} é um número primo')
else:
    print(f'{number} NãO é um número primo')