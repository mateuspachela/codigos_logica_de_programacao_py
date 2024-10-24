qtd_numeros = int(input()) # recebe a entrada do usuario de quantos numeros serão passados

lista_de_numeros_pares = [] # lista que armazena numeros pares
lista_de_numeros_impares = [] # lista que armazena numeros impares

for numero in range(qtd_numeros): # loop para adicionar as listas corretas os numeros pares e impares
    numero_usuario = int(input())
    if numero_usuario % 2 == 0: # se é par
        lista_de_numeros_pares.append(numero_usuario)
    else: # se é impar
        lista_de_numeros_impares.append(numero_usuario)

for numero_par in sorted(lista_de_numeros_pares): # loop para imprimir os numeros pares na ordem solicitada
    print(numero_par)
for numero_impar in sorted(lista_de_numeros_impares, reverse=True): # loop para imprimir os numeros impares na ordem solicitada
    print(numero_impar)