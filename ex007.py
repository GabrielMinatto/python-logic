largura = float(input("Largura da parede em metros: "))
altura = float(input("Altura da parede em metros: "))

def calculaArea(largura,altura):
    area = largura * altura
    print(f"A área da parede é {area} m2")
    return area

def qtdtinta(area):
    tinta = area / 2
    print(f"A quantidade de tinta necessária para pintar essa parede é {tinta}L")
    return tinta

qtdtinta(calculaArea(largura,altura))

