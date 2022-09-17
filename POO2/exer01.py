class Carro:
    # Construtor
    def __init__(self, marca, modelo, placa):

        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
         print("-----------------")
         print(self.marca, self.modelo, self.placa)

# Criação dos Objetos
Carro1 = Carro ("Hyundai", "Creta", "fks-4057")
carro2 = Carro ("BMW", "X1", "Efw-6010")

Carro1.exibir_dados(),carro2.exibir_dados()
