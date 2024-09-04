def vote(year_birth):
    age = 2023 - year_birth
    if age >= 18:
        return f"com {age} anos VOTO OBRIGATÓRIO"
    if age == 16:
        return f"VOTO OPCIONAL"
    if age < 16:
        return f"VOTO NEGADO"
    


year_of_birth = int(input('Ano de nascimento: '))

print(vote(year_of_birth))