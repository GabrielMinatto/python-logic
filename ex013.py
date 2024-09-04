import math   

catetoOposto = float(input("Informe a medida do cateto oposto: "))
catetoAdj = float(input("Informe a medida do cateto adjacente: "))

hipotenusa = math.pow(catetoOposto,2) + math.pow(catetoAdj,2)
hipotenusa = math.sqrt(hipotenusa)
print(f"A hipotenusa desse triangulo retangula de medidas {catetoOposto}cm e {catetoAdj}cm é {hipotenusa}cm")
