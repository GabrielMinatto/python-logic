
first_term = int(input("Primeiro termo: "))
reason = int(input("Razão: "))
first_term -= reason

decimo = first_term + (10 - 1) * reason

while first_term <= decimo:
    first_term += reason
    print(first_term, end = ', ')
print('Acabou')

# print(decimo)5
# for i in range(first_term, decimo + reason, reason):
#     print('{}'.format(i), end =', ')

# print('Acabou')