# Definição dos dicionários globais para armazenar os valores
dicionario_valores = {}
dicionario_valores_invertidos = {}
shifts_encontrados = []
caracteres_possiveis = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Função para criar o dicionário de caracteres para valores ASCII dentro dos permitidos pelo exercício
def criar_dicionario_asc():
    global dicionario_valores, caracteres_possiveis
    valores_lista = []
    for i in caracteres_possiveis:
        valor_atribuido = caracteres_possiveis.index(i)
        valores_lista.append(valor_atribuido)
    lista_letra = list(caracteres_possiveis)
    lista = (zip(lista_letra, valores_lista))
    dicionario = dict(lista)
    dicionario_valores = dicionario
    return dicionario_valores

# Função para criar o dicionário anterior invertido (valor para caractere)
def criar_dicionario_invertido():
    global dicionario_valores_invertidos, caracteres_possiveis
    valores_lista = []
    for i in caracteres_possiveis:
        valor_atribuido = caracteres_possiveis.index(i)
        valores_lista.append(valor_atribuido)
    lista_letra = list(caracteres_possiveis)
    lista = (zip(valores_lista, lista_letra))
    dicionario = dict(lista)
    dicionario_valores_invertidos = dicionario
    return dicionario_valores_invertidos

criar_dicionario_asc()
criar_dicionario_invertido()

# Função para verificar se a chave é válida e contém 5 caracteres permitidos
def is_valid_key(chave):
    caracteres_validos = 0
    for caractere in chave:
        if caractere in caracteres_possiveis:
            caracteres_validos += 1

    if caracteres_validos == 5:
        return True
    else:
        return False
    
# Função para verificar se a chave privada é o inverso da chave pública    
def is_inverse(chave_publica, chave_privada):
    if is_valid_key(chave):
        chave_publica_invertida = chave_publica[::-1]
        if chave_privada == chave_publica_invertida:
            return True
        else:
            return False

# Função para inverter uma mensagem (usada quando a chave privada é o inverso da pública)
def inverse(mensagem):
    mensagem_encriptada = mensagem[::-1]
    return print(f'Mensagem criptografada: {mensagem_encriptada}')

# Função para encontrar os shifts
def find_shifts(chave_publica, chave_privada, dicionario_valores):
    global shifts_encontrados
    valores_publica = []
    valores_privada = []
    shifts = []
    for i in chave_publica:
        caractere = dicionario_valores.get(i)
        valores_publica.append(caractere)

    for j in chave_privada:
        caractere = dicionario_valores.get(j)
        valores_privada.append(caractere)

    for valor_publica, valor_privada in zip(valores_publica, valores_privada):
        shift = valor_privada - valor_publica
        shifts.append(shift)
        shifts_encontrados = shifts
    return shifts_encontrados


# Função para criptografar a mensagem usando shifts fixos
def shift_encrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_encriptados = []
    lista_mensagem_encriptada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)
    for valor in valores_mensagem:
        valor_encriptado = valor + shifts_encontrados[0]
        valores_encriptados.append(valor_encriptado)
    for valor_encriptado in valores_encriptados:
        if valor_encriptado >= 0 and valor_encriptado <= 61:
            caractere_encriptado = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(caractere_encriptado)
        elif valor_encriptado < 0:
            valor_encriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)
        elif valor_encriptado > 61:
            valor_encriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)
    
    mensagem_encriptada = ''.join(lista_mensagem_encriptada)
    return print(f'Mensagem criptografada: {mensagem_encriptada}')

# Função para descriptografar a mensagem usando shifts fixos
def shift_decrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_descriptados = []
    lista_mensagem_descriptada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)
    for valor in valores_mensagem:
        valor_descriptado = valor - shifts_encontrados[0]
        valores_descriptados.append(valor_descriptado)
    for valor_descriptado in valores_descriptados:
        if valor_descriptado >= 0 and valor_descriptado <= 61:
            caractere_descriptado = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptada.append(caractere_descriptado)
        elif valor_descriptado < 0:
            valor_descriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptada.append(novo_valor)
        elif valor_descriptado > 61:
            valor_descriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptada.append(novo_valor)

    mensagem_descriptada = ''.join(lista_mensagem_descriptada)
    return print(f'Mensagem descriptografada: {mensagem_descriptada}')

