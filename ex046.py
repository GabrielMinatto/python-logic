
for i in range(1, 6):
    weight = float(input(f"Peso da {i} pessoa: "))
    if i == 1:
        heaviest = weight
    elif weight > heaviest:
        lighter = weight
        heaviest = weight
    elif weight < lighter:
        lighter = weight

print(f"O maior peso lido foi de {heaviest}")
print(f"O menor peso lido foi de {lighter}")