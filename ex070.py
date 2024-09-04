
numbers = []

for i in range(0, 5):
    number = int(input("digite um valor: "))
    if i == 0 or number > numbers[-1]:
        numbers.append(number)
    else:
        pos = 0
        while pos < len(numbers):
            if number <= numbers[pos]:
                numbers.insert(pos,number)
                break
            pos += 1
print(numbers)


    
        



    
    

