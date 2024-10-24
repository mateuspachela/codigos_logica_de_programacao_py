quantidade_alimentos = int(input())
todos_alimentos = []

'''for para armazenar as informacoes dos alimentos a partir da quantidade de alimentos que
foi informada pelo usuario'''
for i in range(quantidade_alimentos):
    ficha_alimento = input().split()
    nome_alimento = ficha_alimento[0]
    quantidade_protein_packets = ficha_alimento[1]
    quantidade_code_carbs = ficha_alimento[2]
    quantidade_data_lipids = ficha_alimento[3]
    todos_alimentos.append(ficha_alimento) # adicionando alimento e suas quantidades a uma lista com todos os alimentos disponiveis

quantidade_atletas = int(input())

'''for para armazenar as informacoes dos atletas a partir da quantidade de atletas que
foi informada pelo usuario'''
for i in range(quantidade_atletas):
    ficha_atleta = input().split()
    nome_atleta = ficha_atleta[0]
    qtd_necessaria_pp = float(ficha_atleta[1])
    qtd_necessaria_cc = float(ficha_atleta[2])
    qtd_necessaria_dl = float(ficha_atleta[3])
    alimentos_cafe = input().split()
    alimentos_almoco = input().split()
    alimentos_janta = input().split()
    qtd_consumida_pp = 0 
    qtd_consumida_cc = 0
    qtd_consumida_dl = 0

    for indice, alimento in enumerate(todos_alimentos): # for que percorre todos os alimentos possiveis
        for i in alimentos_cafe: # for que percorre os alimentos que o atleta comeu pela manha
            if alimento[0] == i: # compara com a lista de todos os alimentos para calcular a quantidade de nutrientes que foi consumida pelo atleta
                qtd_consumida_pp += float(alimento[1])
                qtd_consumida_cc += float(alimento[2])
                qtd_consumida_dl += float(alimento[3])
        for j in alimentos_almoco: # for que percorre os alimentos que o atleta comeu no almoço
            if alimento[0] == j: # compara com a lista de todos os alimentos para calcular a quantidade de nutrientes que foi consumida pelo atleta
                qtd_consumida_pp += float(alimento[1])
                qtd_consumida_cc += float(alimento[2])
                qtd_consumida_dl += float(alimento[3])
        for k in alimentos_janta: # for que percorre os alimentos que o atleta comeu no almoço
            if alimento[0] == k: # compara com a lista de todos os alimentos para calcular a quantidade de nutrientes que foi consumida pelo atleta
                qtd_consumida_pp += float(alimento[1])
                qtd_consumida_cc += float(alimento[2])
                qtd_consumida_dl += float(alimento[3])
    

    '''variaveis para verificar se o atleta consumiu o suficiente'''
    avaliacao_pp = qtd_necessaria_pp - qtd_consumida_pp
    avaliacao_cc = qtd_necessaria_cc - qtd_consumida_cc
    avaliacao_dl = qtd_necessaria_dl - qtd_consumida_dl
    protein_packets = [avaliacao_pp, 'ProteinPackets', qtd_consumida_pp] # lista com a quantidade e o nome do macronutriente
    code_carbs = [avaliacao_cc, 'CodeCarbs', qtd_consumida_cc] # lista com a quantidade e o nome do macronutriente
    data_lipids = [avaliacao_dl, 'DataLipids', qtd_consumida_dl] # lista com a quantidade e o nome do macronutriente
    avaliacao_geral = [protein_packets, code_carbs, data_lipids] # lista com as listas dos macronutrientes e suas informacoes
    print(nome_atleta)

    ''' for para atender as condicoes de saida'''
    for avaliacao in avaliacao_geral:
        if avaliacao[0] > 0:
            print(f'{avaliacao[0]:.1f} gramas de {avaliacao[1]} em falta')
        elif avaliacao[0] == 0:
            print(f'{avaliacao[2]:.1f} gramas de {avaliacao[1]} adequado')
        else:
            print(f'{-avaliacao[0]:.1f} gramas de {avaliacao[1]} em excesso')
