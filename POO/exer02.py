#Crie uma classe que representa um triângulo.

#Crie um programa que utilize esta classe. 
#O programa deve pedir ao usuário que informe as medidas dos três lados de um triângulo.
# Depois deve criar um objeto com essas medidas e exibir seu perímetro.

class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):

        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
        

lado_a = float(input("lado_a: "))
lado_b = float(input("lado_b: "))
lado_c = float(input("lado_c: "))

#Criar o objeto
Triangulo1 = Triangulo(lado_a, lado_b, lado_c)

print(Triangulo1.calcular_perimetro())
