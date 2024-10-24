#lab9.2
contador = False
while True:
    try:
        linha = input().strip()
        if linha == "":
            continue
        frequencia_valor = {}
        for caractere in linha:
            if caractere in frequencia_valor:
                frequencia_valor[caractere] += 1
            else:
                frequencia_valor[caractere] = 1

        lista_frequencia = []
        for caractere, freq in frequencia_valor.items():
            lista_frequencia.append((freq, -ord(caractere), caractere))

        lista_frequencia.sort()
        #printar linha por linha
        mensagem = []
        for freq, _, caractere in lista_frequencia:
            mensagem.append(f'{ord(caractere)} {freq}')

        if contador:
            print('')
        print("\n".join(mensagem))
        contador = True 

            
    except EOFError:
        break