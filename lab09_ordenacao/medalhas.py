def sort_placement(pais):
    return (-pais[1], -pais[2], -pais[3], pais[0])

num_paises = int(input())

informacao_paises = []
for i in range(num_paises): # cria lista com tuplas ("medalahs de ouro", "medalhas de prata", "medalhas de bronze", "nome do país")
    nome_pais, score_pais = input().split(maxsplit=1)
    medalha_ouro, medalha_prata, medalha_bronze = map(int, score_pais.split())
    informacao_paises.append((nome_pais, medalha_ouro, medalha_prata, medalha_bronze))

informacao_paises.sort(key=sort_placement) # ordena colocação dos países

for pais in informacao_paises:
    print(*pais)