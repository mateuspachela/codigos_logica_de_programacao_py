#lab9.5

inscricoes_sim = []
inscricoes_nao = []

# Leitura das inscrições
while True:
    inscricao = input()
    if inscricao == "FIM":
        break
    nome, opcao = inscricao.split()
    if opcao == "YES":
        inscricoes_sim.append(nome)
    elif opcao == "NO":
        inscricoes_nao.append(nome)

maior_qtd_letras = -1
dicionario_qtd_letras_nome = {}

for pessoa in inscricoes_sim:
    qtd_letra = len(pessoa)
    if pessoa not in dicionario_qtd_letras_nome:
        dicionario_qtd_letras_nome[pessoa] = qtd_letra

    if qtd_letra > maior_qtd_letras:
        maior_qtd_letras = qtd_letra

candidatos_amigo = []
for nome, tamanho in dicionario_qtd_letras_nome.items():
    if tamanho == maior_qtd_letras:
        candidatos_amigo.append(nome)

indice_inscricao_priorizada = 999
for candidato in candidatos_amigo:
    if inscricoes_sim.index(candidato) < indice_inscricao_priorizada:
        indice_inscricao_priorizada = inscricoes_sim.index(candidato)

amigo = inscricoes_sim[indice_inscricao_priorizada]


# Impressão dos resultados
for nome in sorted(set(inscricoes_sim)):
    print(nome)
for nome in sorted(set(inscricoes_nao)):
    print(nome)

print()
print(f'Amigo do Habay:')
print(f'{amigo}')