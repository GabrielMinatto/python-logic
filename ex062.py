tuple = ("zero",'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')

number = int(input('Digite um número entre 0 e 10: '))
while not (0 <= number <= 10):
    number = int(input('Digite um número entre 0 e 10: '))
print(tuple[number])