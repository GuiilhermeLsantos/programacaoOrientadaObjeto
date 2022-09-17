#Implemente a classe Livro, conforme o diagrama a seguir. 
#No programa principal, crie um objeto da classe Livro.

class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):

        self.titulo = titulo
        self.autor = autor 
        self.quantidade_paginas = quantidade_paginas
    
livro1 = Livro ("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
livro2 = Livro ("Poeira em alto mar", "Alan Bida", 100)

print(livro1.titulo)
print(livro1.autor)
print(livro1.quantidade_paginas)