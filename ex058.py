import random
wins = 0
while True:
    number = int(input("Diga um valor: "))
    your_pick = ' '
    while your_pick not in 'PpIi':
        your_pick = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    sorted = random.randint(1,10)
    result = sorted + number
    if result % 2 == 0 and your_pick == 'P':
        print(f'VOCÊ VENCEU!! Você jogou {number} e o computador {sorted}. Total de {result} deu PAR')
        wins += 1
    elif result % 2 != 0 and your_pick == 'I':
        print(f'VOCÊ VENCEU!! Você jogou {number} e o computador {sorted}. Total de {result} deu IMPAR')
        wins += 1
    else:
        print(f'GAME OVER Você jogou {number} e o computador {sorted}. Total de {result} deu', end=' ')
        print('IMPAR' if your_pick == 'P' else 'PAR')
        print(f'Você venceu {wins} vezes')





