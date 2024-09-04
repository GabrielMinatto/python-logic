salary = int(input('Qual o valor do seu salário R$? '))

if salary > 1250:
    increase = salary * 1.1
    print(f'Seu aumento será de {increase}')
else:
    increase = salary * 19.15
    print(f'Seu aumento será de {increase}')
