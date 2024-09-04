

withdraw = int(input('Qual o valor de que deseja sacar: R$'))
total = withdraw
ballot = 50
total_ballot = 0
while True:
    if total >= ballot:
        total -= ballot
        total_ballot += 1
    else:
        if total_ballot > 0:
            print(f'Total de {total_ballot} cédulas de R${ballot}')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        total_ballot = 0
        if total == 0:
            break



