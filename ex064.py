from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
highest = 0
lowest = 0

for i in range(len(n)):
    if i == 1:
        highest = n[i]
        lowest = n[i]
    if n[i] > highest:
        highest = n[i]
    if n[i] < lowest:
        lowest = n[i]
print(n)
print(highest, lowest)
