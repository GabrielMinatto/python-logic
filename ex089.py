def highest(*num):
    cont = highest = 0
    print('Analisando os valores passados...')
    for value in num:
        print(f'{value} ', end ='')
        if cont == 0:
            highest = value
        elif highest < value:
            highest = value
        cont += 1
    print(f'Foram passados {cont} valores')
    print(f'O maior valor foi {highest}')

highest(2, 9, 4, 5, 7, 1)
highest()