total_age = 0
avg_age = 0
oldest_man_age = 0
oldest_man_name = ''
less20_woman = 0 

for i in range(1,5):
    print(f'{i}ª pessoa')
    name = str(input("Nome:"))
    age = int(input("Idade: "))
    gender = str(input("Genero  [M/F]: "))
    total_age += age
    if i == 1 and gender in 'Mm':
        oldest_man_name = name
        oldest_man_age = age
    elif gender in 'Mm' and oldest_man_age < age:
        oldest_man_name = name
        oldest_man_age = age
    elif gender in 'Ff' and age < 20:
        less20_woman += 1

avg_age = total_age/4

print(f'A média de idade do grupo é de {avg_age:.2f} anos')
print(f'O homem mais velho tem {oldest_man_age} anos e se chama {oldest_man_name}')
print(f'Ao todo são {less20_woman} mulheres com menos de 20 anos')

