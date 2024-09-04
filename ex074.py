people = []
data = []
heaviest = lighter = 0
while True:
    data.append(str(input("NOME: ")))
    data.append(float(input("PESO: ")))
    if len(people) == 0:
        heaviest = lighter = data[1]
    else: 
        if data[1] > heaviest:
            heaviest = data[1]
        if data[1] < lighter:
            lighter = data[1]
    people.append(data[:])
    data.clear()
    stop = str(input("Deseja continuar [S/N] ")).strip().upper()[0]
    while stop not in "SN":
        stop = str(input("Deseja continuar [S/N] ")).strip().upper()[0]
    if stop == "N":
        break

print(f'A quantidade de pessoas cadastradas foi {len(people)}')
print(f'O MAIOR peso foi de {heaviest}Kg. Peso de ', end='')
for person in people:
    print(person)
    if person[1] == heaviest:
        print(f'{person[0]} ', end='')
    
print(f'\nO MENOR peso foi de {lighter}Kg. Peso de ', end='')
for person in people:
    if person[1] == lighter:
        print(f'{person[0]} ', end='')




