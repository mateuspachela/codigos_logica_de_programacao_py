dias_user = int(input())
anos = 0
meses = 0
dias = 0
    
if dias_user >= 365:
    anos = dias_user // 365
    meses = (dias_user - (anos * 365)) // 30
    dias = dias_user - (anos * 365 + meses * 30)
    
if dias_user >= 30 and dias_user < 365:
    meses = dias_user // 30
    dias = dias_user % 30
    anos = 0   
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')