# Função para encontrar shifts alternados
def find_shifts_alternate(chave_publica, chave_privada):
    valores_publica = []
    valores_privada = []
    shifts = []
    for i in chave_publica:
        caractere = dicionario_valores.get(i)
        valores_publica.append(caractere)

    for j in chave_privada:
        caractere = dicionario_valores.get(j)
        valores_privada.append(caractere)

    for valor_publica, valor_privada in zip(valores_publica, valores_privada):
        shift = valor_privada - valor_publica
        shifts.append(shift)
        shifts_encontrados = shifts
    return shifts_encontrados

# Função para criptografar a mensagem usando shifts alternados
def shifts_alternate_encrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_encriptados = []
    lista_mensagem_encriptada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)

    for index, valor in enumerate(valores_mensagem):
        shift_index = index % 2
        valor_encriptado = valor + shifts_encontrados[shift_index]
        valores_encriptados.append(valor_encriptado)

    for valor_encriptado in valores_encriptados:
        if valor_encriptado >= 0 and valor_encriptado <= 61:
            caractere_encriptado = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(caractere_encriptado)
        elif valor_encriptado < 0:
            valor_encriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)
        elif valor_encriptado > 61:
            valor_encriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)

    mensagem_encriptada = ''.join(lista_mensagem_encriptada)
    return print(f'Mensagem criptografada: {mensagem_encriptada}')

# Função para descriptografar a mensagem usando shifts alternados
def shifts_alternate_decrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_descriptados = []
    lista_mensagem_descriptografada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)

    for index, valor in enumerate(valores_mensagem):
        shift_index = index % 2
        valor_encriptado = valor - shifts_encontrados[shift_index]
        valores_descriptados.append(valor_encriptado)

    for valor_descriptado in valores_descriptados:
        if valor_descriptado >= 0 and valor_descriptado <= 61:
            caractere_descriptado = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(caractere_descriptado)
        elif valor_descriptado < 0:
            valor_descriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(novo_valor)
        elif valor_descriptado > 61:
            valor_descriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(novo_valor)

    mensagem_encriptada = ''.join(lista_mensagem_descriptografada)
    return print(f'Mensagem descriptografada: {mensagem_encriptada}')

# Função para encontrar shifts variáveis
def find_variable_shifts(chave_publica, chave_privada):
    valores_publica = []
    valores_privada = []
    shifts = []
    for i in chave_publica:
        caractere = dicionario_valores.get(i)
        valores_publica.append(caractere)

    for j in chave_privada:
        caractere = dicionario_valores.get(j)
        valores_privada.append(caractere)

    for valor_publica, valor_privada in zip(valores_publica, valores_privada):
        shift = valor_privada - valor_publica
        shifts.append(shift)
        shifts_encontrados = shifts
    return shifts_encontrados

# Função para criptografar a mensagem usando shifts variáveis
def variable_shifts_encrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_encriptados = []
    lista_mensagem_encriptada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)

    for index, valor in enumerate(valores_mensagem):
        shift_index = index % 5
        valor_encriptado = valor + shifts_encontrados[shift_index]
        valores_encriptados.append(valor_encriptado)

    for valor_encriptado in valores_encriptados:
        if valor_encriptado >= 0 and valor_encriptado <= 61:
            caractere_encriptado = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(caractere_encriptado)
        elif valor_encriptado < 0:
            valor_encriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)
        elif valor_encriptado > 61:
            valor_encriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_encriptado)
            lista_mensagem_encriptada.append(novo_valor)

    mensagem_encriptada = ''.join(lista_mensagem_encriptada)
    return print(f'Mensagem criptografada: {mensagem_encriptada}')

