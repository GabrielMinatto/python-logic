def contar_itens(lista):
    if not lista:
        return 0
    else:
        return 1 + contar_itens(lista[1:])

# Exemplo de uso
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(contar_itens(minha_lista))
