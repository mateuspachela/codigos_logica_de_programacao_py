while True:
    
    quantidade_alunos = int(input())

    if quantidade_alunos == 0:
        break
    
    dicionario_alunos_original = {}

    for aluno in range(quantidade_alunos):
        assinatura_aluno = input().split()
        nome_aluno = assinatura_aluno[0]
        assinatura_original = assinatura_aluno[1]
        dicionario_alunos_original[nome_aluno] = assinatura_original 

    quantidade_comparecimento = int(input())

    assinaturas_falsas = 0

    for comparecimento in range(quantidade_comparecimento):
        assinatura_em_sala = input().split()
        nome = assinatura_em_sala[0]
        assinatura = assinatura_em_sala[1]
        assinatura_original = dicionario_alunos_original[nome]

        diferencas = 0
        for caractere_original, caractere_assinado in zip(assinatura_original, assinatura): 
            if caractere_original != caractere_assinado:
                diferencas += 1
        
        if diferencas > 1:
            assinaturas_falsas += 1

    print(assinaturas_falsas)