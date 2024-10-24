identificacao_notas = 'WHQESTX'
valores_notas = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]
dicionario_notas = dict(zip(identificacao_notas, valores_notas))

tolerancia = 1e-9 # define a tolerância para a comparação de floats

while True:
    entrada_usuario = input().strip()
    if entrada_usuario == '*':  # verifica se a entrada é o asterisco indicando o fim
        break

    compassos_validos = 0
    compassos = entrada_usuario.split('/')[1:-1]  # divide a entrada em compassos e remove as barras iniciais e finais
    
    for compasso in compassos:
        valor_compasso = sum(dicionario_notas.get(letra, 0) for letra in compasso)
        if abs(valor_compasso - 1.0) < tolerancia:  # verifica se o valor do compasso é aproximadamente 1
            compassos_validos += 1
    
    print(compassos_validos)