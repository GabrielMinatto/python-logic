
worker = {}

worker['Name'] = str(input('Nome: '))
birth_year = int(input('Ano de nascimento: '))
worker['Age'] = 2023 - birth_year
worker['CTPS'] = int(input('CTPS: '))
if worker['CTPS'] != 0:
    worker['Hiring'] = int(input('Ano de contratação: '))
    worker['Retirement'] = (worker['Hiring'] + 35) - birth_year
    worker['Salary'] = float(input('Salário: R$ '))

for k, v in worker.items():
    print(f'{k} tem valor {v}')