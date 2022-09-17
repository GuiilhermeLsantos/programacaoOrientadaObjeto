#Preencha um dicionário com os dados de 5 alunos.
# -  Utilize o ra do aluno como chave e uma lista de três notas como valor.
# -  Solicite os dados ao usuário.
#Percorra o dicionário e exiba a média de cada aluno.

#Exemplo: 
#Veja um exemplo da estrutura do dicionário.
#{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}

from stat import IO_REPARSE_TAG_APPEXECLINK

alunos = {}

for n in range(5):
    ra = input("Digite RA: ")
    nota = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite nota 2: "))
    nota3 = float(input("Digite a nota 3: "))

    alunos [ra] = [nota,nota2,nota3]

for n in alunos:
    media = sum(alunos[n]) //3

    print (media)
