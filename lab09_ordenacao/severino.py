# lab 9.6
while True:
    try:
        codigos_livros = []
        livros = int(input())
        for i in range(livros):
            codigo_livro = input()
            codigos_livros.append(codigo_livro)
        for j in sorted(codigos_livros):
            print(j)
    except EOFError:
        break