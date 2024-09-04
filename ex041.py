
first_term = int(input("Primeiro termo: "))

reason = int(input("Razão: "))

décimo = first_term + (10 - 1) * reason

for i in range(first_term, décimo + reason, reason):
    print('{}'.format(i), end =', ')

print('Acabou')