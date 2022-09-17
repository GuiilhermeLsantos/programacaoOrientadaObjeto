#Crie dois objetos da classe Aluno
#Utilize o método inserir_nota para inserir algumas notas para os alunos.
#Utilize o método calcular_media para calcular a média de cada aluno.

class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media

aluno1 = Aluno(123456, 'Paulo', '2A')
aluno2 = Aluno(456789, 'João', '2A')
aluno3 = Aluno(678765, 'Ana', '2A')

aluno1.inserir_nota(8)
aluno1.inserir_nota(7)

aluno2.inserir_nota(10)
aluno2.inserir_nota(6)

aluno3.inserir_nota(7.5)

print(aluno1.nome, aluno1.calcular_media())
print(aluno2.nome, aluno2.calcular_media())
print(aluno3.nome, aluno3.calcular_media())