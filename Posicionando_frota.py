def define_posicoes (linha, coluna, orientacao, tamanho):
    lista = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha+i)
            posicao.append(coluna)
            lista.append(posicao)

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha)
            posicao.append(coluna+i)
            lista.append(posicao)


    return lista


def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)

    if orientacao == 'vertical' and 10 - linha < tamanho:
        return False
    
    if orientacao == 'horizontal' and 10 - coluna < tamanho:
        return False
    

    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        for tipo, posicoes in frota.items():
            for posicao in posicoes:
                for linha_frota, coluna_frota in posicao:
                    if linha == linha_frota and coluna == coluna_frota:
                        return False
                    
    return True

def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):


    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))

    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]

    
    return frota


# Posicionando frota:
embarcacoes = {1: ['porta-aviões', 4], 2:['navio-tanque', 3], 3:['navio-tanque', 3], 4:['contratorpedeiro', 2], 5:['contratorpedeiro', 2], 6:['contratorpedeiro', 2], 7: ['submarino',1], 8: ['submarino',1], 9: ['submarino',1], 10: ['submarino',1]}
frota = {}
i = 1
while i <= len(embarcacoes):
    nome = embarcacoes[i][0]
    tamanho = embarcacoes[i][1]
    
    print ('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome, tamanho))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if nome != 'submarino':
        orientacao = int(input('Vertical(1) ou Horizontal(2): '))
        
    if orientacao == 1:
        orientacao = 'vertical'
    elif orientacao == 2:
        orientacao = 'horizontal'

    valido = posicao_valida (frota, linha, coluna, orientacao, tamanho)

    if valido == False:
        print('Esta posição não está válida!')
    
    else:
        lista_posicoes = define_posicoes (linha, coluna, orientacao, tamanho)
        frota = preenche_frota (frota, nome, linha, coluna, orientacao, tamanho)
        i += 1

