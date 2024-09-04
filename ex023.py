phrase = str(input("Digite uma frase: ")).upper()

print('A letra A parece {}'.format(phrase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(phrase.find('A')+1))
print('A última letra A aprareceu na posição {}'.format(phrase.rfind('A')+1))
