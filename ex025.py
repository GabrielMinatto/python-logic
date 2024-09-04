import random

sorted_number = random.randrange(1,6)

print(sorted_number)
while True:
    guess = int(input("Digite um palpite de 1 à 5: "))
    if not(1 <= guess <= 5):
        print('>>Erro!! digite um número dentro do intervalo de 1 à 5')
    elif(guess == sorted_number):
        print("Parabéns você acertou!!!")
        break
    else:
        print("Você errou! tente novamente")





