salario_anual = float(input()) # A pessoa usuária deve informar o valor do salário anual.
despesas_pagas_anual = float(input()) # A pessoa usuária deve informar as despesas pagas ao longo do ano vigente.
imposto_pago = float(input()) # A pessoa usuária deve informar o valor de imposto já pago.

# o “Leão IR” realizará dois tipos de cálculos: o cálculo completo e o cálculo simplificado.

# dos dados tirados da tabela:
faixa_salarial_um = 22847.76
aliquota_um = 0.0
deducao_ir_um = 0.0

faixa_salarial_dois = 33919.80
aliquota_dois = 0.075
deducao_ir_dois = 1713.58

faixa_salarial_tres = 45012.60
aliquota_tres = 0.15
deducao_ir_tres = 4257.57

faixa_salarial_quatro = 55976.16
aliquota_quatro = 0.225
deducao_ir_quatro = 7633.51

faixa_salarial_cinco = 5976.17
aliquota_cinco = 0.275
deducao_ir_cinco = 10432.32

# fazendo o calculo completo com as regras dadas pelo exercicio

renda_tributavel = salario_anual - despesas_pagas_anual # renda tributavel de acordo com o exercicio

if renda_tributavel <= faixa_salarial_um:
    aliquota = aliquota_um
    deducao_ir = deducao_ir_um
elif renda_tributavel <= faixa_salarial_dois:
    aliquota = aliquota_dois
    deducao_ir = deducao_ir_dois
elif renda_tributavel <= faixa_salarial_tres:
    aliquota = aliquota_tres
    deducao_ir = deducao_ir_tres
elif renda_tributavel <= faixa_salarial_quatro:
    aliquota = aliquota_quatro
    deducao_ir = deducao_ir_quatro
else:
    aliquota = aliquota_cinco
    deducao_ir = deducao_ir_cinco
       
calcular_completo = (renda_tributavel * aliquota) - (imposto_pago + deducao_ir)

# fazendo o calculo simplificado com as regras dadas pelo exercicio

deducao_simplificada = 0.2 * salario_anual
deducao_simplificada_max = 16754.34

if deducao_simplificada >= deducao_simplificada_max:  
    deducao_simplificada = deducao_simplificada_max
else:
    deducao_simplificada

renda_tributavel_simplificada = salario_anual - deducao_simplificada

if renda_tributavel_simplificada <= faixa_salarial_um:
    aliquota = aliquota_um
    deducao_ir = deducao_ir_um
elif renda_tributavel_simplificada <= faixa_salarial_dois:
    aliquota = aliquota_dois
    deducao_ir = deducao_ir_dois
elif renda_tributavel_simplificada <= faixa_salarial_tres:
    aliquota = aliquota_tres
    deducao_ir = deducao_ir_tres
elif renda_tributavel_simplificada <= faixa_salarial_quatro:
    aliquota = aliquota_quatro
    deducao_ir = deducao_ir_quatro
else:
    aliquota = aliquota_cinco
    deducao_ir = deducao_ir_cinco

calcular_simplificado = (renda_tributavel_simplificada * aliquota) - (deducao_ir + imposto_pago)

# definindo as condicoes para cada print

if calcular_simplificado <= calcular_completo:
    calculo_final = calcular_simplificado
else:
    calculo_final = calcular_completo

if calculo_final >= 0:
    print(f'VALOR A PAGAR: R$ {calculo_final:.2f}')
else:
    calculo_final *= -1
    print(f'VALOR A SER RESSARCIDO: R$ {calculo_final:.2f}')