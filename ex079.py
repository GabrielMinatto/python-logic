
students = []
grades = []

while True: 
    name = str(input('NOME: '))
    grade1 = float(input('NOTA 1: '))
    grade2 = float(input('NOTA 2: '))
    avg_grade = (grade1 + grade2)/2
    students.append([name, [grade1, grade2], avg_grade])
    stop = str(input('Deseja cotinuar [S/N] ')).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input('Deseja cotinuar [S/N] ')).strip().upper()[0]
    
    if stop == 'N':
        break
   
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA:>8"}')
print('-'*26)

for i, student in enumerate(students):
    print(f'{i:<4}{student[0]:<10}{student[2]:8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostra as notasd e qual aluno? (999 interrompe)'))
    if opc == 999:
        print('SAINDO...')
        break
    if opc <= len(students) - 1:
        print(f'Notas de {students[opc][0]} são {students[opc][1]}')