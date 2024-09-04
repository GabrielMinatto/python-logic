matrix = [[0, 0, 0,],[0, 0, 0,],[0, 0, 0]]
sum = 0
pair_sum = 0
highest = 0

for row in range(0,3):
    for col in range(0,3):
        matrix[row][col] = int(input(f'Digite um valor para posição [{row}, {col}]: '))
       
        if row == 1 and col == 0:
            
            highest = matrix[1][0]
        
        if highest < matrix[1][col]:
            
            highest = matrix[1][col]
        
        if col == 2:
            
            sum += matrix[row][2] 
        
        if matrix[row][col] % 2 == 0:
            
            pair_sum += matrix[row][col]
    
for row in range(0,3):
    for col in range(0,3):
        print(f'[{matrix[row][col]:^5}]', end = '')

    print()

print(f'A soma dos valores pares é {pair_sum}.')
print(f'A soma dos valores da terceira coluna é {sum}.')
print(f'O maior valor da segunda linha é {highest}.')