pair_count = 0
n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))
print(f'O número 9 apareceu {n.count(9)} vezes')
print(f'O número 3 apareceu {n.index(3) + 1} posição')
for i in range(len(n)):
    if n[i] % 2 == 0:
        pair_count += 1 
print(f'A quantidade de número pares foi {pair_count}')