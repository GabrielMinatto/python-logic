phrase = input("Escreva uma frase para verificar se ela é um palíndromo: ")
phrase2 = phrase.replace(' ', '')
inverse = ''
inverse = phrase2[::-1]

# for i in range(len(phrase2) - 1, -1, -1):
#     inverse += phrase2[i]

if inverse == phrase2:
    print(f"{inverse} é um palindromo de {phrase2}")
else:
    print(f'{phrase} nao é um palindromo')



