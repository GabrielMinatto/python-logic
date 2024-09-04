print('CADASTRE UMA PESSOA')
print('-' * 50)
legal_age = 0
men = 0
womensless20 = 0
start = True
while start:
    age = int(input("Idade: "))
    while age < 1:
        age = int(input("Idade: "))
    if age > 18:
        legal_age += 1
    gender = ' '
    while gender not in 'MF':
        gender = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if gender == 'F' and age > 20:
        womensless20 += 1
    elif gender == 'M':
        men += 1
    print('-' * 50)
    out = ' '
    while out not in 'SN':
        out = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if out == 'N':
            start = False
            break
print(f'Maior de 18 anos {legal_age}, Mulher com menos de 20 anos {womensless20}, total de homens foi {men}')
