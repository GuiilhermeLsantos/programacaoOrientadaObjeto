class Cachorro:
    #Construtor da Class
    def __init__(self, nome, idade, raca):
        # Atributos da Class
        self.nome = nome 
        self.idade =  idade
        self.raca = raca

#Exibir Atributos e valores
    def exibir(self):
        print("nome:", self.nome)
        print("idade:", self.idade)
        print("raca:", self.raca)

#Definição Método da Class
    def latir(self):
        print("Cachorro",self.nome ,"latiu")

    def dormir(self):
        print("Cachorro",self.nome,"dormiu")

#Usuario Imformando
nome = input("nome:")
idade = int(input("idade:"))
raca = input("raca:")

# Criação de Objetos
Cachorro1 = Cachorro("Rex", 4, "Pitbull")
Cachorro2 = Cachorro("Max", 2, "Shitzus")

#Execução de Método da Class
Cachorro1.latir()
Cachorro2.latir()
Cachorro1.exibir()

#Alteração de Atributo de Objeto
Cachorro1.idade = 5
