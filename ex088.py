from time import sleep


def counter(begin,end,pace):
    print('-' * 20)
    print(f'contagem de {begin} até {end} de {pace} em {pace}')
    if pace < 0:
        pace *= -1
    if pace == 0:
        pace = 1
    if begin < end:
        cont = begin
        while cont <= end:
            print(cont, end =' ', flush=True)
            sleep(0.3)
            cont += pace
        print('FIM')
    else:
        cont = begin
        while cont >= end:
            print(cont, end =' ', flush=True)
            sleep(0.3)
            cont -= pace
        print('FIM')
    

counter(1,10,1)
counter(10,0,2)
print('-' * 20)
print(f'Personaliza a contagem')
b = int(input("Início: "))
e = int(input("Fim: "))
p = int(input("Passo: "))
counter(b,e,p)