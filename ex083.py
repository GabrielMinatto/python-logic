player = dict()
goals = list()
tot_goals = 0
player["name"] = str(input("Nome do jogador: "))
player["matches"] = int(input("Quantas partidas ele jogou: "))
for i in range(player["matches"]):
    goal = int(input(f"Quantos gols na partida {i + 1}: "))
    tot_goals += goal
    goals.append(goal)
    player["goals"] = goals
player["total"] = tot_goals
print('-=' * 30)
print(player)
print('-=' * 30)
for k, v in player.items():
    print(f'o campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {player["name"]} jogou {player["matches"]}.')

for i in range(player["matches"]):
    print(f'Na partida {i + 1}, ele fez {goals[i]}')
print(f'Fez um total de {player["total"]} gols.')

