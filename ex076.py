matrix = [[0, 0, 0,],[0, 0, 0,],[0, 0, 0]]

for row in range(0,3):
    for col in range(0,3):
        matrix[row][col] = int(input(f'Digite um valor para posição [{row}, {col}]: '))
for row in range(0,3):
    for col in range(0,3):
        print(f'[{matrix[row][col]:^5}]', end = '')
    print()