#lab08
def contar_arvores_invisiveis(matriz_arvores, altura, largura): # funcao para contar as arvores inviseveis da vista de fora
    global posicoes_arvores
    visiveis = [[False] * largura for _ in range(altura)] # compreensao de lista para criar uma lista do tamanho da matriz que recebemos de entrada com termos booleanos True e False

    # loop para considerar todas as arvores das bordas visiveis de uma visao de fora
    for i in range(altura):
        visiveis[i][0] = True
        visiveis[i][largura - 1] = True
    for j in range(largura):
        visiveis[0][j] = True
        visiveis[altura - 1][j] = True
    
    # loop para olhar as arvores que nao sao da borda e ver se sao visiveis de baixo, ou de cima, ou da esquerda, ou da direita
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):

            # checar para cima
            visao_cima = True
            for k in range(i):
                if matriz_arvores[k][j] >= matriz_arvores[i][j]:
                    visao_cima = False
                    break
            
            # checar para baixo
            visao_baixo = True
            for k in range(i + 1, altura):
                if matriz_arvores[k][j] >= matriz_arvores[i][j]:
                    visao_baixo = False
                    break
            
            # checar para a esquerda
            visao_esquerda = True
            for k in range(j):
                if matriz_arvores[i][k] >= matriz_arvores[i][j]:
                    visao_esquerda = False
                    break
            
            # checar para a direita
            visao_direita = True
            for k in range(j + 1, largura):
                if matriz_arvores[i][k] >= matriz_arvores[i][j]:
                    visao_direita = False
                    break
        
            
            # se visível de qualquer direção, marcar como visível
            if visao_cima or visao_baixo or visao_esquerda or visao_direita:
                visiveis[i][j] = True
    
    # contar árvores invisíveis
    posicoes_arvores = []
    for i in range(altura):
        for j in range(largura):
            if not visiveis[i][j]:
                posicoes_arvores.append([i,j])

    return posicoes_arvores

def arvore_escolhida(matriz_arvores, posicoes_arvores, altura, largura): # funcao para achar a melhor arvore possivel diante das arvores que achamos na primeira funcao
    global melhor_arvore, max_visiveis
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] # 8 direções possiveis para visualizar
    max_visiveis = 0 # variavel que armazena as arvores visiveis do ponto de vista da arvore analisada
    melhor_arvore = None # variavel que armazena a posicao da melhor arvore

    for arvore in posicoes_arvores: # loop para analisar as arvores que constaram invisiveis do lado de fora
        x, y = arvore
        qtd_vizinhas = 0

        for direcao in direcoes: # loop para analisar todas as direcoes possiveis
            dx, dy = direcao
            nx, ny = x + dx, y + dy

            while 0 <= nx < altura and 0 <= ny <largura: # condicao para analisar até a ultima posicao possivel da matriz naquela direção

                if matriz_arvores[nx][ny] >= matriz_arvores[x][y]: # condicao para contar as arvores visiveis
                    qtd_vizinhas += 1
                    break
                else:
                    qtd_vizinhas += 1
                nx += dx
                ny += dy
                
        if qtd_vizinhas > max_visiveis: # condicao para verificar quantas arvores sao visiveis e propor a melhor arvore a ser escolhida
            max_visiveis = qtd_vizinhas
            melhor_arvore = (x,y)
    
    return melhor_arvore, max_visiveis


def print_saida(posicoes_arvores, melhor_arvore, max_visiveis): # funcao para printar de acordo com o que o exercicio pede
    print(f'Árvores candidatas:')
    for posicao in posicoes_arvores:
        print(f'{posicao[0]},{posicao[1]}')
    print(f'Árvore escolhida:')
    print(f'{melhor_arvore[0]},{melhor_arvore[1]} com {max_visiveis} árvores visíveis.')




altura_e_largura = input().split(',') # entrada do usuario com a matriz de arvores

altura = int(altura_e_largura[0])
largura = int(altura_e_largura[1])

matriz_arvores = []
for linha in range(altura): # loop para armazenar a matriz recebida pelo usuario
    altura_arvore = input()
    row = []
    for c in altura_arvore:
        row.append(int(c))
    matriz_arvores.append(row)

# invocação das funcoes que foram solicitadas
contar_arvores_invisiveis(matriz_arvores, altura, largura)
arvore_escolhida(matriz_arvores, posicoes_arvores, altura, largura)
print_saida(posicoes_arvores, melhor_arvore, max_visiveis)