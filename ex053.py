
first_term = int(input("Primeiro termo: "))
reason = int(input("Razão: "))
first_term -= reason
cont = 1 
total = 0 
more_terms = 10
while more_terms != 0:
    total += more_terms
    while cont <= total:
        print(first_term, end = ', ')
        first_term += reason
        cont += 1 
    print('Pausa')
    more_terms = int(input('Digite quantos termo mais deseja ver ou digite [0] para sair do programa '))
print('Acabou')