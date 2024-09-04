name = str(input("Digite seu nome completo: "))

nameUpper = name.upper()
nameLower = name.lower()
firstName = name.split()
letter = name.replace(' ', '')

print(f'Seu nome maiúsculo {nameUpper}')
print(f'seu noem minúsculo {nameLower}')
print(f'Seu primeiro nome tem {len(firstName[0])} letras') 
print(f'Seu nome tem completo tem {len(letter)} letras')