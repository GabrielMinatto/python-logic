number_count = 0

while number_count < 3:
    number_count += 1
    number = int(input('Digite 3 valores números inteiros: '))
    if number_count == 1: 
        minor_number = number
        highest_number = number
    elif number > highest_number:
        highest_number = number
    elif number < minor_number:
        minor_number = number
        

print(f'O menor número dos três é {minor_number} e o maior é o {highest_number}')

