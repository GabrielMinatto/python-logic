import random
import time

games = []
numbers = []

count = int(input('Quantos jogos você quer sortear? '))

for i in range(0,count):
    while len(numbers) < 6:
        number = random.randint(1,60)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    games.append(numbers[:])
    numbers.clear()
count = 1
for game in games:
    print(f'Jogo {count}: {game}')
    count += 1
    time.sleep(0.6)