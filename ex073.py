expression = list(input("Digite um expressão matemática: "))
print(expression)
parenteses_count = 0
for char in expression:
    if char == '(' or char == ')':
        parenteses_count += 1
print(parenteses_count)
if parenteses_count % 2 == 0:
    print("Expressão válida")
else:
    print("Expressao inválida")
