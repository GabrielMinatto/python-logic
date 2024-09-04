def higher(lista):
    if not lista:
        return 0
    else:
        return higher(lista[1:])