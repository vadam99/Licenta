import random

"""tabla = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]"""


tabla = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [2, 1, 4, 3, 6, 5, 8, 9, 7],
         [3, 6, 5, 8, 9, 7, 2, 1, 4],
         [8, 9, 7, 2, 1, 4, 3, 6, 5],
         [5, 3, 1, 6, 4, 2, 9, 7, 8],
         [6, 4, 2, 9, 7, 8, 5, 3, 1],
         [9, 7, 8, 5, 3, 1, 6, 4, 2]]


copie_tabla2 = [[tabla[i][j] for j in range(len(tabla[0]))] for i in range(len(tabla))]
copie_tabla = [[0 for i in range(9)] for j in range(9)]


lista_nr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def afisare(mat):
    for i in range(9):
        for j in range(9):
            print(mat[i][j], end=" ")
        print()
    return mat


def verificare_linii(nr, lin):
    for j in range(9):
        if copie_tabla2[lin][j] == nr:
            return False
    return True


def verificare_coloane(nr, col):
    for i in range(9):
        if copie_tabla2[i][col] == nr:
            return False
    return True


def verificare_zone(nr, lin, col):
    ii = lin // 3 * 3  # Patratele au fiecare cate 3 linii si 3 coloane. Fiecare patrat are prima linie numerotata cu 0, 3, sau 6.
    jj = col // 3 * 3  # ----------------------------------------------. Fiecare patrat are prima coloana numerotata cu 0, 3, sau 6.
    for i in range(3):
        for j in range(3):
            if copie_tabla2[ii + i][jj + j] == nr:  # Parcurgem fiecare patrat. ii reprezinta prima linie din patrat, iar jj prima coloana
                return False
    return True


def isValid(nr, lin, col):
    if not verificare_linii(nr, lin) or not verificare_coloane(nr, col) or not verificare_zone(nr, lin, col):
        return False
    return True


def bkt():
    for i in range(9):
        for j in range(9):
            if copie_tabla2[i][j] == 0:
                for nr in lista_nr:
                    if isValid(nr, i, j):
                        copie_tabla2[i][j] = nr
                        bkt()
                        copie_tabla2[i][j] = 0  # In caz ca nu am gasit o solutie la problema noastra, ne intoarcem la pasul/pasii anteriori si resetam schimbarea/schimbarile facuta/facute.
                return "Gata"
    for i in range(9):
        for j in range(9):
            copie_tabla[i][j] = copie_tabla2[i][j]
    afisare(copie_tabla2)
    print()


def shift_row(nr, board):
    while nr > 0:
        a = random.randint(0, 8)
        a = a // 3 * 3
        b = random.randint(0, 2)
        x = a + b
        j = 0
        while j < 9:
            board[a][j], board[x][j] = board[x][j], board[a][j]
            j += 1
        nr -= 1


def shift_col(nr, board):
    while nr > 0:
        a = random.randint(0, 8)
        a = a // 3 * 3
        b = random.randint(0, 2)
        x = a + b
        i = 0
        while i < 9:
            board[i][a], board[i][x] = board[i][x], board[i][a]
            i += 1
        nr -= 1


def genereaza_tabla():
    global copie_tabla2
    copie_tabla2 = [[tabla[i][j] for j in range(len(tabla[0]))] for i in range(len(tabla))]
    # Folosind tabla in loc de copie_tabla2 in aceasta functie imi punea k zerouri in tabla originala, ceea ce nu e corect in caz ca vrem sa apelam functia de mai multe ori
    shift_col(10, copie_tabla2)
    shift_row(10, copie_tabla2)
    print()
    k = 1
    while k > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        while copie_tabla2[i][j] == 0:  # Deoarece generam pozitii random, e posibil sa dam din nou peste o pozitie in care am pus deja 0, iar noi vrem ca variabila k sa arate cate pozitii vor avea 0.
            i = random.randint(0, 8)
            j = random.randint(0, 8)
        copie_tabla2[i][j] = 0
        k -= 1
    afisare(copie_tabla2)
    print()
    return copie_tabla2

#copie_tabla2 = genereaza_tabla()

# genereaza_tabla()
# genereaza_tabla()
# print("Solutia/Solutiile:")
# print(bkt())
# afisare(copie_tabla)

def verifica_numere(board):
    for i in range(9):
        for j in range(9):
            if 0 >= board[i][j] or board[i][j] > 9:
                return False
    return True


def verifica_linii(board):
    for i in range(9):
        d = dict()
        for j in range(9):
            nr = board[i][j]
            if nr != 0 and nr in d.keys():
                return False
            d[nr] = nr
        return True


def verifica_coloane(board):
    for j in range(9):
        d = dict()
        for i in range(9):
            nr = board[i][j]
            if nr != 0 and nr in d.keys():
                return False
            d[nr] = nr
    return True


def verifica_zone(board):
    for i in range(3):      # Prima linie din zona i
        for j in range(3):  # Prima coloana din zona j
            d = dict()
            for ii in range(3):
                for jj in range(3):
                    lin = ii + i * 3
                    col = jj + j * 3
                    nr = board[lin][col]
                    if nr != 0 and nr in d.keys():
                        return False
                    d[nr] = nr
    return True


def sudoku_valid(board):
    if not verifica_numere(board):
        return False
    if not verifica_linii(board) or not verifica_coloane(board) or not verifica_zone(board):
        return False
    return True

# print(sudoku_valid(copie_tabla))
