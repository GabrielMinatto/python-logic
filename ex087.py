def write(txt):
    print('-' * len(txt))
    print(f"{txt:^{len(txt)}}")
    print('-' * len(txt))

msg = str(input("Escreva uma mensagem: "))

write(msg)