qtd_divisoes = int(input())
for i in range(1, qtd_divisoes+1):
    numeros = input().split()
    numero_um = int(numeros[0])
    numero_dois = int(numeros[-1])
    if numero_dois == 0:
        print('divisao impossivel')
    else:
        divisao = numero_um / numero_dois
        print(f'{divisao:.1f}')