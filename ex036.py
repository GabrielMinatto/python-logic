import datetime

today = datetime.date.today()

year = today.year

year_of_birth = int(input('QUal seu ano de nascimento: '))

if (year - year_of_birth) == 18:
    print('Está na hora de se alistar')
elif (year - year_of_birth) > 18:
    print('Ja passou da hora de se alistar')
else:
    print('ainda não está na hora de se alistar')