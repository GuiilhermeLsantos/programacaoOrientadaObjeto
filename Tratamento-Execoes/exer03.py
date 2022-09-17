#Exercício 03
#Crie um dicionário para armazenar um cadatro de alunos. 
#Utilize como chave o RA do aluno e como valor o nome do aluno.
#Os dados devem ser informados pelo usuário
#O RA de cada aluno deve ser composto por uma string de exatamente 7 caracteres.
#Caso o RA informado não esteja no formato correto, deve ser gerada uma exceção do tipo ValueError (utilize a instrução raise).
#Caso o RA informado já esteja cadastrado no dicionário, deve ser gerada uma exceção do tipo TypeError (utilize a instrução raise).


dicionario_alunos = {}  # dicionário vazio
try:
    for n in range(3):            
        ra = input('RA: ')
        if len(ra) !=7:
            raise ValueError
        if ra in dicionario_alunos:
            raise TypeError
    nome = input('Nome: ')
    dicionario_alunos[ra] = nome  # insere no dicionário

except ValueError:
    print('Erro: Ra não tem 7 caracter')
except TypeError:
    print('Erro: Ra já cadastrado')
except Exception:
    print('Erro: Algo de errado não está certo')
else:
    print(dicionario_alunos)