city = str(input("Qual o nome da sua cidade: "))

cityLower = city.lower().split()

if ('santo' in cityLower[0]):
    print(f'A cidade de {city} começa com a palavra Santo')
else: 
    print(f"A cidade de {city} não começa com a palavra Santo")


