quantidade_ida_feira = int(input())
dicionario_produtos = {}

for ida in range(quantidade_ida_feira):
    valor_gasto = 0
    quantidade_produtos_disponiveis = int(input())
    for produto in range(quantidade_produtos_disponiveis):
        produto_preco = input().split()
        dicionario_produtos[produto_preco[0]] = float(produto_preco[1])
    quantidade_compras_parcinova = int(input())
    for compra in range(quantidade_compras_parcinova):
        produto_desejado = input().split()
        quantidade_produto = int(produto_desejado[1])
        if produto_desejado[0] in dicionario_produtos:
            valor_produto = dicionario_produtos.get(produto_desejado[0])
            valor_gasto += valor_produto * quantidade_produto
    print(f'R$ {valor_gasto:.2f}')