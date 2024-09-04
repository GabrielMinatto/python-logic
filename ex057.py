
while True:
    c = 1 
    print('-' * 80)
    number = int(input("Quer ver a tabuada de qual valor? "))
    if number < 0:
        print('FIM DA EXECUÇÃO')
        break
    else: 
        while c <= 10:
            print(f'{number} X {c} = {number*c}')
            c += 1