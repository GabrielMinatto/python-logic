valor = float(input("Insira uma valor em metros para ser convertido: "))

def convertecm(medida):
    medida = valor*100
    print(f"valor em centímetros: {medida}cm")

def convertemm(medida):
    medida = valor*1000
    print(f"valor em milimetros: {medida}mm")

convertecm(valor)
convertemm(valor)
    
1