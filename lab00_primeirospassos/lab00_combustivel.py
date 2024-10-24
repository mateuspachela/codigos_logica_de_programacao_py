consumo_km_l = 12
tempo_gasto = int(input())
velocidade_media = int(input())
distancia_percorrida = velocidade_media * tempo_gasto
litros_necessarios = distancia_percorrida / consumo_km_l
print(f'{litros_necessarios:.3f}')