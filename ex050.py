
number = int(input("Digite o número que deseja calcular o fatorial: "))
count = number
f = 1 
print('Caculando', number,'! = ', end = '' )
while count > 0:
    print(f'{count}', end = '')
    print(' x ' if count > 1 else ' = ', end = '')
    f *= count
    count -= 1
print(f)
    # print(f'{f}! = ')
    # print(f'{count}', end = ' X ')