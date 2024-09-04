
financing = float(input('Qual é o valor do imóvel que deseja financiar? '))

salary = float(input('Qual o seu salário? '))

years = int(input('Em quanto tempo gostaria de quitar esse financiamento? '))

months = years * 12
monthly_payment = financing/months

if monthly_payment > (salary * 0.30):
    print(f'Não é póssivel fazer esse financiamento pois a parcela excede 30% do seu salário {monthly_payment:.2f}')
else:
    print(f'A parcela desse financiamento será de R$ {monthly_payment:.2f} e será paga durante {months} meses')