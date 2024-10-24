quantidade_listas_compra = int(input())
for lista in range(quantidade_listas_compra):
    lista_compra = sorted(set(input().split()))
    print(" ".join(lista_compra))