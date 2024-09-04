people = list()
person = dict()
sum_age = 0 
while True:
    person.clear()
    person["name"] = str(input("Nome: "))
    person["gender"] = ""
    person["gender"] = str(input("Gênero [M/F]: ")).strip().upper()[0]
    while person["gender"] not in "FM":
        person["gender"] = str(input("Gênero [M/F]: ")).strip().upper()[0]
    person["age"] = int(input("Idade: "))
    people.append(person.copy())
    sum_age += person["age"]
    stop = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    while stop not in "SN":
        stop = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if stop == "N":
        break
avg_age = sum_age/len(people)
print(f"Dic = {person}")
print(f"list = {people}")
print('-=' * 30)
print(f'total de pessoas cadastradas {len(people)}')
print(f'Média das idades {avg_age:.2f}')

for per in people:
    if per['gender'] in 'F':
        print(f'Lista de mulheres {per["name"]} ', end = '')

for per in people:
    if per['age'] >= avg_age:
        print(f'Pessoas com idade acima da média: {per["name"]}', end= '') 
