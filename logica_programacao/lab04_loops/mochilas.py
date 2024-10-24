mochilas = input().split() # recebe do usuario as mochilas e seus itens pertencentes

for i in range(0, len(mochilas)):
    tamanho_mochila = len(mochilas[i]) # calcula o tamanho da mochila
    divisao_compartimentos = tamanho_mochila // 2 # calcula quantos itens deve haver em cada compartimento
    compartimento_um = mochilas[i][:divisao_compartimentos] # pega a primeira metade da string da mochila e armazena no compartimento um
    compartimento_dois = mochilas[i][divisao_compartimentos:] # pega a segunda metade da string da mochila e armazena no compartimento dois
    itens_repetidos = []
    
    for item in compartimento_um: # iteração para verificar os itens repetidos dos compartimentos
        if item in compartimento_dois and item not in itens_repetidos:
            itens_repetidos.append(item)

    if len(itens_repetidos) > 0: # condições para print de saída a partir da repetição de itens ou não
        for item_repetido in itens_repetidos:
            print(f'mochila {i + 1}: {item_repetido}')
    else:
        print(f'mochila {i + 1}: Sem item repetido')