# Função para descriptografar a mensagem usando shifts variáveis
def variable_shifts_decrypt(shifts_encontrados, mensagem):
    valores_mensagem = []
    valores_descriptados = []
    lista_mensagem_descriptografada = []

    for i in mensagem:
        caractere = dicionario_valores.get(i)
        valores_mensagem.append(caractere)

    for index, valor in enumerate(valores_mensagem):
        shift_index = index % 5
        valor_encriptado = valor - shifts_encontrados[shift_index]
        valores_descriptados.append(valor_encriptado)

    for valor_descriptado in valores_descriptados:
        if valor_descriptado >= 0 and valor_descriptado <= 61:
            caractere_descriptado = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(caractere_descriptado)
        elif valor_descriptado < 0:
            valor_descriptado += 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(novo_valor)
        elif valor_descriptado > 61:
            valor_descriptado -= 62
            novo_valor = dicionario_valores_invertidos.get(valor_descriptado)
            lista_mensagem_descriptografada.append(novo_valor)

    mensagem_encriptada = ''.join(lista_mensagem_descriptografada)
    return print(f'Mensagem descriptografada: {mensagem_encriptada}')
    
# Função para verificar se os shifts são fixos
def shift_fixo(shifts_encontrados):
    if all(shift == shifts_encontrados[0] for shift in shifts_encontrados):
        return True
    else:
        return False
    
# Função para verificar se os shifts são alternados    
def shift_alternado(shifts_encontrados):
    for shift in range(1, len(shifts_encontrados)):
        if shifts_encontrados[shift] != -shifts_encontrados[shift-1]:
            return False
    
    return True

# Função para verificar se os shifts são pares repetidos
def shift_par(shifts_encontrados):
    if shifts_encontrados[0] == shifts_encontrados[2] and shifts_encontrados[1] == shifts_encontrados[3]:
        return True
    elif shifts_encontrados[0] == shifts_encontrados[2] and shifts_encontrados[1] == shifts_encontrados[3] + 62:
        return True
    elif shifts_encontrados[0] == shifts_encontrados[2] + 62 and shifts_encontrados[1] == shifts_encontrados[3]:
        return True
    else:
        return False

# Loop principal que lê comandos do usuário até ele digitar exit e sair do programa.
while True:

    entrada_comando = input()
    if entrada_comando == 'public_key':
        chave = input()
        chave_publica = chave
        resultado = is_valid_key(chave)
        if resultado:
            print('Chave pública válida')
        else:
            print('Chave pública inválida')

    elif entrada_comando == 'private_key':
        chave = input()
        chave_privada = chave
        resultado = is_valid_key(chave)
        if resultado:
            print('Chave privada válida')
        else:
            print('Chave privada inválida')

    elif entrada_comando == 'encrypt':
        mensagem = input()
        if is_inverse(chave_publica,chave_privada):
            inverse(mensagem)
        else:
            find_shifts(chave_publica, chave_privada, dicionario_valores)
            shift_fixo(shifts_encontrados)
            shift_alternado(shifts_encontrados)
            shift_par(shifts_encontrados)

            if shift_fixo(shifts_encontrados):
                shift_encrypt(shifts_encontrados, mensagem)
            elif shift_alternado(shifts_encontrados) or shift_par(shifts_encontrados):
                shifts_alternate_encrypt(shifts_encontrados, mensagem)
            else:
                variable_shifts_encrypt(shifts_encontrados, mensagem)


    elif entrada_comando == 'decrypt':
        mensagem = input()
        if is_inverse(chave_publica,chave_privada):
            inverse(mensagem)
        else:
            find_shifts(chave_publica, chave_privada, dicionario_valores)
            shift_fixo(shifts_encontrados)
            if shift_fixo(shifts_encontrados):
                shift_decrypt(shifts_encontrados, mensagem)
            elif shift_alternado(shifts_encontrados):
                shifts_alternate_decrypt(shifts_encontrados, mensagem)
            else:
                variable_shifts_decrypt(shifts_encontrados, mensagem)
    elif entrada_comando == 'exit':
        break


