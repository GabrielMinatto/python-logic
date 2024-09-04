gender = str(input("Qual seu genero? Digite M para Masculino e F para Feminino: ")).strip().upper()[0]

while gender not in 'MmFf':
        gender = str(input(">>>ERRO! Qual seu genero? Digite M para Masculino e F para Feminino: ")).strip().upper()[0]
print('Sexo válido')

    
      