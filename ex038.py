import time

for i in range(5, -1,-1):
    print(f'contagem regressiva {i}')
    time.sleep(1)
    if i == 0:
        print('***FOGOS DE ARTIFICIO***')