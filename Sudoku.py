jogo = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# FUNÇÃO QUE SEPARA OS NUMEROS EM FORMA DE SUDOKU
def sudoku(jg):
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            print('---------------------')

        for j in range(0, 9):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(jg[i][j])
            else:
                print(str(jg[i][j]) + " ", end='')


# FUNÇÃO QUE UTILIZA BACKTRACKING PARA OBTER O RESULTADO CORRETO NO SUDOKU
def resolver(jg):

    casa = casavazia(jg)
    # O CODIGO PEGA UMA CASA VAZIA POR VEZ PARA SER PREENCHIDA
    # SE NÃO OUVER CASAS A SER PREENCHIDA O SUDOKU ESTA COMPLETO, ENTÃO ELE PRINTA O JOGO E ENCERRA A FUNÇÃO
    if not casa:
        sudoku(jg)
        return
    else:
        i, j = casa

    for num in range(1, 10):
        if validar(jg, num, (i, j)):
            jg[i][j] = num
            resolver(jg)
            jg[i][j] = 0


# FUNÇÃO QUE VERIFICA SE A CASA ESTA VAZIA OU NÃO
def casavazia(jg):
    for i in range(len(jg)):
        for j in range(len(jg[0])):
            if jg[i][j] == 0:
                return (i, j)


# FUNÇÃO QUE VALIDA SE A CASA QUE O NUMERO ESTA CORRETA
def validar(jg, num, pos):
    # LINHA
    for i in range(0, 9):
        if jg[pos[0]][i] == num and pos[1] != i:
            return False

    # COLUNA
    for i in range(0, 9):
        if jg[i][pos[1]] == num and pos[0] != i:
            return False

    # BLOCO
    if pos[0] == 0 or pos[0] == 1 or pos[0] == 2:
        xbox = [0, 1, 2]
    elif pos[0] == 3 or pos[0] == 4 or pos[0] == 5:
        xbox = [3, 4, 5]
    else:
        xbox = [6, 7, 8]

    if pos[1] == 0 or pos[1] == 1 or pos[1] == 2:
        ybox = [0, 1, 2]
    elif pos[1] == 3 or pos[1] == 4 or pos[1] == 5:
        ybox = [3, 4, 5]
    else:
        ybox = [6, 7, 8]

    for i in range(len(jg)):
        for j in range(len(jg[0])):
            if i in xbox and j in ybox:
                if jg[i][j] == num and pos != (i, j):
                    return False
    return True


resolver(jogo)


'''
# TESTE MANUAL DE VALIDAÇÃO DE NUMERO
if validar(jogo, 7, [0, 2]):
    print('CERTO')
else:
    print('ERRADO')
'''
