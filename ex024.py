name = str(input('Digite seu nome: '))
nameList = name.split()
index = len(nameList)

#print(index)
print(f'Primeiro nome {nameList[0]} e último nome {nameList[index - 1]}')