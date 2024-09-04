import datetime

current_year = datetime.datetime.now().year
of_legal_age = 0
minor = 0 
for i in range(1, 8):
    year_birth = int(input(f"Em que ano a {i} nasceu? "))
    age = current_year - year_birth
    if age >= 18:
        of_legal_age += 1
    else:
        minor += 1
print(f'Ao todo tivemos {of_legal_age} pessoas maior de idade')
print(f'e também tivemos {minor} pessoas menor de idade')