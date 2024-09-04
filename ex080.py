student = dict ()
file = list ()
student['name'] = str(input('NOME: '))
student['grade'] = float(input('MÉDIA: '))
if student['grade'] >= 7:
    student['situation'] = 'APROVADO'
else:
    student['situation'] = 'REPROVADO'
file.append(student.copy())

print(f'Nome: {student["name"]}')
print(f'A média é {student["grade"]}')
print(f'Situação do aluno é {student["situation"]}')
