

number = int(input('Digite o número: '))
count = 1 
fibonacci = 1
antecessor = 0
while number >= count:
    fibonacci = fibonacci + antecessor
    antecessor = fibonacci - antecessor
    count = count + 1
    print(fibonacci, end=', ')

# 1 + 1 = 2
# 2 + 1 = 3
# 3 + 2 = 5 
# 5 + 3 = 8
# 8 + 5 = 13


