#ihiyhyih
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes=[]
    if orientacao== 'vertical':
        for i in range(tamanho):
            posicoes.append([linha+i,coluna])
    elif orientacao== 'horizontal':
        for j in range(tamanho):
            posicoes.append([linha,coluna+j])
    return posicoes

def preenche_frota(dic,n_navio,l,c,ori,tam):
    if n_navio not in dic:
        dic[n_navio]=[define_posicoes(l,c,ori,tam)]
    else:
        dic[n_navio].append(define_posicoes(l,c,ori,tam))
    return dic

def faz_jogada(tabu,linha,coluna):
    if tabu[linha][coluna] == 1:
        tabu[linha][coluna]='X'
    else:
        tabu[linha][coluna]='-'
    return tabu

def posiciona_frota(frota):
    grid=[0]*10
    for i in range(len(grid)):
        grid[i]=[0]*10
    for cordenadas in frota.values():
        for j in cordenadas:
            for i in j:
                linha=i[0]
                coluna=i[1]
                grid[linha][coluna]=1
    return grid

def afundados(frota,tabuleiro):
    resultado=0
    afundado=False
    for cordenadas in frota.values():
        for i in cordenadas:
            for k in i:
                linha=k[0]
                coluna=k[1]
                if tabuleiro[linha][coluna]=='X':
                    afundado= True
                else:
                    afundado= False
                    break
            if afundado== True:
                resultado+=1
    return resultado                


            