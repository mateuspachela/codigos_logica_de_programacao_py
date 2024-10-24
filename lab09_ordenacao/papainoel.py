qtd_nomes = int(input())
qtd_comportadas = 0
qtd_nao_comportadas = 0
criancas = []

for i in range(qtd_nomes):
    dados_crianca = input().split()
    comportamento = dados_crianca[0]
    nome_crianca = dados_crianca[1]
    criancas.append(nome_crianca)
    if comportamento == '+':
        qtd_comportadas += 1
    else:
        qtd_nao_comportadas += 1
    
for crianca in sorted(criancas):
    print(crianca)
print(f'Se comportaram: {qtd_comportadas} | Nao se comportaram: {qtd_nao_comportadas}')