from random import randint
num = []

def raffle():
    for i in range(0,5):
        num.append(randint(1,10))

def sum(lst):
    sum = 0
    cont = 0
    while cont < len(lst):
        if num[cont] % 2 == 0:
            sum += num[cont]
            print(f'{num[cont]} +', end=' ')
            cont += 1
        else:
            cont += 1
    print(f'valor total {sum}')

raffle()
print(num)
sum(num)
