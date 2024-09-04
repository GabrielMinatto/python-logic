travel_distance = int(input('Digite a distancia da sua viagem em km: '))
if travel_distance <= 200:
    price = travel_distance * 0.5
    print(f'Sua viagem de {travel_distance}km custará R$ {price}')
elif travel_distance > 200:
    price = travel_distance * 0.45
    print(f'Sua viagem de {travel_distance}km custará R$ {price}')