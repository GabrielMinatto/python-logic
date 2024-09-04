
number = int(input("Digite um número: "))
sum = number
count = 1
while True: 
    stop = str(input("Deseja continuar? [S/N]: "))
    if stop == "N":
        avg = sum/count
        print(f'A MÉDIA dos números foi de {avg:.2f} o MENOR deles foi {lower} e o MAIOR foi {higher}')
        break
    else:
        number = int(input("Digite um número: "))
        sum += number
        if count == 1:
            higher = number
            lower = number
        if number > higher:
            higher = number
        if number < lower:
            lower = number
        count+= 1


