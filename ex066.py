
products = ('Pão de forma', 1.5,'Iogurte', 12.50,'Leite', 4.5,'Refrigerante', 6.9)

for pos in range(len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end = '')
    else:
        print(f'R$ {products[pos]:>2}')
    


