numero_instancias = int(input())

for instancia in range(numero_instancias):

    dicionario_traducao = {}
    linhas_traduzidas = []

    palavras_linhas = input().split()
    palavras = int(palavras_linhas[0])
    linhas = int(palavras_linhas[1])

    for i in range(palavras):
        palavra = input()
        traducao = input()
        dicionario_traducao[palavra] = traducao
    
    for j in range(linhas):
        linha_traduzida = []

        letra_musica = input().split()
        
        for word in letra_musica:
            if word in dicionario_traducao:
                linha_traduzida.append(dicionario_traducao[word])
            else:
                linha_traduzida.append(word)
        
        print(' '.join(linha_traduzida))
    print()