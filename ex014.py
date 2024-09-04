import math

angulo = int(input("informe o grau do angulo que deseja calculao Seno, Cosseno e a Tagente: "))


seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O Seno, Cosseno e Tangente do angulo {angulo} são respectivamente {seno:.2f}, {cos:.2f} e {tan:.2f}")