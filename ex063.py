teams = ('Botafogo','Palmeiras', 'bragantino','Grêmio', 'Atlético-MG','Flamengo','Athletico-PR','Fluminense','Fortaleza','São Paulo','Cuiabá','Corinthians','Internacional','bahia',
         'Santos','Cruzeiro','Vasco da Gama','Goiás','Coritiba','América-MG')

pos = 1
print(f'Os cinco primeiros colocados são respectivamente:')
for team in  range(0,5):
    print(f'{pos} - {teams[team]}')
    pos += 1


pos = 17
print(f'Os quatro ultimos colocados são respectivamente:')
for last in range(-4,0):
    print(f'{pos} - {teams[last]}')
    pos += 1


print(sorted(teams))
print('O Grêmio está na posição: ', teams.index('Grêmio') + 1 )