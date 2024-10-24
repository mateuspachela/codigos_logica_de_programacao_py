numero_casos = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range(1, numero_casos + 1):
    quantia = input().split()
    numero = int(quantia[0])
    ultima_letra = quantia[-1]

    if ultima_letra == 'C':
        coelhos += numero
    elif ultima_letra == 'R':
        ratos += numero
    elif ultima_letra == 'S':
        sapos += numero
        
total_cobaias = int(coelhos + ratos + sapos)
percentual_coelhos = (coelhos / total_cobaias) * 100
percentual_ratos = (ratos / total_cobaias) * 100
percentual_sapos = (sapos / total_cobaias) * 100

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percentual_coelhos:.2f} %')
print(f'Percentual de ratos: {percentual_ratos:.2f} %')
print(f'Percentual de sapos: {percentual_sapos:.2f} %')