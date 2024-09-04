
nota1 = float(input("Insira sua nota1: "))
while nota1 < 0: 
        print(">>>INSIRA UMA NOTA VÁLIDA!!")
        nota1 = float(input("Insira sua nota1: "))

nota2 = float(input("Insira sua nota2: "))
while nota2 < 0:
        print(">>>INSIRA UMA NOTA VÁLIDA!!")
        nota2 = float(input("Insira sua nota2: "))

media = (nota1 + nota2)/2

print(f"Suas notas foram {nota1} e {nota2} sua média ficou {media}")