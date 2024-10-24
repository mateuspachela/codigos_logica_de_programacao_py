#lab9.8

entrada = input().split() # recebe o N e K

numero_alunos = int(entrada[0])
numero_sorteado = int(entrada[1])
alunos = []
for i in range(numero_alunos): # loop para adicionar a lista de alunos os alunos que se encontram
    aluno = input()
    alunos.append(aluno)

alunos.sort() # ordena a lista em ordem alfabetica

print(alunos[numero_sorteado - 1]) # printa a posicao que corresponde ao numero sorteado