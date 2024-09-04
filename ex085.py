players = list()
player = dict()
goals = list()


while True:
    tot_goals = 0
    player.clear()
    goals.clear()
    
    player["name"] = str(input("Nome do jogador: "))
    
    player["matches"] = int(input("Quantas partidas ele jogou: "))
    
    for i in range(player["matches"]):
        goal = int(input(f"Quantos gols na partida {i + 1}: "))
        tot_goals += goal
        goals.append(goal)
        player["goals"] = goals.copy()
    
    player["total"] = tot_goals
    players.append(player.copy())
    
    while True:
        stop = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if stop in 'SN':
            break
        print('ERRO!')
    if stop == 'N':
        break

print('-=' * 30)
print(players)
print('-=' * 30)

for i in player.keys():
    print(f'{i:<15}', end = '')
print()
print('-=' * 30)
for  k, v in enumerate(players):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    search = int(input('Mostrar dados de qual jogador? '))
    if search == 999:
        break
    if search >= len(players):
        print(f'ERRO')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {players[search]["name"]}:')
        for i, g in enumerate(players[search]["goals"]):
            print(f'Na partida {i + 1} fez {g} gols.')
    print('-' * 30)

