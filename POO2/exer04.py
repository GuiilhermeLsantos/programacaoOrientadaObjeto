class Aluno:

    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_notas(self, nota):
        if nota >= 0 and nota <= 10:
            self.notas.append(self.notas)
        else:
            print("Nota invalida")

    def calcular_media(self):
        for i in len(self.notas):
            